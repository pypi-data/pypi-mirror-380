"""Samplers used for generating (RA, dec) coordinates."""

from pathlib import Path

import numpy as np
from cdshealpix.nested import healpix_to_skycoord
from citation_compass import CiteClass
from mocpy import MOC

from lightcurvelynx.math_nodes.given_sampler import TableSampler
from lightcurvelynx.math_nodes.np_random import NumpyRandomFunc


class UniformRADEC(NumpyRandomFunc):
    """A FunctionNode that uniformly samples (RA, dec) over a sphere,

    Attributes
    ----------
    use_degrees : bool
        The default return unit. If True returns samples in degrees.
        Otherwise, if False, returns samples in radians.
    """

    def __init__(self, outputs=None, seed=None, use_degrees=True, **kwargs):
        self.use_degrees = use_degrees

        # Override key arguments. We create a uniform sampler function, but
        # won't need it because the subclass overloads compute().
        func_name = "uniform"
        outputs = ["ra", "dec"]
        super().__init__(func_name, outputs=outputs, seed=seed, **kwargs)

    def compute(self, graph_state, rng_info=None, **kwargs):
        """Return the given values.

        Parameters
        ----------
        graph_state : GraphState
            An object mapping graph parameters to their values. This object is modified
            in place as it is sampled.
        rng_info : numpy.random._generator.Generator, optional
            A given numpy random number generator to use for this computation. If not
            provided, the function uses the node's random number generator.
        **kwargs : dict, optional
            Additional function arguments.

        Returns
        -------
        results : any
            The result of the computation. This return value is provided so that testing
            functions can easily access the results.
        """
        rng = rng_info if rng_info is not None else self._rng

        # Generate the random (RA, dec) lists.
        ra = rng.uniform(0.0, 2.0 * np.pi, size=graph_state.num_samples)
        dec = np.arcsin(rng.uniform(-1.0, 1.0, size=graph_state.num_samples))
        if self.use_degrees:
            ra = np.degrees(ra)
            dec = np.degrees(dec)

        # If we are generating a single sample, return floats.
        if graph_state.num_samples == 1:
            ra = ra[0]
            dec = dec[0]

        # Set the outputs and return the results. This takes the place of
        # function node's _save_results() function because we know the outputs.
        graph_state.set(self.node_string, "ra", ra)
        graph_state.set(self.node_string, "dec", dec)
        return [ra, dec]


class ObsTableRADECSampler(TableSampler):
    """A FunctionNode that samples RA and dec (and time) from an ObsTable.
    RA and dec are returned in degrees.

    Note
    ----
    Does not currently use uniform sampling from the radius. Uses a very
    rough approximate as a proof of concept. Do not use for statistical analysis.

    Parameters
    ----------
    data : ObsTable
        The ObsTable object to use for sampling.
    radius : float
        The radius of the the field of view of the observations in degrees. Use 0.0 to just sample
        the centers of the images. Default: None
    in_order : bool
        Return the given data in order of the rows (True). If False, performs
        random sampling with replacement. Default: False
    """

    def __init__(self, data, radius=None, in_order=False, **kwargs):
        if radius is None:
            radius = data.survey_values.get("radius", None)
            if radius is None:
                raise ValueError("ObsTable has no radius. Must provide radius.")
        if radius < 0.0:
            raise ValueError("Invalid radius: {radius}")
        self.radius = radius

        data_dict = {
            "ra": data["ra"],
            "dec": data["dec"],
            "time": data["time"],
        }
        super().__init__(data_dict, in_order=in_order, **kwargs)

    def compute(self, graph_state, rng_info=None, **kwargs):
        """Return the given values.

        Parameters
        ----------
        graph_state : GraphState
            An object mapping graph parameters to their values. This object is modified
            in place as it is sampled.
        rng_info : numpy.random._generator.Generator, optional
            A given numpy random number generator to use for this computation. If not
            provided, the function uses the node's random number generator.
        **kwargs : dict, optional
            Additional function arguments.

        Returns
        -------
        results : any
            The result of the computation. This return value is provided so that testing
            functions can easily access the results.
        """
        # Sample the center RA, dec, and times without the radius.
        results = super().compute(graph_state, rng_info=rng_info, **kwargs)

        if self.radius > 0.0:
            # Add an offset around the center. This is currently a placeholder that does
            # NOT produce a uniform sampling. TODO: Make this uniform sampling.
            rng = rng_info if rng_info is not None else self._rng

            # Choose a uniform circle around the center point. Not that this is not uniform over
            # the final RA, dec because it does not account for compression in dec around the polls.
            offset_amt = self.radius * np.sqrt(rng.uniform(0.0, 1.0, size=graph_state.num_samples))
            offset_ang = 2.0 * np.pi * rng.uniform(0.0, 1.0, size=graph_state.num_samples)

            # Add the offsets to RA and dec. Keep time unchanged.
            results[0] += offset_amt * np.cos(offset_ang)  # RA
            results[1] += offset_amt * np.sin(offset_ang)  # dec

            # Resave the results (overwriting the previous results)
            self._save_results(results, graph_state)

        return results


