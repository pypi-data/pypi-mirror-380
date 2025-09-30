"""The top-level module for survey related data, such as pointing and noise
information. ObsTable class is a base class with specific implementations
for different survey data, such as Rubin and ZTF."""

import sqlite3
from pathlib import Path

import astropy.units as u
import numpy as np
import pandas as pd
from astropy.coordinates import Latitude, Longitude
from mocpy import MOC
from regions import Region
from scipy.spatial import KDTree

from lightcurvelynx.astro_utils.detector_footprint import DetectorFootprint


class ObsTable:
    """A wrapper class around the observations table with helper computation functions and
    cached data for efficiency.

    Parameters
    ----------
    table : dict or pandas.core.frame.DataFrame
        The table with all the survey information. Metadata can be included in the
        "lightcurvelynx_survey_data" entry of the attributes dictionary.
    colmap : dict, optional
        A mapping of standard column names to their names in the input table.
        For example, in Rubin's OpSim we might have the column "observationStartMJD"
        which maps to "time". In that case we would have an entry with key="time"
        and value="observationStartMJD".
    detector_footprint : astropy.regions.SkyRegion, Astropy.regions.PixelRegion, or
        DetectorFootprint, optional
        The footprint object for the instrument's detector. If None, no footprint
        filtering is done. Default is None.
    wcs : astropy.wcs.WCS, optional
        The WCS for the footprint. Either this or pixel_scale must be provided if
        a footprint is provided as a Astropy region.
    **kwargs : dict
        Additional keyword arguments to pass to the constructor. This can include
        overrides of any of the survey values.

    Attributes
    ----------
    survey_values : dict, optional
        A mapping for constant values for the survey used in various computations, such
        as readout noise and dark current.
    filters : np.ndarray
        The unique filters in the survey table (if provided).
    _table : pandas.core.frame.DataFrame
        The table with all the observation information mapped to standard column names.
    _colmap : dict
        A mapping of standard column names to their names in the input table.
    _inv_colmap : dict
        A dictionary mapping the custom column names back to the standard names.
    _kd_tree : scipy.spatial.KDTree or None
        A kd_tree of the survey pointings for fast spatial queries. We use the scipy
        kd-tree instead of astropy's functions so we can directly control caching.
    _detector_footprint : DetectorFootprint, optional
        The footprint object for the instrument's detector. If None, no footprint
        filtering is done. Default is None.
    _wacs : astropy.wcs.WCS, optional
        The WCS for the footprint.
    """

    _required_columns = ["ra", "dec", "time"]

    # Default survey values. These are all None for the abstract base class.
    _default_survey_values = {
        "dark_current": None,
        "ext_coeff": None,
        "pixel_scale": None,
        "radius": None,
        "read_noise": None,
        "zp_per_sec": None,
        "survey_name": "Unknown",
    }

    def __init__(
        self,
        table,
        *,
        colmap=None,
        detector_footprint=None,
        wcs=None,
        **kwargs,
    ):
        # Create a copy of the table.
        if isinstance(table, dict):
            self._table = pd.DataFrame(table)
        else:
            self._table = table.copy()

        # Remap the columns to standard names. Start with the existing names (from the table)
        # and overwrite anything provided by the column map. Save the inverse mapping.
        name_map = {col: col for col in self._table.columns}
        self._inv_colmap = {}
        self._colmap = colmap if colmap is not None else {}
        if colmap is not None:
            for key, value in colmap.items():
                if value in name_map:
                    # Check for collisions (mapping a column to an existing column)
                    if key in self._table.columns and key != value:
                        raise ValueError(f"Trying to map {value} to {key}, but {key} is already a column.")

                    # Add this entry to the list of column names that need to be remapped.
                    name_map[value] = key

                # Save the inverse mapping as well
                self._inv_colmap[value] = key
        self._table.rename(columns=name_map, inplace=True)

        # Check that we have the required columns.
        for col in self._required_columns:
            if col not in self._table.columns:
                raise KeyError(f"Missing required column: {col}")

        # Save the survey values, overwriting anything that is manually specified
        # as a keyword argument or provided in the table's metadata.
        self.survey_values = self._default_survey_values.copy()
        if "lightcurvelynx_survey_data" in self._table.attrs:
            metadata = self._table.attrs["lightcurvelynx_survey_data"]
            if not isinstance(metadata, dict):
                raise TypeError("Got unexpected type for lightcurvelynx_survey_data")
            for key, value in metadata.items():
                self.survey_values[key] = value
        for key, value in kwargs.items():
            self.survey_values[key] = value

        self.filters = np.unique(self._table["filter"]) if "filter" in self._table.columns else np.array([])

        # If we are not given zero point data, try to derive it from the other columns.
        if "zp" not in self:
            self._assign_zero_points()

        # Build the kd-tree.
        self._kd_tree = None
        self._build_kd_tree()

        # Create the footprint if one is provided.
        self._wcs = wcs
        if isinstance(detector_footprint, Region):
            pixel_scale = self.survey_values.get("pixel_scale", None)
            detector_footprint = DetectorFootprint(detector_footprint, wcs=wcs, pixel_scale=pixel_scale)
        self._detector_footprint = detector_footprint

    def __len__(self):
        return len(self._table)

    def __getitem__(self, key):
        """Access the underlying observation table by column name."""
        if key in self._table.columns:
            return self._table[key]
        if key in self._inv_colmap and self._inv_colmap[key] in self._table.columns:
            return self._table[self._inv_colmap[key]]
        raise KeyError(f"Column not found: {key}")

    def __contains__(self, key):
        """Check if a column exists in the survey table."""
        if key in self._table.columns:
            return True
        if key in self._inv_colmap and self._inv_colmap[key] in self._table.columns:
            return True
        return False

    def clear_detector_footprint(self):
        """Clear the detector footprint, so no footprint filtering is done."""
        self._detector_footprint = None

    def _assign_constant_if_needed(self, colname, check_positive=True):
        """Assign a constant column to the table if it does not already have one.

        Parameters
        ----------
        colname : str
            The name of the column to assign.
        check_positive : bool, optional
            If True, check that the value is positive before assigning it. Default is True.

        Returns
        -------
        bool
            True if the column was added or already exists. False otherwise.
        """
        if colname in self._table.columns:
            return True  # Already have a column.

        # Check that we have the value to add.
        if self.survey_values.get(colname) is None:
            return False
        value = self.survey_values[colname]

        # If the value is a single number, convert it to a dictionary with the same value for all bands.
        if isinstance(value, int | float):
            value = {fil: value for fil in self.filters}

        # Fill in the information for each filter.
        col_vals = np.zeros(len(self._table), dtype=float)
        for fil in self.filters:
            if fil not in value:
                raise ValueError(f"`{colname}` must include all the filters in the table. Missing '{fil}'.")
            if not isinstance(value[fil], int | float):
                raise ValueError(f"`{colname}` must map filter names to numeric values.")
            if check_positive and value[fil] <= 0:
                raise ValueError(f"`{colname}` values must be positive. Got {value[fil]} for filter {fil}.")
            mask = self._table["filter"] == fil
            col_vals[mask] = value[fil]
        self.add_column(colname, col_vals)

        return True

    def safe_get_survey_value(self, key):
        """Get a survey value by key, checking that it is not None.

        Parameters
        ----------
        key : str
            The key of the survey value to retrieve.
        """
        value = self.survey_values.get(key, None)
        if value is None:
            raise ValueError(
                f"Survey value for {key} is not defined. This should be set when creating the object."
            )
        return value

    @property
    def radius(self):
        """Return the radius if it exists."""
        return self.survey_values.get("radius", None)

    @radius.setter
    def radius(self, new_val):
        """Create a setter for radius."""
        if new_val <= 0:
            raise ValueError(f"Invalid radius: {new_val}")
        self.survey_values["radius"] = new_val

    @property
    def columns(self):
        """Get the column names."""
        return self._table.columns

    @classmethod
    def from_db(cls, filename, sql_query="SELECT * FROM observations", **kwargs):
        """Create an ObsTable object from the data in an db file. Reads data matching
        what is produced by write_db (and matching the RubinOpsim table).

        Parameters
        ----------
        filename : str
            The name of the db file.
        sql_query : str
            The SQL query to use when loading the table.
            Default: "SELECT * FROM observations"
        kwargs : dict, optional
            Additional keyword arguments to pass to the Survey constructor.

        Returns
        -------
        ObsTable
            A table with all of the pointing data.

        Raise
        -----
        FileNotFoundError if the file does not exist.
        ValueError if unable to load the table.
        """
        if not Path(filename).is_file():
            raise FileNotFoundError(f"db file {filename} not found.")
        con = sqlite3.connect(f"file:{filename}?mode=ro", uri=True)

        # Read the table.
        try:
            survey_data = pd.read_sql_query(sql_query, con)
        except Exception:
            raise ValueError("Database read failed.") from None

        # Close the connection.
        con.close()

        return cls(survey_data, **kwargs)

    @classmethod
    def from_parquet(cls, filename):
        """Create an ObsTable object from a parquet file.

        Parameters
        ----------
        filename : str
            The name of the parquet file to read.

        Returns
        -------
        ObsTable
            A table with all of the pointing data.
        """
        if not Path(filename).is_file():
            raise FileNotFoundError(f"File {filename} not found.")
        survey_data = pd.read_parquet(filename)
        return cls(survey_data)

    def build_moc(self, *, radius=None, max_depth=10):
        """Build a Multi-Order Coverage Map from the regions in the data set.

        Parameters
        ----------
        radius : float, optional
            The radius to use for each image (in degrees). If not provided, the default
            radius from the survey values will be used.
        max_depth : int, optional
            The maximum depth of the MOC. Default is 10.

        Returns
        -------
        MOC
            The Multi-Order Coverage Map constructed from the data set.
        """
        radius = radius if radius is not None else self.survey_values.get("radius", None)
        if radius is None:
            raise ValueError("Radius must be provided for MOC construction or as a default. Got None.")

        longitudes = Longitude(self._table["ra"].to_list(), unit="deg")
        latitudes = Latitude(self._table["dec"].to_list(), unit="deg")
        moc = MOC.from_cones(
            lon=longitudes,
            lat=latitudes,
            radius=radius * u.deg,
            max_depth=max_depth,
            delta_depth=0,
            union_strategy="large_cones",
        )
        return moc

    def _build_kd_tree(self):
        """Construct the KD-tree from the ObsTable."""
        ra_rad = np.radians(self._table["ra"].to_numpy())
        dec_rad = np.radians(self._table["dec"].to_numpy())
        # Convert the pointings to Cartesian coordinates on a unit sphere.
        x = np.cos(dec_rad) * np.cos(ra_rad)
        y = np.cos(dec_rad) * np.sin(ra_rad)
        z = np.sin(dec_rad)
        cart_coords = np.array([x, y, z]).T

        # Construct the kd-tree.
        self._kd_tree = KDTree(cart_coords)

    def _assign_zero_points(self):
        """Assign instrumental zero points in nJy to the data table.

        Default implementation does not produce a zeropoint column. Subclasses
        should override this method with a survey specific computation.
        """
        pass

    def add_column(self, colname, values, *, overwrite=False):
        """Add a column to the current data table.

        Parameters
        ----------
        colname : str
            The name of the new column.
        values : int, float, str, list, or numpy.ndarray
            The value(s) to add.
        overwrite : bool
            Overwrite the column is it already exists.
            Default: False
        """
        if colname in self._table.columns and not overwrite:
            raise KeyError(f"Column {colname} already exists.")

        # If the input is a scalar, turn it into an array of the correct length
        if np.isscalar(values):
            values = np.full((len(self._table)), values)
        self._table[colname] = values

    def write_db(self, filename, *, tablename="observations", overwrite=False):
        """Write out the observation table as a database to a given SQL table.

        Parameters
        ----------
        filename : str
            The name of the db file.
        tablename : str
            The table to which to write.
            Default: "observations"
        overwrite : bool
            Overwrite the existing DB file.
            Default: False

        Raise
        -----
        FileExistsError if the file already exists and overwrite is False.
        """
        if_exists = "replace" if overwrite else "fail"

        con = sqlite3.connect(filename)
        try:
            self._table.to_sql(tablename, con, if_exists=if_exists)
        except Exception:
            raise ValueError("Database write failed.") from None

        con.close()

    def write_parquet(self, filename, *, overwrite=False):
        """Write out the observation table as a parquet file.

        Parameters
        ----------
        filename : str
            The name of the parquet file.
        overwrite : bool
            Overwrite the existing parquet file.
            Default: False

        Raise
        -----
        FileExistsError if the file already exists and overwrite is False.
        """
        if not overwrite and Path(filename).is_file():
            raise FileExistsError(f"File {filename} already exists.")

        # Save all the survey data as metadata.
        self._table.attrs["lightcurvelynx_survey_data"] = self.survey_values
        self._table.to_parquet(filename)

    def time_bounds(self):
        """Returns the min and max times for all observations in the ObsTable.

        Returns
        -------
        t_min, t_max : float, float
            The min and max times for all observations in the ObsTable.
        """
        t_min = self._table["time"].min()
        t_max = self._table["time"].max()
        return t_min, t_max

    def filter_rows(self, rows):
        """Filter the rows in the ObsTable to only include those indices that are provided
        in a list of row indices (integers) or marked True in a mask.

        Parameters
        ----------
        rows : numpy.ndarray
            Either a Boolean array of the same length as the table or list of integer
            row indices to keep.

        Returns
        -------
        self : ObsTable
            The filtered ObsTable object.
        """
        # Check if we are dealing with a mask of a list of indices.
        rows = np.asarray(rows)
        if rows.dtype == bool:
            if len(rows) != len(self._table):
                raise ValueError(
                    f"Mask length mismatch. Expected {len(self._table)} rows, but found {len(rows)}."
                )
            mask = rows
        else:
            mask = np.full((len(self._table),), False)
            mask[rows] = True

        # Filter the rows in-place and build a new kd-tree.
        self._table = self._table[mask]
        self._kd_tree = None
        self._build_kd_tree()

        return self

    def is_observed(self, query_ra, query_dec, *, radius=None, t_min=None, t_max=None):
        """Check if the query point(s) fall within the field of view of any
        pointing in the ObsTable.

        Parameters
        ----------
        query_ra : float or numpy.ndarray
            The query right ascension (in degrees).
        query_dec : float or numpy.ndarray
            The query declination (in degrees).
        radius : float or None, optional
            The angular radius of the observation (in degrees).
        t_min : float or None, optional
            The minimum time (in MJD) for the observations to consider.
            If None, no time filtering is applied.
        t_max : float or None, optional
            The maximum time (in MJD) for the observations to consider.
            If None, no time filtering is applied.

        Returns
        -------
        seen : bool or list[bool]
            Depending on the input, this is either a single bool to indicate
            whether the query point is observed or a list of bools for an array
            of query points.
        """
        inds = self.range_search(query_ra, query_dec, radius=radius, t_min=t_min, t_max=t_max)
        if np.isscalar(query_ra):
            return len(inds) > 0
        return [len(entry) > 0 for entry in inds]

    def range_search(self, query_ra, query_dec, *, radius=None, t_min=None, t_max=None):
        """Return the indices of the pointings that fall within the field
        of view of the query point(s).

        Parameters
        ----------
        query_ra : float or numpy.ndarray
            The query right ascension (in degrees).
        query_dec : float or numpy.ndarray
            The query declination (in degrees).
        radius : float or None, optional
            The angular radius of the observation (in degrees). If None
            uses the default radius for the ObsTable.
        t_min : float, numpy.ndarray or None, optional
            The minimum time (in MJD) for the observations to consider.
            If None, no time filtering is applied.
        t_max : float, numpy.ndarray or None, optional
            The maximum time (in MJD) for the observations to consider.
            If None, no time filtering is applied.

        Returns
        -------
        inds : list[int] or list[numpy.ndarray]
            Depending on the input, this is either a list of indices for a single query point
            or a list of arrays (of indices) for an array of query points.
        """
        if query_ra is None or query_dec is None:
            raise ValueError("Query RA and dec must be provided for range search, but got None.")

        # Fallback to the preset radius if None is provided.
        radius = radius if radius is not None else self.survey_values.get("radius", None)
        if radius is None:
            raise ValueError("Radius must be provided for range search or as a default. Got None.")

        # If the points are scalars, make them into length 1 arrays.
        is_scalar = np.isscalar(query_ra) and np.isscalar(query_dec)
        query_ra = np.atleast_1d(query_ra)
        query_dec = np.atleast_1d(query_dec)

        # Confirm the query RA and Dec have the same length.
        if len(query_ra) != len(query_dec):
            raise ValueError("Query RA and Dec must have the same length.")
        if np.any(query_ra == None) or np.any(query_dec == None):  # noqa: E711
            raise ValueError("Query RA and dec cannot contain None.")

        # Transform the query point(s) to 3-d Cartesian coordinate(s).
        ra_rad = np.radians(query_ra)
        dec_rad = np.radians(query_dec)
        x = np.cos(dec_rad) * np.cos(ra_rad)
        y = np.cos(dec_rad) * np.sin(ra_rad)
        z = np.sin(dec_rad)
        cart_query = np.array([x, y, z]).T

        # Adjust the angular radius to a cartesian search radius and perform the search.
        adjusted_radius = 2.0 * np.sin(0.5 * np.radians(radius))
        inds = self._kd_tree.query_ball_point(cart_query, adjusted_radius)

        if t_min is not None or t_max is not None:
            num_queries = len(query_ra)
            times = self._table["time"].to_numpy()

            if t_min is None:
                t_min = np.full(num_queries, -np.inf)
            else:
                t_min = np.atleast_1d(t_min)
            if len(t_min) != num_queries:
                raise ValueError(f"t_min must be a scalar or an array of length {num_queries}.")

            if t_max is None:
                t_max = np.full(num_queries, np.inf)
            else:
                t_max = np.atleast_1d(t_max)
            if len(t_max) != num_queries:
                raise ValueError(f"t_max must be a scalar or an array of length {num_queries}.")

            # Run through each list of indices and filter by time. We need to do this
            # iteratively, because the lists can have different lengths.
            for idx, subinds in enumerate(inds):
                if len(subinds) == 0:
                    continue
                time_mask = (times[subinds] >= t_min[idx]) & (times[subinds] <= t_max[idx])
                inds[idx] = np.asarray(subinds)[time_mask]

        # Do a filtering step based on the detector's footprint. We do this after the range search,
        # because it is more expensive (but also more accurate).
        if self._detector_footprint is not None:
            # Extract the RA and dec of the pointings for later use.
            all_ra = self._table["ra"].to_numpy()
            all_dec = self._table["dec"].to_numpy()
            all_rot = None if "rotation" not in self._table.columns else self._table["rotation"].to_numpy()

            for idx, subinds in enumerate(inds):
                num_matches = len(subinds)
                if num_matches == 0:
                    continue  # Nothing to filter.

                match_rot = None if all_rot is None else all_rot[subinds]
                mask = self._detector_footprint.contains(
                    np.full(num_matches, query_ra[idx]),  # The RA coordinate of this query
                    np.full(num_matches, query_dec[idx]),  # The dec coordinate of this query
                    all_ra[subinds],  # The RA coordinates of the pointings (detector positions)
                    all_dec[subinds],  # The dec coordinates of the pointings (detector positions)
                    rotation=match_rot,  # The detector rotation angles (if available)
                )
                inds[idx] = np.asarray(subinds)[mask]

        # If the query was a scalar, we return a single list of indices.
        if is_scalar:
            inds = inds[0]
        return inds

    def get_observations(self, query_ra, query_dec, *, radius=None, t_min=None, t_max=None, cols=None):
        """Return the observation information when the query point falls within
        the field of view of a pointing in the ObsTable.

        Parameters
        ----------
        query_ra : float
            The query right ascension (in degrees).
        query_dec : float
            The query declination (in degrees).
        radius : float or None, optional
            The angular radius of the observation (in degrees). If None
            uses the default radius for the ObsTable.
        t_min : float or None, optional
            The minimum time (in MJD) for the observations to consider.
            If None, no time filtering is applied.
        t_max : float or None, optional
            The maximum time (in MJD) for the observations to consider.
            If None, no time filtering is applied.
        cols : list or str
            A list of the names of columns to extract or a single column name.
            If None returns all the columns.

        Returns
        -------
        results : dict
            A dictionary mapping the given column name to a numpy array of values.
        """
        neighbors = self.range_search(query_ra, query_dec, radius=radius, t_min=t_min, t_max=t_max)

        results = {}
        if cols is None:
            cols = self._table.columns.to_list()
        elif isinstance(cols, str):
            cols = [cols]

        for col in cols:
            # Allow the user to specify either the original or mapped column names,
            # by using the class accessor (__getitem__), instead of the table one.
            if col not in self:
                raise KeyError(f"Unrecognized column name {col}")
            results[col] = self[col][neighbors].to_numpy()
        return results

    def bandflux_error_point_source(self, bandflux, index):
        """Compute observational bandflux error for a point source.

        Parameters
        ----------
        bandflux : array_like of float
            Band bandflux of the point source in nJy.
        index : array_like of int
            The index of the observation in the ObsTable table.

        Returns
        -------
        flux_err : array_like of float
            Simulated bandflux noise in nJy.
        """
        raise NotImplementedError