class ObsTableUniformRADECSampler(NumpyRandomFunc):
    """A FunctionNode that samples RA and dec uniformly from the area covered
    by an ObsTable.  RA and dec are returned in degrees.

    Note
    ----
    This uses rejection sampling where it randomly guesses an (RA, dec) then checks if that
    point falls within the survey. If not, it repeats the process until it finds a valid point
    or reaches `max_iterations` iterations (then returns the last sample). This sampling method
    can be quite slow or even generate out-of-survey samples if the coverage is small.

    Attributes
    ----------
    data : ObsTable
        The ObsTable object to use for sampling.
    radius : float
        The radius of the field of view of the observations in degrees.
    max_iterations : int
        The maximum number of iterations to perform. Default: 1000

    Parameters
    ----------
    data : ObsTable
        The ObsTable object to use for sampling.
    radius : float, optional
        The search radius around the center of the pointing. If None, uses the
        value from the ObsTable.
    outputs : list of str, optional
        The list of output names. Default: ["ra", "dec"]
    seed : int, optional
        The random seed to use for the internal random number generator. Default: None
    max_iterations : int, optional
        The maximum number of iterations to perform. Default: 1000
    **kwargs : dict, optional
        Additional keyword arguments to pass to the parent class constructor.
    """

    def __init__(self, data, *, radius=None, outputs=None, seed=None, max_iterations=1000, **kwargs):
        if radius is None:
            radius = data.survey_values.get("radius", None)
            if radius is None:
                raise ValueError("ObsTable has no radius. Must provide radius.")
        if radius <= 0.0:
            raise ValueError(f"Invalid override_radius: {radius}")
        self.radius = radius

        if len(data) == 0:
            raise ValueError("ObsTable data cannot be empty.")
        self.data = data

        if max_iterations <= 0:
            raise ValueError("Invalid max_iterations: {max_iterations}")
        self.max_iterations = max_iterations

        # Override key arguments. We create a uniform sampler function, but
        # won't need it because the subclass overloads compute().
        func_name = "uniform"
        outputs = ["ra", "dec"]
        super().__init__(func_name, outputs=outputs, seed=seed, **kwargs)

    def compute(self, graph_state, rng_info=None, **kwargs):
        """Return the given values.

        Parameters
        ----------
        graph_state : GraphState
            An object mapping graph parameters to their values. This object is modified
            in place as it is sampled.
        rng_info : numpy.random._generator.Generator, optional
            A given numpy random number generator to use for this computation. If not
            provided, the function uses the node's random number generator.
        **kwargs : dict, optional
            Additional function arguments.

        Returns
        -------
        (ra, dec) : tuple of floats or np.ndarray
            If a single sample is generated, returns a tuple of floats. Otherwise,
            returns a tuple of np.ndarrays.
        """
        rng = rng_info if rng_info is not None else self._rng

        ra = np.zeros(graph_state.num_samples)
        dec = np.zeros(graph_state.num_samples)
        mask = np.full(graph_state.num_samples, False)
        num_missing = graph_state.num_samples

        # Rejection sampling to ensure the samples are within the ObsTable coverage.
        # This can take many iterations if the coverage is small.
        iter_num = 1
        while num_missing > 0 and iter_num <= self.max_iterations:
            # Generate new samples for the missing ones.
            ra[~mask] = np.degrees(rng.uniform(0.0, 2.0 * np.pi, size=num_missing))
            dec[~mask] = np.degrees(np.arcsin(rng.uniform(-1.0, 1.0, size=num_missing)))

            # Check if the samples are within the ObsTable coverage.
            mask = np.asarray(self.data.is_observed(ra, dec, radius=self.radius))
            num_missing = np.sum(~mask)
            iter_num += 1

        # If we are generating a single sample, return floats.
        if graph_state.num_samples == 1:
            ra = ra[0]
            dec = dec[0]

        # Set the outputs and return the results. This takes the place of
        # function node's _save_results() function because we know the outputs.
        graph_state.set(self.node_string, "ra", ra)
        graph_state.set(self.node_string, "dec", dec)
        return (ra, dec)


class ApproximateMOCSampler(NumpyRandomFunc, CiteClass):
    """A FunctionNode that samples RA and dec (approximately) from the coverage of
    a MOCPy Multi-Order Coverage Map object.

    References
    ----------
    * MOCPY: https://github.com/cds-astro/mocpy/
    * CDS Healpix: https://github.com/cds-astro/cds-healpix-python
    * MOC: Pierre Fernique, Thomas Boch, Tom Donaldson, Daniel Durand , Wil O'Mullane, Martin Reinecke,
    and Mark Taylor. MOC - HEALPix Multi-Order Coverage map Version 1.0. IVOA Recommendation 02 June 2014,
    pages 602, Jun 2014. doi:10.5479/ADS/bib/2014ivoa.spec.0602F.

    Attributes
    ----------
    healpix_list : list of int
        The list of healpix pixel IDs that cover the MOC at the given depth.
    depth : int
        The healpix depth to use as an approximation. Must be [2, 29].
    """

    def __init__(self, moc, *, outputs=None, seed=None, depth=12, **kwargs):
        if depth < 2 or depth > 29:
            raise ValueError("Depth must be [2, 29]. Received {depth}")
        self.depth = depth
        self.healpix_list = moc.to_order(depth).flatten()

        # Override key arguments. We create a uniform sampler function, but
        # won't need it because the subclass overloads compute().
        func_name = "uniform"
        outputs = ["ra", "dec"]
        super().__init__(func_name, outputs=outputs, seed=seed, **kwargs)

    @classmethod
    def from_file(cls, filename, format="fits", **kwargs):
        """Create an ApproximateMOCSampler from a MOC file.

        This file can be created from a mocpy.MOC object using its save() function.

        Parameters
        ----------
        filename : str or Path
            The path to the MOC file. Supported formats include FITS, JSON, and ASCII.
        format : str, optional
            The format of the MOC file. Supported formats include 'fits', 'json', and
            'ascii'. Default is 'fits'.
        **kwargs : dict, optional
            Additional keyword arguments to pass to the constructor.

        Returns
        -------
        ApproximateMOCSampler
            The created ApproximateMOCSampler object.
        """
        filename = Path(filename)
        if not filename.is_file():
            raise FileNotFoundError(f"MOC file not found: {filename}")

        moc = MOC.load(filename, format=format)
        return cls(moc, **kwargs)

    def compute(self, graph_state, rng_info=None, **kwargs):
        """Return the given values.

        Parameters
        ----------
        graph_state : GraphState
            An object mapping graph parameters to their values. This object is modified
            in place as it is sampled.
        rng_info : numpy.random._generator.Generator, optional
            A given numpy random number generator to use for this computation. If not
            provided, the function uses the node's random number generator.
        **kwargs : dict, optional
            Additional function arguments.

        Returns
        -------
        (ra, dec) : tuple of floats or np.ndarray
            If a single sample is generated, returns a tuple of floats. Otherwise,
            returns a tuple of np.ndarrays.
        """
        rng = rng_info if rng_info is not None else self._rng

        # Choose a starting pixel ID for each sample. Then randomly traverse
        # down the healpix tree by moving to one of the children pixels until
        # we reach level=29 (approximately 4.5 * 10^18 possible locations).
        pixel_ids = rng.choice(self.healpix_list, size=graph_state.num_samples).astype(np.uint64)
        start_pixel_ids29 = np.left_shift(pixel_ids, 2 * (29 - self.depth))
        offset_range = np.uint64(1) << np.uint64(2 * (29 - self.depth))
        pixel_ids29 = start_pixel_ids29 + rng.integers(
            offset_range, size=graph_state.num_samples, dtype=np.uint64
        )

        # Convert back the healpix centers to RA and dec.
        coords = healpix_to_skycoord(pixel_ids29, depth=29)
        ra = coords.ra.deg
        dec = coords.dec.deg

        # If we are generating a single sample, return floats.
        if graph_state.num_samples == 1:
            ra = ra[0]
            dec = dec[0]

        # Set the outputs and return the results. This takes the place of
        # function node's _save_results() function because we know the outputs.
        graph_state.set(self.node_string, "ra", ra)
        graph_state.set(self.node_string, "dec", dec)
        return (ra, dec)
