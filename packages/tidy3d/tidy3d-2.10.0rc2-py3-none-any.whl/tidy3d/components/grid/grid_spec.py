"""Defines classes specifying meshing in 1D and a collective class for 3D"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Literal, Optional, Union

import numpy as np
import pydantic.v1 as pd

from tidy3d.components.base import Tidy3dBaseModel, cached_property, skip_if_fields_missing
from tidy3d.components.geometry.base import Box, ClipOperation
from tidy3d.components.geometry.utils_2d import increment_float
from tidy3d.components.lumped_element import LumpedElementType
from tidy3d.components.source.utils import SourceType
from tidy3d.components.structure import MeshOverrideStructure, Structure, StructureType
from tidy3d.components.types import (
    TYPE_TAG_STR,
    ArrayFloat1D,
    ArrayFloat2D,
    Axis,
    Coordinate,
    CoordinateOptional,
    PriorityMode,
    Symmetry,
    Undefined,
    annotate_type,
)
from tidy3d.constants import C_0, MICROMETER, dp_eps, fp_eps, inf
from tidy3d.exceptions import SetupError
from tidy3d.log import log

from .corner_finder import CornerFinderSpec
from .grid import Coords, Coords1D, Grid
from .mesher import GradedMesher, MesherType

# Scaling factor applied to internally generated lower bound of grid size that is computed from
# estimated minimal grid size
MIN_STEP_BOUND_SCALE = 0.5

# Default refinement factor in GridRefinement when both dl and refinement_factor are not defined
DEFAULT_REFINEMENT_FACTOR = 2

# Tolerance for distinguishing pec/grid intersections
GAP_MESHING_TOL = 1e-3


class GridSpec1d(Tidy3dBaseModel, ABC):
    """Abstract base class, defines 1D grid generation specifications."""

    def make_coords(
        self,
        axis: Axis,
        structures: list[StructureType],
        symmetry: tuple[Symmetry, Symmetry, Symmetry],
        periodic: bool,
        wavelength: pd.PositiveFloat,
        num_pml_layers: tuple[pd.NonNegativeInt, pd.NonNegativeInt],
        snapping_points: tuple[CoordinateOptional, ...],
    ) -> Coords1D:
        """Generate 1D coords to be used as grid boundaries, based on simulation parameters.
        Symmetry, and PML layers will be treated here.

        Parameters
        ----------
        axis : Axis
            Axis of this direction.
        structures : List[StructureType]
            List of structures present in simulation, the first one being the simulation domain.
        symmetry : Tuple[Symmetry, Symmetry, Symmetry]
            Reflection symmetry across a plane bisecting the simulation domain
            normal to each of the three axes.
        periodic : bool
            Apply periodic boundary condition or not.
            Only relevant for autogrids.
        wavelength : float
            Free-space wavelength.
        num_pml_layers : Tuple[int, int]
            number of layers in the absorber + and - direction along one dimension.
        snapping_points : Tuple[CoordinateOptional, ...]
            A set of points that enforce grid boundaries to pass through them.

        Returns
        -------
        :class:`.Coords1D`:
            1D coords to be used as grid boundaries.
        """

        # Determine if one should apply periodic boundary condition.
        # This should only affect auto nonuniform mesh generation for now.
        is_periodic = periodic and symmetry[axis] == 0

        # generate boundaries
        bound_coords = self._make_coords_initial(
            axis=axis,
            structures=structures,
            wavelength=wavelength,
            symmetry=symmetry,
            is_periodic=is_periodic,
            snapping_points=snapping_points,
        )

        # incorporate symmetries
        if symmetry[axis] != 0:
            # Offset to center if symmetry present
            center = structures[0].geometry.center[axis]
            center_ind = np.argmin(np.abs(center - bound_coords))
            bound_coords += center - bound_coords[center_ind]
            bound_coords = bound_coords[bound_coords >= center]
            bound_coords = np.append(2 * center - bound_coords[:0:-1], bound_coords)

        # Add PML layers in using dl on edges
        bound_coords = self._add_pml_to_bounds(num_pml_layers, bound_coords)
        return bound_coords

    @abstractmethod
    def _make_coords_initial(
        self,
        axis: Axis,
        structures: list[StructureType],
        **kwargs,
    ) -> Coords1D:
        """Generate 1D coords to be used as grid boundaries, based on simulation parameters.
        Symmetry, PML etc. are not considered in this method.

        For auto nonuniform generation, it will take some more arguments.

        Parameters
        ----------
        structures : List[StructureType]
            List of structures present in simulation, the first one being the simulation domain.
        **kwargs
            Other arguments

        Returns
        -------
        :class:`.Coords1D`:
            1D coords to be used as grid boundaries.
        """

    @staticmethod
    def _add_pml_to_bounds(num_layers: tuple[int, int], bounds: Coords1D) -> Coords1D:
        """Append absorber layers to the beginning and end of the simulation bounds
        along one dimension.

        Parameters
        ----------
        num_layers : Tuple[int, int]
            number of layers in the absorber + and - direction along one dimension.
        bound_coords : np.ndarray
            coordinates specifying boundaries between cells along one dimension.

        Returns
        -------
        np.ndarray
            New bound coordinates along dimension taking abosrber into account.
        """
        if bounds.size < 2:
            return bounds

        first_step = bounds[1] - bounds[0]
        last_step = bounds[-1] - bounds[-2]
        add_left = bounds[0] - first_step * np.arange(num_layers[0], 0, -1)
        add_right = bounds[-1] + last_step * np.arange(1, num_layers[1] + 1)
        return np.concatenate((add_left, bounds, add_right))

    @staticmethod
    def _postprocess_unaligned_grid(
        axis: Axis,
        simulation_box: Box,
        machine_error_relaxation: bool,
        bound_coords: Coords1D,
    ) -> Coords1D:
        """Postprocess grids whose two ends  might be aligned with simulation boundaries.
        This is to be used in `_make_coords_initial`.

        Parameters
        ----------
        axis : Axis
            Axis of this direction.
        structures : List[StructureType]
            List of structures present in simulation, the first one being the simulation domain.
        machine_error_relaxation : bool
            When operations such as translation are applied to the 1d grids, fix the bounds
            were numerically within the simulation bounds but were still chopped off.
        bound_coords : Coord1D
            1D grids potentially unaligned with the simulation boundary

        Returns
        -------
        :class:`.Coords1D`:
            1D coords to be used as grid boundaries.

        """
        center, size = simulation_box.center[axis], simulation_box.size[axis]
        # chop off any coords outside of simulation bounds, beyond some buffer region
        # to take numerical effects into account
        bound_min = np.nextafter(center - size / 2, -inf, dtype=np.float32)
        bound_max = np.nextafter(center + size / 2, inf, dtype=np.float32)

        if bound_max < bound_coords[0] or bound_min > bound_coords[-1]:
            axis_name = "xyz"[axis]
            raise SetupError(
                f"Simulation domain does not overlap with the provided grid in '{axis_name}' direction."
            )

        if size == 0:
            # in case of zero-size dimension return the boundaries between which simulation falls
            ind = np.searchsorted(bound_coords, center, side="right")

            # in case when the center coincides with the right most boundary
            if ind >= len(bound_coords):
                ind = len(bound_coords) - 1

            return bound_coords[ind - 1 : ind + 1]

        bound_coords = bound_coords[bound_coords <= bound_max]
        bound_coords = bound_coords[bound_coords >= bound_min]

        # if not extending to simulation bounds, repeat beginning and end
        dl_min = bound_coords[1] - bound_coords[0]
        dl_max = bound_coords[-1] - bound_coords[-2]
        while bound_coords[0] - dl_min >= bound_min:
            bound_coords = np.insert(bound_coords, 0, bound_coords[0] - dl_min)
        while bound_coords[-1] + dl_max <= bound_max:
            bound_coords = np.append(bound_coords, bound_coords[-1] + dl_max)

        # in case operations are applied to coords, it's possible the bounds were numerically within
        # the simulation bounds but were still chopped off, which is fixed here
        if machine_error_relaxation:
            if np.isclose(bound_coords[0] - dl_min, bound_min):
                bound_coords = np.insert(bound_coords, 0, bound_coords[0] - dl_min)
            if np.isclose(bound_coords[-1] + dl_max, bound_max):
                bound_coords = np.append(bound_coords, bound_coords[-1] + dl_max)

        return bound_coords

    @abstractmethod
    def estimated_min_dl(
        self, wavelength: float, structure_list: list[Structure], sim_size: tuple[float, 3]
    ) -> float:
        """Estimated minimal grid size along the axis. The actual minimal grid size from mesher
        might be smaller.

        Parameters
        ----------
        wavelength : float
            Wavelength to use for the step size and for dispersive media epsilon.
        structure_list : List[Structure]
            List of structures present in the simulation.
        sim_size : Tuple[float, 3]
            Simulation domain size.

        Returns
        -------
        float
            Estimated minimal grid size from grid specification.
        """


class UniformGrid(GridSpec1d):
    """Uniform 1D grid. The most standard way to define a simulation is to use a constant grid size in each of the three directions.

    Example
    -------
    >>> grid_1d = UniformGrid(dl=0.1)

    See Also
    --------

    :class:`.QuasiUniformGrid`
        Specification for quasi-uniform grid along a given dimension.

    :class:`.AutoGrid`
        Specification for non-uniform grid along a given dimension.

    **Notebooks:**
        * `Photonic crystal waveguide polarization filter <../../notebooks/PhotonicCrystalWaveguidePolarizationFilter.html>`_
        * `Using automatic nonuniform meshing <../../notebooks/AutoGrid.html>`_
    """

    dl: pd.PositiveFloat = pd.Field(
        ...,
        title="Grid Size",
        description="Grid size for uniform grid generation.",
        units=MICROMETER,
    )

    @pd.validator("dl", always=True)
    def _validate_dl(cls, val):
        """
        Ensure 'dl' is not too small.
        """
        if val < 1e-7:
            raise SetupError(
                f"Uniform grid spacing 'dl' is {val} µm. "
                "Please check your units! For more info on Tidy3D units, see: "
                "https://docs.flexcompute.com/projects/tidy3d/en/latest/faq/docs/faq/What-are-the-units-used-in-the-simulation.html"
            )
        return val

    def _make_coords_initial(
        self,
        axis: Axis,
        structures: list[StructureType],
        **kwargs,
    ) -> Coords1D:
        """Uniform 1D coords to be used as grid boundaries.

        Parameters
        ----------
        axis : Axis
            Axis of this direction.
        structures : List[StructureType]
            List of structures present in simulation, the first one being the simulation domain.

        Returns
        -------
        :class:`.Coords1D`:
            1D coords to be used as grid boundaries.
        """

        center, size = structures[0].geometry.center[axis], structures[0].geometry.size[axis]

        # Take a number of steps commensurate with the size; make dl a bit smaller if needed
        num_cells = int(np.ceil(size / self.dl))

        # Make sure there's at least one cell
        num_cells = max(num_cells, 1)

        # Adjust step size to fit simulation size exactly
        dl_snapped = size / num_cells if size > 0 else self.dl

        return center - size / 2 + np.arange(num_cells + 1) * dl_snapped

    def estimated_min_dl(
        self, wavelength: float, structure_list: list[Structure], sim_size: tuple[float, 3]
    ) -> float:
        """Minimal grid size, which equals grid size here.

        Parameters
        ----------
        wavelength : float
            Wavelength to use for the step size and for dispersive media epsilon.
        structure_list : List[Structure]
            List of structures present in the simulation.
        sim_size : Tuple[float, 3]
            Simulation domain size.

        Returns
        -------
        float
            Minimal grid size from grid specification.
        """

        return self.dl


class CustomGridBoundaries(GridSpec1d):
    """Custom 1D grid supplied as a list of grid cell boundary coordinates.

    Example
    -------
    >>> grid_1d = CustomGridBoundaries(coords=[-0.2, 0.0, 0.2, 0.4, 0.5, 0.6, 0.7])
    """

    coords: Coords1D = pd.Field(
        ...,
        title="Grid Boundary Coordinates",
        description="An array of grid boundary coordinates.",
        units=MICROMETER,
    )

    def _make_coords_initial(
        self,
        axis: Axis,
        structures: list[StructureType],
        **kwargs,
    ) -> Coords1D:
        """Customized 1D coords to be used as grid boundaries.

        Parameters
        ----------
        axis : Axis
            Axis of this direction.
        structures : List[StructureType]
            List of structures present in simulation, the first one being the simulation domain.

        Returns
        -------
        :class:`.Coords1D`:
            1D coords to be used as grid boundaries.
        """

        return self._postprocess_unaligned_grid(
            axis=axis,
            simulation_box=structures[0].geometry,
            machine_error_relaxation=False,
            bound_coords=self.coords,
        )

    def estimated_min_dl(
        self, wavelength: float, structure_list: list[Structure], sim_size: tuple[float, 3]
    ) -> float:
        """Minimal grid size from grid specification.

        Parameters
        ----------
        wavelength : float
            Wavelength to use for the step size and for dispersive media epsilon.
        structure_list : List[Structure]
            List of structures present in the simulation.
        sim_size : Tuple[float, 3]
            Simulation domain size.

        Returns
        -------
        float
            Minimal grid size from grid specification.
        """

        return min(np.diff(self.coords))

    @pd.validator("coords", always=True)
    def _validate_coords(cls, val):
        """
        Ensure 'coords' is sorted and has at least 2 entries.
        """
        if len(val) < 2:
            raise SetupError("You must supply at least 2 entries for 'coords'.")
        # Ensure coords is sorted
        positive_diff = np.diff(val) > 0
        if not np.all(positive_diff):
            violations = np.where(np.diff(val) <= 0)[0] + 1
            raise SetupError(
                "'coords' must be strictly increasing (sorted in ascending order). "
                f"The entries at the following indices violated this requirement: {violations}."
            )
        return val


class CustomGrid(GridSpec1d):
    """Custom 1D grid supplied as a list of grid cell sizes centered on the simulation center.

    Example
    -------
    >>> grid_1d = CustomGrid(dl=[0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2])
    """

    dl: tuple[pd.PositiveFloat, ...] = pd.Field(
        ...,
        title="Customized grid sizes.",
        description="An array of custom nonuniform grid sizes. The resulting grid is centered on "
        "the simulation center such that it spans the region "
        "``(center - sum(dl)/2, center + sum(dl)/2)``, unless a ``custom_offset`` is given. "
        "Note: if supplied sizes do not cover the simulation size, the first and last sizes "
        "are repeated to cover the simulation domain.",
        units=MICROMETER,
    )

    custom_offset: float = pd.Field(
        None,
        title="Customized grid offset.",
        description="The starting coordinate of the grid which defines the simulation center. "
        "If ``None``, the simulation center is set such that it spans the region "
        "``(center - sum(dl)/2, center + sum(dl)/2)``.",
        units=MICROMETER,
    )

    def _make_coords_initial(
        self,
        axis: Axis,
        structures: list[StructureType],
        **kwargs,
    ) -> Coords1D:
        """Customized 1D coords to be used as grid boundaries.

        Parameters
        ----------
        axis : Axis
            Axis of this direction.
        structures : List[StructureType]
            List of structures present in simulation, the first one being the simulation domain.

        Returns
        -------
        :class:`.Coords1D`:
            1D coords to be used as grid boundaries.
        """

        center = structures[0].geometry.center[axis]

        # get bounding coordinates
        dl = np.array(self.dl)
        bound_coords = np.append(0.0, np.cumsum(dl))

        # place the middle of the bounds at the center of the simulation along dimension,
        # or use the `custom_offset` if provided
        if self.custom_offset is None:
            bound_coords += center - bound_coords[-1] / 2
        else:
            bound_coords += self.custom_offset

        return self._postprocess_unaligned_grid(
            axis=axis,
            simulation_box=structures[0].geometry,
            machine_error_relaxation=self.custom_offset is not None,
            bound_coords=bound_coords,
        )

    def estimated_min_dl(
        self, wavelength: float, structure_list: list[Structure], sim_size: tuple[float, 3]
    ) -> float:
        """Minimal grid size from grid specification.

        Parameters
        ----------
        wavelength : float
            Wavelength to use for the step size and for dispersive media epsilon.
        structure_list : List[Structure]
            List of structures present in the simulation.
        sim_size : Tuple[float, 3]
            Simulation domain size.

        Returns
        -------
        float
            Minimal grid size from grid specification.
        """
        return min(self.dl)


class AbstractAutoGrid(GridSpec1d):
    """Specification for non-uniform or quasi-uniform grid along a given dimension."""

    max_scale: float = pd.Field(
        1.4,
        title="Maximum Grid Size Scaling",
        description="Sets the maximum ratio between any two consecutive grid steps.",
        ge=1.2,
        lt=2.0,
    )

    mesher: MesherType = pd.Field(
        GradedMesher(),
        title="Grid Construction Tool",
        description="The type of mesher to use to generate the grid automatically.",
    )

    dl_min: pd.NonNegativeFloat = pd.Field(
        None,
        title="Lower Bound of Grid Size",
        description="Lower bound of the grid size along this dimension regardless of "
        "structures present in the simulation, including override structures "
        "with ``enforced=True``. It is a soft bound, meaning that the actual minimal "
        "grid size might be slightly smaller. If ``None`` or 0, a heuristic lower bound "
        "value will be applied.",
        units=MICROMETER,
    )

    @abstractmethod
    def _preprocessed_structures(self, structures: list[StructureType]) -> list[StructureType]:
        """Preprocess structure list before passing to ``mesher``."""

    @abstractmethod
    def _dl_collapsed_axis(self, wavelength: float, sim_size: tuple[float, 3]) -> float:
        """The grid step size if just a single grid along an axis in the simulation domain."""

    @property
    @abstractmethod
    def _dl_min(self) -> float:
        """Lower bound of grid size applied internally."""

    @property
    @abstractmethod
    def _min_steps_per_wvl(self) -> float:
        """Minimal steps per wavelength applied internally."""

    @abstractmethod
    def _dl_max(self, sim_size: tuple[float, 3]) -> float:
        """Upper bound of grid size applied internally."""

    @property
    def _undefined_dl_min(self) -> bool:
        """Whether `dl_min` has been specified or not."""
        return self.dl_min is None or self.dl_min == 0

    def _filtered_dl(self, dl: float, sim_size: tuple[float, 3]) -> float:
        """Grid step size after applying minimal and maximal filtering."""
        return max(min(dl, self._dl_max(sim_size)), self._dl_min)

    def _make_coords_initial(
        self,
        axis: Axis,
        structures: list[StructureType],
        wavelength: float,
        symmetry: Symmetry,
        is_periodic: bool,
        snapping_points: tuple[CoordinateOptional, ...],
    ) -> Coords1D:
        """Customized 1D coords to be used as grid boundaries.

        Parameters
        ----------
        axis : Axis
            Axis of this direction.
        structures : List[StructureType]
            List of structures present in simulation.
        wavelength : float
            Free-space wavelength.
        symmetry : Tuple[Symmetry, Symmetry, Symmetry]
            Reflection symmetry across a plane bisecting the simulation domain
            normal to each of the three axes.
        is_periodic : bool
            Apply periodic boundary condition or not.
        snapping_points : Tuple[CoordinateOptional, ...]
            A set of points that enforce grid boundaries to pass through them.

        Returns
        -------
        :class:`.Coords1D`:
            1D coords to be used as grid boundaries.
        """

        sim_cent = list(structures[0].geometry.center)
        sim_size = list(structures[0].geometry.size)

        # upper bound of grid step size based on total sim_size
        dl_max = self._dl_max(sim_size)

        for dim, sym in enumerate(symmetry):
            if sym != 0:
                sim_cent[dim] += sim_size[dim] / 4
                sim_size[dim] /= 2
        symmetry_domain = Box(center=sim_cent, size=sim_size)

        # New list of structures with symmetry applied
        struct_list = [Structure(geometry=symmetry_domain, medium=structures[0].medium)]
        rmin_domain, rmax_domain = symmetry_domain.bounds
        for structure in structures[1:]:
            if isinstance(structure, MeshOverrideStructure) and not structure.drop_outside_sim:
                # check overlapping per axis
                rmin, rmax = structure.geometry.bounds
                drop_structure = rmin[axis] > rmax_domain[axis] or rmin_domain[axis] > rmax[axis]
            else:
                # check overlapping of the entire structure
                drop_structure = not symmetry_domain.intersects(structure.geometry)
            if not drop_structure:
                struct_list.append(structure)

        # parse structures
        interval_coords, max_dl_list = self.mesher.parse_structures(
            axis,
            self._preprocessed_structures(struct_list),
            wavelength,
            self._min_steps_per_wvl,
            self._dl_min,
            dl_max,
        )
        # insert snapping_points
        interval_coords, max_dl_list = self.mesher.insert_snapping_points(
            self._dl_min, axis, interval_coords, max_dl_list, snapping_points
        )

        # Put just a single pixel if 2D-like simulation
        if interval_coords.size == 1:
            dl = self._dl_collapsed_axis(wavelength, sim_size)
            return np.array([sim_cent[axis] - dl / 2, sim_cent[axis] + dl / 2])

        # generate mesh steps
        interval_coords = np.array(interval_coords).flatten()
        max_dl_list = np.array(max_dl_list).flatten()
        len_interval_list = interval_coords[1:] - interval_coords[:-1]
        dl_list = self.mesher.make_grid_multiple_intervals(
            max_dl_list, len_interval_list, self.max_scale, is_periodic
        )

        # generate boundaries
        bound_coords = np.append(0.0, np.cumsum(np.concatenate(dl_list)))
        bound_coords += interval_coords[0]

        # fix simulation domain boundaries which may be slightly off
        domain_bounds = [bound[axis] for bound in symmetry_domain.bounds]
        if not np.all(np.isclose(bound_coords[[0, -1]], domain_bounds)):
            raise SetupError(
                f"AutoGrid coordinates along axis {axis} do not match the simulation "
                "domain, indicating an unexpected error in the meshing. Please create a github "
                "issue so that the problem can be investigated. In the meantime, switch to "
                f"uniform or custom grid along {axis}."
            )
        bound_coords[[0, -1]] = domain_bounds

        return np.array(bound_coords)


class QuasiUniformGrid(AbstractAutoGrid):
    """Similar to :class:`.UniformGrid` that generates uniform 1D grid, but grid positions
    are locally fine tuned to be snaped to snapping points and the edges of structure bounding boxes.
    Internally, it is using the same meshing method as :class:`.AutoGrid`, but it ignores material information in
    favor for a user-defined grid size.

    Example
    -------
    >>> grid_1d = QuasiUniformGrid(dl=0.1)

    See Also
    --------

    :class:`.UniformGrid`
        Uniform 1D grid.

    :class:`.AutoGrid`
        Specification for non-uniform grid along a given dimension.

    **Notebooks:**
        * `Using automatic nonuniform meshing <../../notebooks/AutoGrid.html>`_
    """

    dl: pd.PositiveFloat = pd.Field(
        ...,
        title="Grid Size",
        description="Grid size for quasi-uniform grid generation. Grid size at some locations can be "
        "slightly smaller.",
        units=MICROMETER,
    )

    def _preprocessed_structures(self, structures: list[StructureType]) -> list[StructureType]:
        """Processing structure list before passing to ``mesher``. Adjust all structures to drop their
        material properties so that they all have step size ``dl``.
        """
        processed_structures = []
        for structure in structures:
            dl = [self.dl, self.dl, self.dl]
            # skip override structures containing dl = None along axes
            if isinstance(structure, MeshOverrideStructure):
                for ind, dl_axis in enumerate(structure.dl):
                    if dl_axis is None:
                        dl[ind] = None
            processed_structures.append(MeshOverrideStructure(geometry=structure.geometry, dl=dl))
        return processed_structures

    @property
    def _dl_min(self) -> float:
        """Lower bound of grid size."""
        if self._undefined_dl_min:
            return 0.5 * self.dl
        return self.dl_min

    @property
    def _min_steps_per_wvl(self) -> float:
        """Minimal steps per wavelength."""
        # irrelevant in this class, just supply an arbitrary number
        return 1

    def _dl_max(self, sim_size: tuple[float, 3]) -> float:
        """Upper bound of grid size."""
        return self.dl

    def _dl_collapsed_axis(self, wavelength: float, sim_size: tuple[float, 3]) -> float:
        """The grid step size if just a single grid along an axis."""
        return self._filtered_dl(self.dl, sim_size)

    def estimated_min_dl(
        self, wavelength: float, structure_list: list[Structure], sim_size: tuple[float, 3]
    ) -> float:
        """Estimated minimal grid size, which equals grid size here.

        Parameters
        ----------
        wavelength : float
            Wavelength to use for the step size and for dispersive media epsilon.
        structure_list : List[Structure]
            List of structures present in the simulation.
        sim_size : Tuple[float, 3]
            Simulation domain size.

        Returns
        -------
        float
            Minimal grid size from grid specification.
        """

        return self.dl


class AutoGrid(AbstractAutoGrid):
    """Specification for non-uniform grid along a given dimension.

    Example
    -------
    >>> grid_1d = AutoGrid(min_steps_per_wvl=16, max_scale=1.4)

    See Also
    --------

    :class:`.UniformGrid`
        Uniform 1D grid.

    :class:`.GridSpec`
        Collective grid specification for all three dimensions.

    **Notebooks:**
        * `Using automatic nonuniform meshing <../../notebooks/AutoGrid.html>`_

    **Lectures:**
        *  `Time step size and CFL condition in FDTD <https://www.flexcompute.com/fdtd101/Lecture-7-Time-step-size-and-CFL-condition-in-FDTD/>`_
        *  `Numerical dispersion in FDTD <https://www.flexcompute.com/fdtd101/Lecture-8-Numerical-dispersion-in-FDTD/>`_
    """

    min_steps_per_wvl: float = pd.Field(
        10.0,
        title="Minimal Number of Steps Per Wavelength",
        description="Minimal number of steps per wavelength in each medium.",
        ge=6.0,
    )

    min_steps_per_sim_size: float = pd.Field(
        10.0,
        title="Minimal Number of Steps Per Simulation Domain Size",
        description="Minimal number of steps per longest edge length of simulation domain "
        "bounding box. This is useful when the simulation domain size is subwavelength.",
        ge=1.0,
    )

    def _dl_max(self, sim_size: tuple[float, 3]) -> float:
        """Upper bound of grid size, constrained by `min_steps_per_sim_size`."""
        return max(sim_size) / self.min_steps_per_sim_size

    @property
    def _dl_min(self) -> float:
        """Lower bound of grid size."""
        # set dl_min = 0 if unset, to be handled by mesher
        if self._undefined_dl_min:
            return 0
        return self.dl_min

    @property
    def _min_steps_per_wvl(self) -> float:
        """Minimal steps per wavelength."""
        return self.min_steps_per_wvl

    def _preprocessed_structures(self, structures: list[StructureType]) -> list[StructureType]:
        """Processing structure list before passing to ``mesher``."""
        return structures

    def _dl_collapsed_axis(self, wavelength: float, sim_size: tuple[float, 3]) -> float:
        """The grid step size if just a single grid along an axis."""
        return self._vacuum_dl(wavelength, sim_size)

    def _vacuum_dl(self, wavelength: float, sim_size: tuple[float, 3]) -> float:
        """Grid step size when computed in vacuum region."""
        return self._filtered_dl(wavelength / self.min_steps_per_wvl, sim_size)

    def estimated_min_dl(
        self, wavelength: float, structure_list: list[Structure], sim_size: tuple[float, 3]
    ) -> float:
        """Estimated minimal grid size along the axis. The actual minimal grid size from mesher
        might be smaller.

        Parameters
        ----------
        wavelength : float
            Wavelength to use for the step size and for dispersive media epsilon.
        structure_list : List[Structure]
            List of structures present in the simulation.
        sim_size : Tuple[float, 3]
            Simulation domain size.

        Returns
        -------
        float
            Estimated minimal grid size from grid specification.
        """

        min_dl = inf
        for structure in structure_list:
            min_dl = min(
                min_dl, self.mesher.structure_step(structure, wavelength, self.min_steps_per_wvl)
            )
        return self._filtered_dl(min_dl, sim_size)


GridType = Union[UniformGrid, CustomGrid, AutoGrid, CustomGridBoundaries, QuasiUniformGrid]


class GridRefinement(Tidy3dBaseModel):
    """Specification for local mesh refinement that defines the grid step size and the number of grid
    cells in the refinement region.

    Note
    ----

    If both `refinement_factor` and `dl` are defined, the grid step size is upper bounded by the smaller value of the two.
    If neither is defined, default `refinement_factor=2` is applied.


    Example
    -------
    >>> grid_refine = GridRefinement(refinement_factor = 2, num_cells = 7)

    """

    refinement_factor: Optional[pd.PositiveFloat] = pd.Field(
        None,
        title="Mesh Refinement Factor",
        description="Refine grid step size in vacuum by this factor.",
    )

    dl: Optional[pd.PositiveFloat] = pd.Field(
        None,
        title="Grid Size",
        description="Grid step size in the refined region.",
        units=MICROMETER,
    )

    num_cells: pd.PositiveInt = pd.Field(
        3,
        title="Number of Refined Grid Cells",
        description="Number of grid cells in the refinement region.",
    )

    @property
    def _refinement_factor(self) -> pd.PositiveFloat:
        """Refinement factor applied internally."""
        if self.refinement_factor is None and self.dl is None:
            return DEFAULT_REFINEMENT_FACTOR
        return self.refinement_factor

    def _grid_size(self, grid_size_in_vacuum: float) -> float:
        """Grid step size in the refinement region.

        Parameters
        ----------
        grid_size_in_vaccum : float
            Grid step size in vaccum.

        Returns
        -------
        float
            Grid step size in the refinement region.
        """

        dl = inf
        if self._refinement_factor is not None:
            dl = min(dl, grid_size_in_vacuum / self._refinement_factor)
        if self.dl is not None:
            dl = min(dl, self.dl)
        return dl

    def override_structure(
        self, center: CoordinateOptional, grid_size_in_vacuum: float, drop_outside_sim: bool
    ) -> MeshOverrideStructure:
        """Generate override structure for mesh refinement.

        Parameters
        ----------
        center : CoordinateOptional
            Center of the override structure. `None` coordinate along an axis means refinement is not
            applied along that axis.
        grid_size_in_vaccum : float
            Grid step size in vaccum.
        drop_outside_sim : bool
            Drop override structures outside simulation domain.

        Returns
        -------
        MeshOverrideStructure
            Unshadowed override structures for mesh refinement. If refinement doesn't need to be applied to an axis,
            the override geometry has size=inf and dl=None along this axis.
        """

        dl = self._grid_size(grid_size_in_vacuum)
        # override step size list
        dl_list = [None if axis_c is None else dl for axis_c in center]
        # override structure
        center_geo = [0 if axis_c is None else axis_c for axis_c in center]
        size_geo = [inf if axis_c is None else dl * self.num_cells for axis_c in center]
        return MeshOverrideStructure(
            geometry=Box(center=center_geo, size=size_geo),
            dl=dl_list,
            shadow=False,
            drop_outside_sim=drop_outside_sim,
            priority=-1,
        )


class LayerRefinementSpec(Box):
    """Specification for automatic mesh refinement and snapping in layered structures. Structure corners
    on the cross section perpendicular to layer thickness direction can be automatically identified. Subsequently,
    mesh is snapped and refined around the corners. Mesh can also be refined and snapped around the bounds along
    the layer thickness direction.

    Note
    ----

    Corner detection is performed on a 2D plane sitting in the middle of the layer. If the layer is finite
    along inplane axes, corners outside the bounds are discarded.

    Note
    ----

    This class only takes effect when :class:`.AutoGrid` is applied.

    Example
    -------
    >>> layer_spec = LayerRefinementSpec(axis=2, center=(0,0,0), size=(2, 3, 1))

    """

    axis: Axis = pd.Field(
        ...,
        title="Axis",
        description="Specifies dimension of the layer normal axis (0,1,2) -> (x,y,z).",
    )

    min_steps_along_axis: Optional[pd.PositiveFloat] = pd.Field(
        None,
        title="Minimal Number Of Steps Along Axis",
        description="If not ``None`` and the thickness of the layer is nonzero, set minimal "
        "number of steps discretizing the layer thickness.",
    )

    bounds_refinement: Optional[GridRefinement] = pd.Field(
        None,
        title="Mesh Refinement Factor Around Layer Bounds",
        description="If not ``None``, refine mesh around minimum and maximum positions "
        "of the layer along normal axis dimension. If `min_steps_along_axis` is also specified, "
        "refinement here is only applied if it sets a smaller grid size.",
    )

    bounds_snapping: Optional[Literal["bounds", "lower", "upper", "center"]] = pd.Field(
        "lower",
        title="Placing Grid Snapping Point Along Axis",
        description="If not ``None``, enforcing grid boundaries to pass through ``lower``, "
        "``center``, or ``upper`` position of the layer; or both ``lower`` and ``upper`` with ``bounds``.",
    )

    corner_finder: Optional[CornerFinderSpec] = pd.Field(
        CornerFinderSpec(),
        title="Inplane Corner Detection Specification",
        description="Specification for inplane corner detection. Inplane mesh refinement "
        "is based on the coordinates of those corners.",
    )

    corner_snapping: bool = pd.Field(
        True,
        title="Placing Grid Snapping Point At Corners",
        description="If ``True`` and ``corner_finder`` is not ``None``, enforcing inplane "
        "grid boundaries to pass through corners of geometries specified by ``corner_finder``.",
    )

    corner_refinement: Optional[GridRefinement] = pd.Field(
        GridRefinement(),
        title="Inplane Mesh Refinement Factor Around Corners",
        description="If not ``None`` and ``corner_finder`` is not ``None``, refine mesh around "
        "corners of geometries specified by ``corner_finder``. ",
    )

    refinement_inside_sim_only: bool = pd.Field(
        True,
        title="Apply Refinement Only To Features Inside Simulation Domain",
        description="If ``True``, only apply mesh refinement to features such as corners inside "
        "the simulation domain; If ``False``, features outside the domain can take effect "
        "along the dimensions where the projection of the feature "
        "and the projection of the simulation domain overlaps.",
    )

    gap_meshing_iters: pd.NonNegativeInt = pd.Field(
        1,
        title="Gap Meshing Iterations",
        description="Number of recursive iterations for resolving thin gaps. "
        "The underlying algorithm detects gaps contained in a single cell and places a snapping plane at the gaps's centers.",
    )

    dl_min_from_gap_width: bool = pd.Field(
        True,
        title="Set ``dl_min`` from Estimated Gap Width",
        description="Take into account autodetected minimal PEC gap width when determining ``dl_min``. "
        "This only applies if ``dl_min`` in ``AutoGrid`` specification is not set.",
    )

    interior_disjoint_geometries: bool = pd.Field(
        True,
        title="Geometries Are Interior-Disjoint",
        description="If ``True``, geometries made of different materials on the plane must not be overlapping. "
        "This can speed up the performance "
        "of corner finder when there are many structures crossing the plane.",
    )

    @pd.validator("axis", always=True)
    @skip_if_fields_missing(["size"])
    def _finite_size_along_axis(cls, val, values):
        """size must be finite along axis."""
        if np.isinf(values["size"][val]):
            raise SetupError("'size' must take finite values along 'axis' dimension.")
        return val

    @classmethod
    def from_layer_bounds(
        cls,
        axis: Axis,
        bounds: tuple[float, float],
        min_steps_along_axis: np.PositiveFloat = None,
        bounds_refinement: GridRefinement = None,
        bounds_snapping: Literal["bounds", "lower", "upper", "center"] = "lower",
        corner_finder: Union[CornerFinderSpec, None, object] = Undefined,
        corner_snapping: bool = True,
        corner_refinement: Union[GridRefinement, None, object] = Undefined,
        refinement_inside_sim_only: bool = True,
        gap_meshing_iters: pd.NonNegativeInt = 1,
        dl_min_from_gap_width: bool = True,
        **kwargs,
    ):
        """Constructs a :class:`LayerRefinementSpec` that is unbounded in inplane dimensions from bounds along
        layer thickness dimension.

        Parameters
        ----------
        axis : Axis
            Specifies dimension of the layer normal axis (0,1,2) -> (x,y,z).
        bounds : Tuple[float, float]
            Minimum and maximum positions of the layer along axis dimension.
        min_steps_along_axis : np.PositiveFloat = None
            Minimal number of steps along axis.
        bounds_refinement : GridRefinement = None
            Mesh refinement factor around layer bounds.
        bounds_snapping : Literal["bounds", "lower", "upper", "center"] = "lower"
            Placing grid snapping point along axis:  ``lower``, ``center``, or ``upper``
            position of the layer; or both ``lower`` and ``upper`` with ``bounds``.
        corner_finder : CornerFinderSpec = CornerFinderSpec()
            Inplane corner detection specification.
        corner_snapping : bool = True
            Placing grid snapping point at corners.
        corner_refinement : GridRefinement = GridRefinement()
            Inplane mesh refinement factor around corners.
        refinement_inside_sim_only : bool = True
            Apply refinement only to features inside simulation domain.
        gap_meshing_iters : bool = True
            Number of recursive iterations for resolving thin gaps.
        dl_min_from_gap_width : bool = True
            Take into account autodetected minimal PEC gap width when determining ``dl_min``.


        Example
        -------
        >>> layer = LayerRefinementSpec.from_layer_bounds(axis=2, bounds=(0,1))

        """
        if corner_finder is Undefined:
            corner_finder = CornerFinderSpec()
        if corner_refinement is Undefined:
            corner_refinement = GridRefinement()

        center = Box.unpop_axis((bounds[0] + bounds[1]) / 2, (0, 0), axis)
        size = Box.unpop_axis((bounds[1] - bounds[0]), (inf, inf), axis)

        return cls(
            axis=axis,
            center=center,
            size=size,
            min_steps_along_axis=min_steps_along_axis,
            bounds_refinement=bounds_refinement,
            bounds_snapping=bounds_snapping,
            corner_finder=corner_finder,
            corner_snapping=corner_snapping,
            corner_refinement=corner_refinement,
            refinement_inside_sim_only=refinement_inside_sim_only,
            gap_meshing_iters=gap_meshing_iters,
            dl_min_from_gap_width=dl_min_from_gap_width,
            **kwargs,
        )

    @classmethod
    def from_bounds(
        cls,
        rmin: Coordinate,
        rmax: Coordinate,
        axis: Axis = None,
        min_steps_along_axis: np.PositiveFloat = None,
        bounds_refinement: GridRefinement = None,
        bounds_snapping: Literal["bounds", "lower", "upper", "center"] = "lower",
        corner_finder: CornerFinderSpec = Undefined,
        corner_snapping: bool = True,
        corner_refinement: GridRefinement = Undefined,
        refinement_inside_sim_only: bool = True,
        gap_meshing_iters: pd.NonNegativeInt = 1,
        dl_min_from_gap_width: bool = True,
        **kwargs,
    ):
        """Constructs a :class:`LayerRefinementSpec` from minimum and maximum coordinate bounds.

        Parameters
        ----------
        rmin : Tuple[float, float, float]
            (x, y, z) coordinate of the minimum values.
        rmax : Tuple[float, float, float]
            (x, y, z) coordinate of the maximum values.
        axis : Axis
            Specifies dimension of the layer normal axis (0,1,2) -> (x,y,z). If ``None``, apply the dimension
            along which the layer thas smallest thickness.
        min_steps_along_axis : np.PositiveFloat = None
            Minimal number of steps along axis.
        bounds_refinement : GridRefinement = None
            Mesh refinement factor around layer bounds.
        bounds_snapping : Literal["bounds", "lower", "upper", "center"] = "lower"
            Placing grid snapping point along axis:  ``lower``, ``center``, or ``upper``
            position of the layer; or both ``lower`` and ``upper`` with ``bounds``.
        corner_finder : CornerFinderSpec = CornerFinderSpec()
            Inplane corner detection specification.
        corner_snapping : bool = True
            Placing grid snapping point at corners.
        corner_refinement : GridRefinement = GridRefinement()
            Inplane mesh refinement factor around corners.
        refinement_inside_sim_only : bool = True
            Apply refinement only to features inside simulation domain.
        gap_meshing_iters : bool = True
            Number of recursive iterations for resolving thin gaps.
        dl_min_from_gap_width : bool = True
            Take into account autodetected minimal PEC gap width when determining ``dl_min``.


        Example
        -------
        >>> layer = LayerRefinementSpec.from_bounds(axis=2, rmin=(0,0,0), rmax=(1,1,1))

        """
        if corner_finder is Undefined:
            corner_finder = CornerFinderSpec()
        if corner_refinement is Undefined:
            corner_refinement = GridRefinement()

        box = Box.from_bounds(rmin=rmin, rmax=rmax)
        if axis is None:
            axis = np.argmin(box.size)
        return cls(
            axis=axis,
            center=box.center,
            size=box.size,
            min_steps_along_axis=min_steps_along_axis,
            bounds_refinement=bounds_refinement,
            bounds_snapping=bounds_snapping,
            corner_finder=corner_finder,
            corner_snapping=corner_snapping,
            corner_refinement=corner_refinement,
            refinement_inside_sim_only=refinement_inside_sim_only,
            gap_meshing_iters=gap_meshing_iters,
            dl_min_from_gap_width=dl_min_from_gap_width,
            **kwargs,
        )

    @classmethod
    def from_structures(
        cls,
        structures: list[Structure],
        axis: Axis = None,
        min_steps_along_axis: np.PositiveFloat = None,
        bounds_refinement: GridRefinement = None,
        bounds_snapping: Literal["bounds", "lower", "upper", "center"] = "lower",
        corner_finder: CornerFinderSpec = Undefined,
        corner_snapping: bool = True,
        corner_refinement: GridRefinement = Undefined,
        refinement_inside_sim_only: bool = True,
        gap_meshing_iters: pd.NonNegativeInt = 1,
        dl_min_from_gap_width: bool = True,
        **kwargs,
    ):
        """Constructs a :class:`LayerRefinementSpec` from the bounding box of a list of structures.

        Parameters
        ----------
        structures : List[Structure]
            A list of structures whose overall bounding box is used to define mesh refinement
        axis : Axis
            Specifies dimension of the layer normal axis (0,1,2) -> (x,y,z). If ``None``, apply the dimension
            along which the bounding box of the structures thas smallest thickness.
        min_steps_along_axis : np.PositiveFloat = None
            Minimal number of steps along axis.
        bounds_refinement : GridRefinement = None
            Mesh refinement factor around layer bounds.
        bounds_snapping : Literal["bounds", "lower", "upper", "center"] = "lower"
            Placing grid snapping point along axis:  ``lower``, ``center``, or ``upper``
            position of the layer; or both ``lower`` and ``upper`` with ``bounds``.
        corner_finder : CornerFinderSpec = CornerFinderSpec()
            Inplane corner detection specification.
        corner_snapping : bool = True
            Placing grid snapping point at corners.
        corner_refinement : GridRefinement = GridRefinement()
            Inplane mesh refinement factor around corners.
        refinement_inside_sim_only : bool = True
            Apply refinement only to features inside simulation domain.
        gap_meshing_iters : bool = True
            Number of recursive iterations for resolving thin gaps.
        dl_min_from_gap_width : bool = True
            Take into account autodetected minimal PEC gap width when determining ``dl_min``.

        """
        if corner_finder is Undefined:
            corner_finder = CornerFinderSpec()
        if corner_refinement is Undefined:
            corner_refinement = GridRefinement()

        all_bounds = tuple(structure.geometry.bounds for structure in structures)
        rmin = tuple(min(b[i] for b, _ in all_bounds) for i in range(3))
        rmax = tuple(max(b[i] for _, b in all_bounds) for i in range(3))
        box = Box.from_bounds(rmin=rmin, rmax=rmax)
        if axis is None:
            axis = np.argmin(box.size)

        return cls(
            axis=axis,
            center=box.center,
            size=box.size,
            min_steps_along_axis=min_steps_along_axis,
            bounds_refinement=bounds_refinement,
            bounds_snapping=bounds_snapping,
            corner_finder=corner_finder,
            corner_snapping=corner_snapping,
            corner_refinement=corner_refinement,
            refinement_inside_sim_only=refinement_inside_sim_only,
            gap_meshing_iters=gap_meshing_iters,
            dl_min_from_gap_width=dl_min_from_gap_width,
            **kwargs,
        )

    @cached_property
    def length_axis(self) -> float:
        """Gets the thickness of the layer."""
        return self.size[self.axis]

    @cached_property
    def center_axis(self) -> float:
        """Gets the position of the center of the layer along the layer dimension."""
        return self.center[self.axis]

    @cached_property
    def _is_inplane_bounded(self) -> bool:
        """Whether the layer is bounded in at least one of the inplane dimensions."""
        return np.isfinite(self.size[(self.axis + 1) % 3]) or np.isfinite(
            self.size[(self.axis + 2) % 3]
        )

    @cached_property
    def _slightly_enlarged_box(self) -> Box:
        """Slightly enlarged box for robust point containment querying."""
        # increase size slightly
        size = [increment_float(orig_length, 1) for orig_length in self.size]
        return Box(center=self.center, size=size)

    def _unpop_axis(self, ax_coord: float, plane_coord: Any) -> CoordinateOptional:
        """Combine coordinate along axis with identical coordinates on the plane tangential to the axis.

        Parameters
        ----------
        ax_coord : float
            Value self.axis direction.
        plane_coord : Any
            Values along planar directions that are identical.

        Returns
        -------
        CoordinateOptional
            The three values in the xyz coordinate system.
        """
        return self.unpop_axis(ax_coord, [plane_coord, plane_coord], self.axis)

    def suggested_dl_min(self, grid_size_in_vacuum: float, structures: list[Structure]) -> float:
        """Suggested lower bound of grid step size for this layer.

        Parameters
        ----------
        grid_size_in_vaccum : float
            Grid step size in vaccum.

        Returns
        -------
        float
            Suggested lower bound of grid size to resolve most snapping points and
            mesh refinement structures.
        """
        dl_min = inf

        # axis dimension
        if self.length_axis > 0:
            # bounds snapping
            if self.bounds_snapping == "bounds":
                dl_min = min(dl_min, self.length_axis)
            # from min_steps along bounds
            if self.min_steps_along_axis is not None:
                dl_min = min(dl_min, self.length_axis / self.min_steps_along_axis)
            # refinement
            if self.bounds_refinement is not None:
                dl_min = min(dl_min, self.bounds_refinement._grid_size(grid_size_in_vacuum))

        # inplane dimension
        if self.corner_finder is not None and self.corner_refinement is not None:
            dl_min = min(dl_min, self.corner_refinement._grid_size(grid_size_in_vacuum))

        # min feature size
        if self.corner_finder is not None and not self.corner_finder._no_min_dl_override:
            dl_suggested = self._dl_min_from_smallest_feature(structures)
            dl_min = min(dl_min, dl_suggested)

        return dl_min

    def generate_snapping_points(
        self, structure_list: list[Structure], cached_corners_and_convexity=None
    ) -> list[CoordinateOptional]:
        """generate snapping points for mesh refinement."""
        snapping_points = self._snapping_points_along_axis
        if self.corner_snapping:
            snapping_points += self._corners(structure_list, cached_corners_and_convexity)
        return snapping_points

    def generate_override_structures(
        self,
        grid_size_in_vacuum: float,
        structure_list: list[Structure],
        cached_corners_and_convexity=None,
    ) -> list[MeshOverrideStructure]:
        """Generate mesh override structures for mesh refinement."""
        return self._override_structures_along_axis(
            grid_size_in_vacuum
        ) + self._override_structures_inplane(
            structure_list, grid_size_in_vacuum, cached_corners_and_convexity
        )

    def _inplane_inside(self, point: ArrayFloat2D) -> bool:
        """On the inplane cross section, whether the point is inside the layer.

        Parameters
        ----------
        point : ArrayFloat2D
            Point position on inplane plane.

        Returns
        -------
        bool
            ``True`` for every point that is inside the layer.
        """

        point_3d = self.unpop_axis(
            ax_coord=self.center[self.axis], plane_coords=point, axis=self.axis
        )
        return self._slightly_enlarged_box.inside(point_3d[0], point_3d[1], point_3d[2])

    def _corners_and_convexity_2d(
        self, structure_list: list[Structure], ravel: bool
    ) -> tuple[list[ArrayFloat2D], list[ArrayFloat1D]]:
        """Raw inplane corners and their convexity."""
        if self.corner_finder is None:
            return [], []

        # filter structures outside the layer
        structures_intersect = structure_list
        if self._is_inplane_bounded:
            structures_intersect = [s for s in structure_list if self.intersects(s.geometry)]
        inplane_points, convexity = self.corner_finder._corners_and_convexity(
            self.axis,
            self.center_axis,
            structures_intersect,
            ravel,
            self.interior_disjoint_geometries,
        )

        # filter corners outside the inplane bounds
        if self._is_inplane_bounded and len(inplane_points) > 0:
            # flatten temporary list of arrays for faster processing
            if not ravel:
                split_inds = np.cumsum([len(pts) for pts in inplane_points])[:-1]
                inplane_points = np.concatenate(inplane_points)
                convexity = np.concatenate(convexity)
            inds = [self._inplane_inside(point) for point in inplane_points]
            inplane_points = inplane_points[inds]
            convexity = convexity[inds]
            if not ravel:
                inplane_points = np.split(inplane_points, split_inds)
                convexity = np.split(convexity, split_inds)

        return inplane_points, convexity

    def _dl_min_from_smallest_feature(self, structure_list: list[Structure]):
        """Calculate `dl_min` suggestion based on smallest feature size."""

        inplane_points, convexity = self._corners_and_convexity_2d(
            structure_list=structure_list, ravel=False
        )

        dl_min = inf

        if self.corner_finder is None or self.corner_finder._no_min_dl_override:
            return dl_min

        finder = self.corner_finder

        for points, conv in zip(inplane_points, convexity):
            conv_nei = np.roll(conv, -1)
            lengths = np.linalg.norm(points - np.roll(points, axis=0, shift=-1), axis=-1)

            if finder.convex_resolution is not None:
                convex_features = np.logical_and(conv, conv_nei)
                if np.any(convex_features):
                    min_convex_size = np.min(lengths[convex_features])
                    dl_min = min(dl_min, min_convex_size / finder.convex_resolution)

            if finder.concave_resolution is not None:
                concave_features = np.logical_not(np.logical_or(conv, conv_nei))
                if np.any(concave_features):
                    min_concave_size = np.min(lengths[concave_features])
                    dl_min = min(dl_min, min_concave_size / finder.concave_resolution)

            if finder.mixed_resolution is not None:
                mixed_features = np.logical_xor(conv, conv_nei)
                if np.any(mixed_features):
                    min_mixed_size = np.min(lengths[mixed_features])
                    dl_min = min(dl_min, min_mixed_size / finder.mixed_resolution)

        return dl_min

    def _corners(
        self, structure_list: list[Structure], cached_corners_and_convexity=None
    ) -> list[CoordinateOptional]:
        """Inplane corners in 3D coordinate."""
        if self.corner_finder is None:
            return []
        if cached_corners_and_convexity is None:
            inplane_points, _ = self._corners_and_convexity_2d(
                structure_list=structure_list, ravel=True
            )
        else:
            inplane_points, convexity = cached_corners_and_convexity
            inplane_points, _ = self.corner_finder._ravel_corners_and_convexity(
                ravel=True, corner_list=inplane_points, convexity_list=convexity
            )

        # convert 2d points to 3d
        return [
            Box.unpop_axis(ax_coord=None, plane_coords=point, axis=self.axis)
            for point in inplane_points
        ]

    @property
    def _snapping_points_along_axis(self) -> list[CoordinateOptional]:
        """Snapping points for layer bounds."""

        if self.bounds_snapping is None:
            return []
        if self.bounds_snapping == "center":
            return [
                self._unpop_axis(ax_coord=self.center_axis, plane_coord=None),
            ]
        if self.bounds_snapping == "lower":
            return [
                self._unpop_axis(ax_coord=self.bounds[0][self.axis], plane_coord=None),
            ]
        if self.bounds_snapping == "upper":
            return [
                self._unpop_axis(ax_coord=self.bounds[1][self.axis], plane_coord=None),
            ]

        # the rest is for "bounds"
        return [
            self._unpop_axis(ax_coord=self.bounds[index][self.axis], plane_coord=None)
            for index in range(1 + (self.length_axis > 0))
        ]

    def _override_structures_inplane(
        self,
        structure_list: list[Structure],
        grid_size_in_vacuum: float,
        cached_corners_and_convexity=None,
    ) -> list[MeshOverrideStructure]:
        """Inplane mesh override structures for refining mesh around corners."""
        if self.corner_refinement is None:
            return []

        return [
            self.corner_refinement.override_structure(
                corner, grid_size_in_vacuum, self.refinement_inside_sim_only
            )
            for corner in self._corners(structure_list, cached_corners_and_convexity)
        ]

    def _override_structures_along_axis(
        self, grid_size_in_vacuum: float
    ) -> list[MeshOverrideStructure]:
        """Mesh override structures for refining mesh along layer axis dimension."""

        override_structures = []
        dl = inf
        # minimal number of step sizes along layer axis
        if self.min_steps_along_axis is not None and self.length_axis > 0:
            dl = self.length_axis / self.min_steps_along_axis
            override_structures.append(
                MeshOverrideStructure(
                    geometry=Box(
                        center=self._unpop_axis(ax_coord=self.center_axis, plane_coord=0),
                        size=self._unpop_axis(ax_coord=self.length_axis, plane_coord=inf),
                    ),
                    dl=self._unpop_axis(ax_coord=dl, plane_coord=None),
                    shadow=False,
                    drop_outside_sim=self.refinement_inside_sim_only,
                    priority=-1,
                )
            )

        # refinement at upper and lower bounds
        if self.bounds_refinement is not None:
            refinement_structures = [
                self.bounds_refinement.override_structure(
                    self._unpop_axis(ax_coord=self.bounds[index][self.axis], plane_coord=None),
                    grid_size_in_vacuum,
                    drop_outside_sim=self.refinement_inside_sim_only,
                )
                for index in range(1 + (self.length_axis > 0))
            ]
            # combine them to one if the two overlap
            if len(refinement_structures) == 2 and refinement_structures[0].geometry.intersects(
                refinement_structures[1].geometry
            ):
                rmin, rmax = Box.bounds_union(
                    refinement_structures[0].geometry.bounds,
                    refinement_structures[1].geometry.bounds,
                )
                combined_structure = MeshOverrideStructure(
                    geometry=Box.from_bounds(rmin=rmin, rmax=rmax),
                    dl=refinement_structures[0].dl,
                    shadow=False,
                    drop_outside_sim=self.refinement_inside_sim_only,
                )
                refinement_structures = [
                    combined_structure,
                ]

            # drop if the grid size is no greater than the one from "min_steps_along_axis"
            if refinement_structures[0].dl[self.axis] <= dl:
                override_structures += refinement_structures
        return override_structures

    def _find_vertical_intersections(
        self, grid_x_coords, grid_y_coords, poly_vertices, boundary
    ) -> tuple[list[tuple[int, int]], list[float]]:
        """Detect intersection points of single polygon and vertical grid lines."""

        # indices of cells that contain intersection with grid lines (left edge of a cell)
        cells_ij = []
        # relative displacements of intersection from the bottom of the cell along y axis
        cells_dy = []
        # whether intersections are valid: if polygon segment is almost parallel to
        # a grid line, we mark those intersection as invalid
        cells_valid = []

        # for each polygon vertex find the index of the first grid line on the right
        grid_lines_on_right = np.argmax(grid_x_coords[:, None] >= poly_vertices[None, :, 0], axis=0)
        grid_lines_on_right[poly_vertices[:, 0] >= grid_x_coords[-1]] = len(grid_x_coords)
        # once we know these indices then we can find grid lines intersected by the i-th
        # segment of the polygon as
        # [grid_lines_on_right[i], grid_lines_on_right[i+1]) for grid_lines_on_right[i] > grid_lines_on_right[i+1]
        # or
        # [grid_lines_on_right[i+1], grid_lines_on_right[i]) for grid_lines_on_right[i] < grid_lines_on_right[i+1]

        # loop over segments of the polygon and determine in which cells and where exactly they cross grid lines
        # v_beg and v_end are the starting and ending points of the segment
        # ind_beg and ind_end are starting and ending indices of vertical grid lines that the segment intersects
        # as described above
        for ind_beg, ind_end, v_beg, v_end in zip(
            grid_lines_on_right,
            np.roll(grid_lines_on_right, -1),
            poly_vertices,
            np.roll(poly_vertices, axis=0, shift=-1),
        ):
            # no intersections
            if ind_end == ind_beg:
                continue

            # intersects one grid line but almost parallel to it
            not_nearly_parallel = True
            if np.abs(ind_end - ind_beg) == 1:
                delta_x = np.abs(v_beg[0] - v_end[0])
                delta_y = np.abs(v_beg[1] - v_end[1])
                grid_size_x = np.abs(grid_x_coords[ind_beg - 1] - grid_x_coords[ind_end - 1])
                # we discard segments that are substantially vertical with respect to both grid step size
                # and its own vertical size (so that we don't discard tiny pieces of curved boundaries)
                if delta_x < 2 * GAP_MESHING_TOL * min(grid_size_x, delta_y):
                    not_nearly_parallel = False

            # sort vertices in ascending order to make treatmeant unifrom
            reverse = False
            if ind_beg > ind_end:
                reverse = True
                ind_beg, ind_end, v_beg, v_end = ind_end, ind_beg, v_end, v_beg

            # x coordinates are simply x coordinates of intersected vertical grid lines
            intersections_x = grid_x_coords[ind_beg:ind_end]

            # y coordinates can be found from line equation
            intersections_y = v_beg[1] + (v_end[1] - v_beg[1]) / (v_end[0] - v_beg[0]) * (
                intersections_x - v_beg[0]
            )

            # however, some of the vertical lines might be crossed
            # outside of computational domain
            # so we need to see which ones are actually inside along y axis
            inds_inside_grid = np.logical_and(
                intersections_y >= grid_y_coords[0], intersections_y <= grid_y_coords[-1]
            )

            intersections_y = intersections_y[inds_inside_grid]

            # find i and j indices of cells which contain these intersections

            # i indices are simply indices of crossed vertical grid lines
            cell_is = np.arange(ind_beg, ind_end)[inds_inside_grid]

            # j indices can be computed by finding insertion indices
            # of y coordinates of intersection points into array of y coordinates
            # of the grid lines that preserve sorting
            cell_js = np.searchsorted(grid_y_coords, intersections_y) - 1

            # find local dy, that is, the distance between the intersection point
            # and the bottom edge of the cell
            dy = (intersections_y - grid_y_coords[cell_js]) / (
                grid_y_coords[cell_js + 1] - grid_y_coords[cell_js]
            )

            # preserve uniform ordering along perimeter of the polygon
            if reverse:
                cell_is = cell_is[::-1]
                cell_js = cell_js[::-1]
                dy = dy[::-1]

            # record info
            cells_ij.append(np.transpose([cell_is, cell_js]))
            cells_dy.append(dy)
            cells_valid.append(not_nearly_parallel * np.ones_like(dy))

        if len(cells_ij) > 0:
            cells_ij = np.concatenate(cells_ij)
            cells_dy = np.concatenate(cells_dy)
            cells_valid = np.concatenate(cells_valid)

            # Filter from re-entering subcell features. That is, we discard any consecutive
            # intersections if they are crossing the same edge. This happens, for example,
            # when a tiny feature pokes through an edge. This helps not to set dl_min
            # to a very low value, and take into account only actual gaps and strips.

            # To do that we use the fact that intersection points are recorded and stored
            # in the order as they appear along the border of the polygon.

            # first we calculate linearized indices of edges (cells) they cross
            linear_index = cells_ij[:, 0] * len(grid_y_coords) + cells_ij[:, 1]

            # then look at the differences with next and previous neighbors
            fwd_diff = linear_index - np.roll(linear_index, -1)
            bwd_diff = np.roll(fwd_diff, 1)

            # an intersection point is not a part of a "re-entering subcell feature"
            # if it doesn't cross the same edges as its neighbors
            valid = np.logical_and(fwd_diff != 0, bwd_diff != 0)
            valid = np.logical_and(valid, cells_valid)

            cells_dy = cells_dy[valid]
            cells_ij = cells_ij[valid]

            # Now we are duplicating intersection points very close to cell boundaries
            # to corresponding adjacent cells. Basically, if we have a line crossing
            # very close to a grid node, we consider that it crosses edges on both sides
            # from that node. That is, this serves as a tolerance allowance.
            # Note that duplicated intersections and their originals will be snapped to
            # cell boundaries during quantization later.
            close_to_zero = cells_dy < GAP_MESHING_TOL
            close_to_one = (1.0 - cells_dy) < GAP_MESHING_TOL

            points_to_duplicate_near_zero = cells_ij[close_to_zero]
            points_to_duplicate_near_one = cells_ij[close_to_one]

            # if we go beyond simulation domain boundary, either ignore
            # or wrap periodically depending on boundary conditions
            cells_ij_zero_side = points_to_duplicate_near_zero - np.array([0, 1])
            cells_zero_side_out = cells_ij_zero_side[:, 1] == -1
            if boundary[0] == "periodic":
                cells_ij_zero_side[cells_zero_side_out, 1] = len(grid_y_coords) - 2
            else:
                cells_ij_zero_side = cells_ij_zero_side[cells_zero_side_out == 0]

            cells_ij_one_side = points_to_duplicate_near_one + np.array([0, 1])
            cells_one_side_out = cells_ij_one_side[:, 1] == len(grid_y_coords) - 1
            if boundary[1] == "periodic":
                cells_ij_one_side[cells_one_side_out, 1] = 0
            else:
                cells_ij_one_side = cells_ij_one_side[cells_one_side_out == 0]

            cells_ij = np.concatenate(
                [
                    cells_ij,
                    cells_ij_zero_side,
                    cells_ij_one_side,
                ]
            )
            cells_dy = np.concatenate(
                [
                    cells_dy,
                    np.ones(len(cells_ij_zero_side)),
                    np.zeros(len(cells_ij_one_side)),
                ]
            )

        return cells_ij, cells_dy

    def _process_poly(
        self, grid_x_coords, grid_y_coords, poly_vertices, boundaries
    ) -> tuple[list[tuple[int, int]], list[float], list[tuple[int, int]], list[float]]:
        """Detect intersection points of single polygon and grid lines."""

        # find cells that contain intersections of vertical grid lines
        # and relative locations of those intersections (along y axis)
        v_cells_ij, v_cells_dy = self._find_vertical_intersections(
            grid_x_coords, grid_y_coords, poly_vertices, boundaries[1]
        )

        # find cells that contain intersections of horizontal grid lines
        # and relative locations of those intersections (along x axis)
        # reuse the same command but flip dimensions
        h_cells_ij, h_cells_dx = self._find_vertical_intersections(
            grid_y_coords, grid_x_coords, np.flip(poly_vertices, axis=1), boundaries[0]
        )
        if len(h_cells_ij) > 0:
            # flip dimensions back
            h_cells_ij = np.roll(h_cells_ij, axis=1, shift=1)

        return v_cells_ij, v_cells_dy, h_cells_ij, h_cells_dx

    def _process_slice(
        self, x, y, merged_geos, boundaries
    ) -> tuple[list[tuple[int, int]], list[float], list[tuple[int, int]], list[float]]:
        """Detect intersection points of geometries boundaries and grid lines."""

        # cells that contain intersections of vertical grid lines
        v_cells_ij = []
        # relative locations of those intersections (along y axis)
        v_cells_dy = []

        # cells that contain intersections of horizontal grid lines
        h_cells_ij = []
        # relative locations of those intersections (along x axis)
        h_cells_dx = []

        # for PEC and PMC boundary - treat them as PEC structure
        # so that gaps are resolved near boundaries if any
        nx = len(x)
        ny = len(y)

        if boundaries[0][0] == "pec/pmc":
            h_cells_ij.append(np.transpose([np.zeros(ny), np.arange(ny)]).astype(int))
            h_cells_dx.append(np.zeros(ny))

        if boundaries[0][1] == "pec/pmc":
            h_cells_ij.append(np.transpose([(nx - 2) * np.ones(ny), np.arange(ny)]).astype(int))
            h_cells_dx.append(np.ones(ny))

        if boundaries[1][0] == "pec/pmc":
            v_cells_ij.append(np.transpose([np.arange(nx), np.zeros(nx)]).astype(int))
            v_cells_dy.append(np.zeros(nx, dtype=int))

        if boundaries[1][1] == "pec/pmc":
            v_cells_ij.append(np.transpose([np.arange(nx), (ny - 2) * np.ones(nx)]).astype(int))
            v_cells_dy.append(np.ones(nx))

        # loop over all shapes
        for mat, shapes in merged_geos:
            if not mat.is_pec:
                # note that we expect LossyMetal's converted into PEC in merged_geos
                # that is why we are not checking for that separately
                continue
            polygon_list = ClipOperation.to_polygon_list(shapes)
            for poly in polygon_list:
                poly = poly.normalize().buffer(0)

                # find intersections of a polygon with grid lines
                # specifically:
                # 0. cells that contain intersections of vertical grid lines
                # 1. relative locations of those intersections along y axis
                # 2. cells that contain intersections of horizontal grid lines
                # 3. relative locations of those intersections along x axis
                data = self._process_poly(x, y, np.array(poly.exterior.coords)[:-1], boundaries)

                if len(data[0]) > 0:
                    v_cells_ij.append(data[0])
                    v_cells_dy.append(data[1])

                if len(data[2]) > 0:
                    h_cells_ij.append(data[2])
                    h_cells_dx.append(data[3])

                # in case the polygon has holes
                for poly_inner in poly.interiors:
                    data = self._process_poly(x, y, np.array(poly_inner.coords)[:-1], boundaries)
                    if len(data[0]) > 0:
                        v_cells_ij.append(data[0])
                        v_cells_dy.append(data[1])

                    if len(data[2]) > 0:
                        h_cells_ij.append(data[2])
                        h_cells_dx.append(data[3])

        if len(v_cells_ij) > 0:
            v_cells_ij = np.concatenate(v_cells_ij)
            v_cells_dy = np.concatenate(v_cells_dy)

        if len(h_cells_ij) > 0:
            h_cells_ij = np.concatenate(h_cells_ij)
            h_cells_dx = np.concatenate(h_cells_dx)

        return v_cells_ij, v_cells_dy, h_cells_ij, h_cells_dx

    def _generate_horizontal_snapping_lines(
        self, grid_y_coords, intersected_cells_ij, relative_vert_disp
    ) -> tuple[list[CoordinateOptional], float]:
        """Convert a list of intersections of vertical grid lines, given as coordinates of cells
        and relative vertical displacement inside each cell, into locations of snapping lines that
        resolve thin gaps and strips.
        """
        min_gap_width = inf

        snapping_lines_y = []
        if len(intersected_cells_ij) > 0:
            # quantize intersection locations
            relative_vert_disp = np.round(relative_vert_disp / GAP_MESHING_TOL).astype(int)
            cell_linear_inds = (
                intersected_cells_ij[:, 0] * len(grid_y_coords) + intersected_cells_ij[:, 1]
            )
            cell_linear_inds_and_disps = np.transpose([cell_linear_inds, relative_vert_disp])
            # remove duplicates
            cell_linear_inds_and_disps_unique = np.unique(cell_linear_inds_and_disps, axis=0)

            # count intersections of vertical grid lines in each cell
            cell_linear_inds_unique, counts = np.unique(
                cell_linear_inds_and_disps_unique[:, 0], return_counts=True
            )
            # when we count intersections we use linearized 2d index because we really
            # need to count intersections in each cell separately

            # but when we need to decide about refinement, due to cartesian nature of grid
            # we will need to consider all cells with a given j index at a time

            # so, let's compute j index for each cell in the unique list
            cell_linear_inds_unique_j = cell_linear_inds_unique % len(grid_y_coords)

            # loop through all j rows that contain intersections
            for ind_j in np.unique(cell_linear_inds_unique_j):
                # we need to refine between two grid lines corresponding to index j
                # if at least one cell with given j contains > 1 intersections

                # get all intersected cells with given j index
                j_selection = cell_linear_inds_unique_j == ind_j
                # and number intersections in each of them
                counts_j = counts[j_selection]

                # find cell with max intersections
                max_count_el = np.argmax(counts_j)
                max_count = counts_j[max_count_el]
                if max_count > 1:
                    # get its linear index
                    target_cell_linear_ind = cell_linear_inds_unique[j_selection][max_count_el]
                    # look up relative positions of intersections in that cells
                    target_disps = np.sort(
                        cell_linear_inds_and_disps_unique[
                            cell_linear_inds_and_disps_unique[:, 0] == target_cell_linear_ind, 1
                        ]
                    )

                    # place a snapping line between any two neighboring intersections (in relative units)
                    relative_snap_lines_pos = (
                        0.5 * (target_disps[1:] + target_disps[:-1]) * GAP_MESHING_TOL
                    )
                    # convert relative positions to absolute ones
                    snapping_lines_y += [
                        grid_y_coords[ind_j]
                        + rel_pos * (grid_y_coords[ind_j + 1] - grid_y_coords[ind_j])
                        for rel_pos in relative_snap_lines_pos
                    ]

                    # compute minimal gap/strip width
                    min_gap_width_current = (
                        np.min(target_disps[1:] - target_disps[:-1]) * GAP_MESHING_TOL
                    )
                    min_gap_width = min(
                        min_gap_width,
                        min_gap_width_current * (grid_y_coords[ind_j + 1] - grid_y_coords[ind_j]),
                    )

        return snapping_lines_y, min_gap_width

    def _resolve_gaps(
        self, structures: list[Structure], grid: Grid, boundary_types: tuple
    ) -> tuple[list[CoordinateOptional], float]:
        """
        Detect underresolved gaps and place snapping lines in them. Also return the detected minimal gap width.

        Parameters
        ----------
        structures : list[Structure]
            List of structures to consider.
        grid : Grid
            Grid to resolve gaps on.
        boundary_types : Tuple[Tuple[str, str], Tuple[str, str], Tuple[str, str]] = [[None, None], [None, None], [None, None]]
            Type of boundary conditions along each dimension: "pec/pmc", "periodic", or
            None for any other. This is relevant only for gap meshing.

        Returns
        -------
        tuple[list[CoordinateOptional], float]
            List of snapping lines and the detected minimal gap width.
        """

        # get x and y coordinates of grid lines
        _, tan_dims = Box.pop_axis([0, 1, 2], self.axis)
        x = grid.boundaries.to_list[tan_dims[0]]
        y = grid.boundaries.to_list[tan_dims[1]]

        _, boundaries_tan = Box.pop_axis(boundary_types, self.axis)

        # restrict to the size of layer spec
        rmin, rmax = self.bounds
        _, rmin = Box.pop_axis(rmin, self.axis)
        _, rmax = Box.pop_axis(rmax, self.axis)

        new_coords = []
        new_boundaries = []
        for coord, cmin, cmax, bdry in zip([x, y], rmin, rmax, boundaries_tan):
            if cmax <= coord[0] or cmin >= coord[-1]:
                return [], inf
            if cmin < coord[0]:
                ind_min = 0
            else:
                ind_min = max(0, np.argmax(coord >= cmin) - 1)

            if cmax > coord[-1]:
                ind_max = len(coord) - 1
            else:
                ind_max = np.argmax(coord >= cmax)

            if ind_min >= ind_max - 1:
                return [], inf

            new_coords.append(coord[ind_min : (ind_max + 1)])
            # ignore boundary conditions if we are not touching them
            new_boundaries.append(
                [
                    None if ind_min > 0 else bdry[0],
                    None if ind_max < len(coord) - 1 else bdry[1],
                ]
            )

        x, y = new_coords

        merging_area_bounds = np.array(
            [[x[0] - fp_eps, y[0] - fp_eps], [x[-1] + fp_eps, y[-1] + fp_eps]]
        )

        # restrict size of the plane where pec polygons are found in case of periodic boundary conditions
        # this is to make sure gaps across periodic boundary conditions are resolved
        # (if there is a PEC structure going into periodic boundary, now it will generate a grid line
        # intersection next to that boundary and it will be propagated to the other side)
        for ind in range(2):
            if new_boundaries[ind][0] == "periodic":
                merging_area_bounds[0][ind] += fp_eps + dp_eps
                merging_area_bounds[1][ind] -= fp_eps + dp_eps

        merging_area_center = 0.5 * (merging_area_bounds[0] + merging_area_bounds[1])
        merging_area_size = merging_area_bounds[1] - merging_area_bounds[0]

        merging_area_center = Box.unpop_axis(self.center[self.axis], merging_area_center, self.axis)
        merging_area_size = Box.unpop_axis(self.size[self.axis], merging_area_size, self.axis)

        # get merged pec structures on plane
        # note that we expect this function to also convert all LossyMetal's into PEC
        plane_slice = CornerFinderSpec._merged_pec_on_plane(
            coord=self.center_axis,
            normal_axis=self.axis,
            structure_list=structures,
            center=merging_area_center,
            size=merging_area_size,
            interior_disjoint_geometries=self.interior_disjoint_geometries,
        )

        # find intersections of pec polygons with grid lines
        # specifically:
        # 0. cells that contain intersections of vertical grid lines
        # 1. relative locations of those intersections along y axis
        # 2. cells that contain intersections of horizontal grid lines
        # 3. relative locations of those intersections along x axis
        v_cells_ij, v_cells_dy, h_cells_ij, h_cells_dx = self._process_slice(
            x, y, plane_slice, new_boundaries
        )

        # generate horizontal snapping lines
        snapping_lines_y, min_gap_width_along_y = self._generate_horizontal_snapping_lines(
            y, v_cells_ij, v_cells_dy
        )
        detected_gap_width = min_gap_width_along_y

        # generate vertical snapping lines
        if len(h_cells_ij) > 0:  # check, otherwise np.roll fails
            snapping_lines_x, min_gap_width_along_x = self._generate_horizontal_snapping_lines(
                x, np.roll(h_cells_ij, shift=1, axis=1), h_cells_dx
            )

            detected_gap_width = min(detected_gap_width, min_gap_width_along_x)
        else:
            snapping_lines_x = []

        # convert snapping lines' coordinates into 3d coordinates
        snapping_lines_y_3d = [
            Box.unpop_axis(Y, (None, None), axis=tan_dims[1]) for Y in snapping_lines_y
        ]
        snapping_lines_x_3d = [
            Box.unpop_axis(X, (None, None), axis=tan_dims[0]) for X in snapping_lines_x
        ]

        return snapping_lines_x_3d + snapping_lines_y_3d, detected_gap_width


class GridSpec(Tidy3dBaseModel):
    """Collective grid specification for all three dimensions.

    Example
    -------
    >>> uniform = UniformGrid(dl=0.1)
    >>> custom = CustomGrid(dl=[0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2])
    >>> auto = AutoGrid(min_steps_per_wvl=12)
    >>> grid_spec = GridSpec(grid_x=uniform, grid_y=custom, grid_z=auto, wavelength=1.5)

    See Also
    --------

    :class:`.UniformGrid`
        Uniform 1D grid.

    :class:`.AutoGrid`
        Specification for non-uniform grid along a given dimension.

    **Notebooks:**
        * `Using automatic nonuniform meshing <../../notebooks/AutoGrid.html>`_

    **Lectures:**
        *  `Time step size and CFL condition in FDTD <https://www.flexcompute.com/fdtd101/Lecture-7-Time-step-size-and-CFL-condition-in-FDTD/>`_
        *  `Numerical dispersion in FDTD <https://www.flexcompute.com/fdtd101/Lecture-8-Numerical-dispersion-in-FDTD/>`_
    """

    grid_x: GridType = pd.Field(
        AutoGrid(),
        title="Grid specification along x-axis",
        description="Grid specification along x-axis",
        discriminator=TYPE_TAG_STR,
    )

    grid_y: GridType = pd.Field(
        AutoGrid(),
        title="Grid specification along y-axis",
        description="Grid specification along y-axis",
        discriminator=TYPE_TAG_STR,
    )

    grid_z: GridType = pd.Field(
        AutoGrid(),
        title="Grid specification along z-axis",
        description="Grid specification along z-axis",
        discriminator=TYPE_TAG_STR,
    )

    wavelength: float = pd.Field(
        None,
        title="Free-space wavelength",
        description="Free-space wavelength for automatic nonuniform grid. It can be ``None`` "
        "if there is at least one source in the simulation, in which case it is defined by "
        "the source central frequency. "
        "Note: it only takes effect when at least one of the three dimensions "
        "uses :class:`.AutoGrid`.",
        units=MICROMETER,
    )

    override_structures: tuple[annotate_type(StructureType), ...] = pd.Field(
        (),
        title="Grid specification override structures",
        description="A set of structures that is added on top of the simulation structures in "
        "the process of generating the grid. This can be used to refine the grid or make it "
        "coarser depending than the expected need for higher/lower resolution regions. "
        "Note: it only takes effect when at least one of the three dimensions "
        "uses :class:`.AutoGrid` or :class:`.QuasiUniformGrid`.",
    )

    snapping_points: tuple[CoordinateOptional, ...] = pd.Field(
        (),
        title="Grid specification snapping_points",
        description="A set of points that enforce grid boundaries to pass through them. "
        "However, some points might be skipped if they are too close. "
        "When points are very close to `override_structures`, `snapping_points` have "
        "higher prioirty so that the structures might be skipped. "
        "Note: it only takes effect when at least one of the three dimensions "
        "uses :class:`.AutoGrid` or :class:`.QuasiUniformGrid`.",
    )

    layer_refinement_specs: tuple[LayerRefinementSpec, ...] = pd.Field(
        (),
        title="Mesh Refinement In Layered Structures",
        description="Automatic mesh refinement according to layer specifications. The material "
        "distribution is assumed to be uniform inside the layer along the layer axis. "
        "Mesh can be refined around corners on the layer cross section, and around upper and lower "
        "bounds of the layer.",
    )

    @cached_property
    def snapped_grid_used(self) -> bool:
        """True if any of the three dimensions uses :class:`.AbstractAutoGrid` that will adjust grid with snapping
        points and geometry boundaries.
        """
        grid_list = [self.grid_x, self.grid_y, self.grid_z]
        return np.any([isinstance(mesh, AbstractAutoGrid) for mesh in grid_list])

    @cached_property
    def auto_grid_used(self) -> bool:
        """True if any of the three dimensions uses :class:`.AutoGrid`."""
        grid_list = [self.grid_x, self.grid_y, self.grid_z]
        return np.any([isinstance(mesh, AutoGrid) for mesh in grid_list])

    @property
    def custom_grid_used(self) -> bool:
        """True if any of the three dimensions uses :class:`.CustomGrid`."""
        grid_list = [self.grid_x, self.grid_y, self.grid_z]
        return np.any([isinstance(mesh, (CustomGrid, CustomGridBoundaries)) for mesh in grid_list])

    @staticmethod
    def wavelength_from_sources(sources: list[SourceType]) -> pd.PositiveFloat:
        """Define a wavelength based on supplied sources. Called if auto mesh is used and
        ``self.wavelength is None``."""

        # no sources
        if len(sources) == 0:
            raise SetupError(
                "Automatic grid generation requires the input of 'wavelength' or sources."
            )

        # Use central frequency of sources, if any.
        freqs = np.array([source.source_time.freq0 for source in sources])

        # multiple sources of different central frequencies
        if not np.all(np.isclose(freqs, freqs[0])):
            raise SetupError(
                "Sources of different central frequencies are supplied. "
                "Please supply a 'wavelength' value for 'grid_spec'."
            )

        return C_0 / freqs[0]

    @cached_property
    def layer_refinement_used(self) -> bool:
        """Whether layer_refiement_specs are applied."""
        return len(self.layer_refinement_specs) > 0

    @property
    def snapping_points_used(self) -> list[bool, bool, bool]:
        """Along each axis, ``True`` if any snapping point is used. However,
        it is still ``False`` if all snapping points take value ``None`` along the axis.
        """

        # empty list
        if len(self.snapping_points) == 0:
            return [False] * 3

        snapping_used = [False] * 3
        for point in self.snapping_points:
            for ind_coord, coord in enumerate(point):
                if snapping_used[ind_coord]:
                    continue
                if coord is not None:
                    snapping_used[ind_coord] = True
        return snapping_used

    @property
    def override_structures_used(self) -> list[bool, bool, bool]:
        """Along each axis, ``True`` if any override structure is used. However,
        it is still ``False`` if only :class:`.MeshOverrideStructure` is supplied, and
        their ``dl[axis]`` all take the ``None`` value.
        """

        # empty override_structure list
        if len(self.override_structures) == 0:
            return [False] * 3

        override_used = [False] * 3
        for structure in self.override_structures:
            # override used in all axes if any `Structure` is present
            if isinstance(structure, Structure):
                return [True] * 3

            for dl_axis, dl in enumerate(structure.dl):
                if (not override_used[dl_axis]) and (dl is not None):
                    override_used[dl_axis] = True
        return override_used

    def internal_snapping_points(
        self,
        structures: list[Structure],
        lumped_elements: list[LumpedElementType],
        cached_corners_and_convexity=None,
    ) -> list[CoordinateOptional]:
        """Internal snapping points. So far, internal snapping points are generated by
        `layer_refinement_specs` and lumped element.

        Parameters
        ----------
        structures : List[Structure]
            List of physical structures.
        lumped_elements : List[LumpedElementType]
            List of lumped elements.
        cached_corners_and_convexity : Optional[list[CachedCornersAndConvexity]]
            Cached corners and convexity data.

        Returns
        -------
        List[CoordinateOptional]
            List of snapping points coordinates.
        """

        # no need to generate anything if autogrid is not used
        if not self.auto_grid_used:
            return []

        snapping_points = []
        # 1) from layer refinement spec
        if self.layer_refinement_used:
            for ind, layer_spec in enumerate(self.layer_refinement_specs):
                if cached_corners_and_convexity is not None:
                    cached_data = cached_corners_and_convexity[ind]
                else:
                    cached_data = None
                snapping_points += layer_spec.generate_snapping_points(
                    list(structures), cached_data
                )
        # ) from lumped_elements
        for lumped_element in lumped_elements:
            snapping_points += lumped_element.to_snapping_points()
        return snapping_points

    def all_snapping_points(
        self,
        structures: list[Structure],
        lumped_elements: list[LumpedElementType],
        internal_snapping_points: Optional[list[CoordinateOptional]] = None,
    ) -> list[CoordinateOptional]:
        """Internal and external snapping points. External snapping points take higher priority.
        So far, internal snapping points are generated by `layer_refinement_specs`.

        Parameters
        ----------
        structures : List[Structure]
            List of physical structures.
        lumped_elements : List[LumpedElementType]
            List of lumped elements.
        internal_snapping_points : List[CoordinateOptional]
            If `None`, recomputes internal snapping points.

        Returns
        -------
        List[CoordinateOptional]
            List of snapping points coordinates.
        """

        if internal_snapping_points is None:
            return self.internal_snapping_points(structures, lumped_elements) + list(
                self.snapping_points
            )
        return internal_snapping_points + list(self.snapping_points)

    @property
    def external_override_structures(self) -> list[StructureType]:
        """External supplied override structure list."""
        return [s.to_static() for s in self.override_structures]

    def internal_override_structures(
        self,
        structures: list[Structure],
        wavelength: pd.PositiveFloat,
        sim_size: tuple[float, 3],
        lumped_elements: list[LumpedElementType],
        cached_corners_and_convexity=None,
    ) -> list[StructureType]:
        """Internal mesh override structures. So far, internal override structures are generated by
        `layer_refinement_specs` and lumped element.

        Parameters
        ----------
        structures : List[Structure]
            List of structures, with the simulation structure being the first item.
        wavelength : pd.PositiveFloat
            Wavelength to use for minimal step size in vaccum.
        sim_size : Tuple[float, 3]
            Simulation domain size.
        lumped_elements : List[LumpedElementType]
            List of lumped elements.
        cached_corners_and_convexity : Optional[list[CachedCornersAndConvexity]]
            Cached corners and convexity data.

        Returns
        -------
        List[StructureType]
            List of override structures.
        """

        # no need to generate anything if autogrid is not used
        if not self.auto_grid_used:
            return []

        override_structures = []
        # 1) from layer refinement spec
        if self.layer_refinement_used:
            for ind, layer_spec in enumerate(self.layer_refinement_specs):
                if cached_corners_and_convexity is not None:
                    cached_data = cached_corners_and_convexity[ind]
                else:
                    cached_data = None
                override_structures += layer_spec.generate_override_structures(
                    self._min_vacuum_dl_in_autogrid(wavelength, sim_size),
                    list(structures),
                    cached_data,
                )
        # 2) from lumped element
        for lumped_element in lumped_elements:
            override_structures += lumped_element.to_mesh_overrides()
        return override_structures

    def all_override_structures(
        self,
        structures: list[Structure],
        wavelength: pd.PositiveFloat,
        sim_size: tuple[float, 3],
        lumped_elements: list[LumpedElementType],
        structure_priority_mode: PriorityMode = "equal",
        internal_override_structures: Optional[list[MeshOverrideStructure]] = None,
    ) -> list[StructureType]:
        """Internal and external mesh override structures sorted based on their priority. By default,
        the priority of internal override structures is -1, and 0 for external ones.

        Parameters
        ----------
        structures : List[Structure]
            List of structures, with the simulation structure being the first item.
        wavelength : pd.PositiveFloat
            Wavelength to use for minimal step size in vaccum.
        sim_size : Tuple[float, 3]
            Simulation domain size.
        lumped_elements : List[LumpedElementType]
            List of lumped elements.
        structure_priority_mode : PriorityMode
            Structure priority setting.
        internal_override_structures : List[MeshOverrideStructure]
            If `None`, recomputes internal override structures.

        Returns
        -------
        List[StructureType]
            List of sorted override structures.
        """

        if internal_override_structures is None:
            internal_override_structures = self.internal_override_structures(
                structures, wavelength, sim_size, lumped_elements
            )
        all_structures = internal_override_structures + self.external_override_structures
        return Structure._sort_structures(all_structures, structure_priority_mode)

    def _min_vacuum_dl_in_autogrid(self, wavelength: float, sim_size: tuple[float, 3]) -> float:
        """Compute grid step size in vacuum for Autogrd. If AutoGrid is applied along more than 1 dimension,
        return the minimal.
        """
        dl = inf
        for grid in [self.grid_x, self.grid_y, self.grid_z]:
            if isinstance(grid, AutoGrid):
                dl = min(dl, grid._vacuum_dl(wavelength, sim_size))
        return dl

    def _dl_min(
        self,
        wavelength: float,
        structure_list: list[StructureType],
        sim_size: tuple[float, 3],
        lumped_elements: list[LumpedElementType],
    ) -> float:
        """Lower bound of grid size to be applied to dimensions where AutoGrid with unset
        `dl_min` (0 or None) is applied.
        """

        # split structure list into `Structure` and `MeshOverrideStructure`
        structures = [
            medium_str for medium_str in structure_list if isinstance(medium_str, Structure)
        ]
        mesh_structures = [
            mesh_str for mesh_str in structure_list if isinstance(mesh_str, MeshOverrideStructure)
        ]

        min_dl = inf
        # minimal grid size from MeshOverrideStructure
        for structure in mesh_structures:
            for dl in structure.dl:
                if dl is not None and dl < min_dl:
                    min_dl = dl
        # from mesh specification
        for grid in [self.grid_x, self.grid_y, self.grid_z]:
            min_dl = min(min_dl, grid.estimated_min_dl(wavelength, structures, sim_size))

        # from layer refinement specifications
        if self.layer_refinement_used:
            min_vacuum_dl = self._min_vacuum_dl_in_autogrid(wavelength, sim_size)
            for layer in self.layer_refinement_specs:
                min_dl = min(min_dl, layer.suggested_dl_min(min_vacuum_dl, structures))
        # from lumped elements
        for lumped_element in lumped_elements:
            for override_structure in lumped_element.to_mesh_overrides():
                min_dl = min(min_dl, min(override_structure.dl))
        return min_dl * MIN_STEP_BOUND_SCALE

    def get_wavelength(self, sources: list[SourceType]) -> float:
        """Get wavelength for automatic mesh generation if needed."""
        wavelength = self.wavelength
        if wavelength is None and self.auto_grid_used:
            wavelength = self.wavelength_from_sources(sources)
            log.info(f"Auto meshing using wavelength {wavelength:1.4f} defined from sources.")
        return wavelength

    def make_grid(
        self,
        structures: list[Structure],
        symmetry: tuple[Symmetry, Symmetry, Symmetry],
        periodic: tuple[bool, bool, bool],
        sources: list[SourceType],
        num_pml_layers: list[tuple[pd.NonNegativeInt, pd.NonNegativeInt]],
        lumped_elements: list[LumpedElementType] = (),
        internal_override_structures: Optional[list[MeshOverrideStructure]] = None,
        internal_snapping_points: Optional[list[CoordinateOptional]] = None,
        boundary_types: tuple[tuple[str, str], tuple[str, str], tuple[str, str]] = [
            [None, None],
            [None, None],
            [None, None],
        ],
        structure_priority_mode: PriorityMode = "equal",
    ) -> Grid:
        """Make the entire simulation grid based on some simulation parameters.

        Parameters
        ----------
        structures : List[Structure]
            List of structures present in the simulation. The first structure must be the
            simulation geometry with the simulation background medium.
        symmetry : Tuple[Symmetry, Symmetry, Symmetry]
            Reflection symmetry across a plane bisecting the simulation domain
            normal to each of the three axes.
        periodic: Tuple[bool, bool, bool]
            Apply periodic boundary condition or not along each of the dimensions.
            Only relevant for autogrids.
        sources : List[SourceType]
            List of sources.
        num_pml_layers : List[Tuple[float, float]]
            List containing the number of absorber layers in - and + boundaries.
        lumped_elements : List[LumpedElementType]
            List of lumped elements.
        internal_override_structures : List[MeshOverrideStructure]
            If `None`, recomputes internal override structures.
        internal_snapping_points : List[CoordinateOptional]
            If `None`, recomputes internal snapping points.
        boundary_types : Tuple[Tuple[str, str], Tuple[str, str], Tuple[str, str]] = [[None, None], [None, None], [None, None]]
            Type of boundary conditions along each dimension: "pec/pmc", "periodic", or
            None for any other. This is relevant only for gap meshing.
        structure_priority_mode : PriorityMode
            Structure priority setting.

        Returns
        -------
        Grid:
            Entire simulation grid.
        """

        grid, _ = self._make_grid_and_snapping_lines(
            structures=structures,
            symmetry=symmetry,
            periodic=periodic,
            sources=sources,
            num_pml_layers=num_pml_layers,
            lumped_elements=lumped_elements,
            internal_override_structures=internal_override_structures,
            internal_snapping_points=internal_snapping_points,
            structure_priority_mode=structure_priority_mode,
        )

        return grid

    def _make_grid_and_snapping_lines(
        self,
        structures: list[Structure],
        symmetry: tuple[Symmetry, Symmetry, Symmetry],
        periodic: tuple[bool, bool, bool],
        sources: list[SourceType],
        num_pml_layers: list[tuple[pd.NonNegativeInt, pd.NonNegativeInt]],
        lumped_elements: list[LumpedElementType] = (),
        internal_override_structures: Optional[list[MeshOverrideStructure]] = None,
        internal_snapping_points: Optional[list[CoordinateOptional]] = None,
        boundary_types: tuple[tuple[str, str], tuple[str, str], tuple[str, str]] = [
            [None, None],
            [None, None],
            [None, None],
        ],
        structure_priority_mode: PriorityMode = "equal",
    ) -> tuple[Grid, list[CoordinateOptional]]:
        """Make the entire simulation grid based on some simulation parameters.
        Also return snappiung point resulted from iterative gap meshing.

        Parameters
        ----------
        structures : List[Structure]
            List of structures present in the simulation. The first structure must be the
            simulation geometry with the simulation background medium.
        symmetry : Tuple[Symmetry, Symmetry, Symmetry]
            Reflection symmetry across a plane bisecting the simulation domain
            normal to each of the three axes.
        periodic: Tuple[bool, bool, bool]
            Apply periodic boundary condition or not along each of the dimensions.
            Only relevant for autogrids.
        sources : List[SourceType]
            List of sources.
        num_pml_layers : List[Tuple[float, float]]
            List containing the number of absorber layers in - and + boundaries.
        lumped_elements : List[LumpedElementType]
            List of lumped elements.
        internal_override_structures : List[MeshOverrideStructure]
            If `None`, recomputes internal override structures.
        internal_snapping_points : List[CoordinateOptional]
            If `None`, recomputes internal snapping points.
        boundary_types : Tuple[Tuple[str, str], Tuple[str, str], Tuple[str, str]] = [[None, None], [None, None], [None, None]]
            Type of boundary conditions along each dimension: "pec/pmc", "periodic", or
            None for any other. This is relevant only for gap meshing.
        structure_priority_mode : PriorityMode
            Structure priority setting.

        Returns
        -------
        Tuple[Grid, List[CoordinateOptional]]:
            Entire simulation grid and snapping points generated during iterative gap meshing.
        """

        old_grid = self._make_grid_one_iteration(
            structures=structures,
            symmetry=symmetry,
            periodic=periodic,
            sources=sources,
            num_pml_layers=num_pml_layers,
            lumped_elements=lumped_elements,
            internal_override_structures=internal_override_structures,
            internal_snapping_points=internal_snapping_points,
            structure_priority_mode=structure_priority_mode,
        )

        snapping_lines = []
        if len(self.layer_refinement_specs) > 0:
            num_iters = max(
                layer_spec.gap_meshing_iters for layer_spec in self.layer_refinement_specs
            )

            min_gap_width = inf
            for ind in range(num_iters):
                new_snapping_lines = []
                for layer_spec in self.layer_refinement_specs:
                    if layer_spec.gap_meshing_iters > ind:
                        one_layer_snapping_lines, gap_width = layer_spec._resolve_gaps(
                            structures,
                            old_grid,
                            boundary_types,
                        )
                        new_snapping_lines = new_snapping_lines + one_layer_snapping_lines
                        if layer_spec.dl_min_from_gap_width:
                            min_gap_width = min(min_gap_width, gap_width)

                if len(new_snapping_lines) == 0:
                    log.info(
                        "Grid is no longer changing. "
                        f"Stopping iterative gap meshing after {ind + 1}/{num_iters} iterations."
                    )
                    break

                snapping_lines = snapping_lines + new_snapping_lines

                new_grid = self._make_grid_one_iteration(
                    structures=structures,
                    symmetry=symmetry,
                    periodic=periodic,
                    sources=sources,
                    num_pml_layers=num_pml_layers,
                    lumped_elements=lumped_elements,
                    internal_override_structures=internal_override_structures,
                    internal_snapping_points=snapping_lines + internal_snapping_points,
                    dl_min_from_gaps=0.45 * min_gap_width,
                    structure_priority_mode=structure_priority_mode,
                )

                same = old_grid == new_grid

                if same:
                    log.info(
                        "Grid is no longer changing. "
                        f"Stopping iterative gap meshing after {ind + 1}/{num_iters} iterations."
                    )
                    break

                old_grid = new_grid

        return old_grid, snapping_lines

    def _make_grid_one_iteration(
        self,
        structures: list[Structure],
        symmetry: tuple[Symmetry, Symmetry, Symmetry],
        periodic: tuple[bool, bool, bool],
        sources: list[SourceType],
        num_pml_layers: list[tuple[pd.NonNegativeInt, pd.NonNegativeInt]],
        lumped_elements: list[LumpedElementType] = (),
        internal_override_structures: Optional[list[MeshOverrideStructure]] = None,
        internal_snapping_points: Optional[list[CoordinateOptional]] = None,
        dl_min_from_gaps: pd.PositiveFloat = inf,
        structure_priority_mode: PriorityMode = "equal",
    ) -> Grid:
        """Make the entire simulation grid based on some simulation parameters.

        Parameters
        ----------
        structures : List[Structure]
            List of structures present in the simulation. The first structure must be the
            simulation geometry with the simulation background medium.
        symmetry : Tuple[Symmetry, Symmetry, Symmetry]
            Reflection symmetry across a plane bisecting the simulation domain
            normal to each of the three axes.
        periodic: Tuple[bool, bool, bool]
            Apply periodic boundary condition or not along each of the dimensions.
            Only relevant for autogrids.
        sources : List[SourceType]
            List of sources.
        num_pml_layers : List[Tuple[float, float]]
            List containing the number of absorber layers in - and + boundaries.
        lumped_elements : List[LumpedElementType]
            List of lumped elements.
        internal_override_structures : List[MeshOverrideStructure]
            If `None`, recomputes internal override structures.
        internal_snapping_points : List[CoordinateOptional]
            If `None`, recomputes internal snapping points.
        dl_min_from_gaps : pd.PositiveFloat
            Minimal grid size computed based on autodetected gaps.
        structure_priority_mode : PriorityMode
            Structure priority setting.

        Returns
        -------
        Grid:
            Entire simulation grid.
        """

        # Set up wavelength for automatic mesh generation if needed.
        wavelength = self.get_wavelength(sources)

        # Warn user if ``GridType`` along some axis is not ``AutoGrid`` and
        # ``override_structures`` is not empty. The override structures
        # are not effective along those axes.
        for axis_ind, override_used_axis, snapping_used_axis, grid_axis in zip(
            ["x", "y", "z"],
            self.override_structures_used,
            self.snapping_points_used,
            [self.grid_x, self.grid_y, self.grid_z],
        ):
            if not isinstance(grid_axis, AbstractAutoGrid):
                if override_used_axis:
                    log.warning(
                        f"Override structures take no effect along {axis_ind}-axis. "
                        "If intending to apply override structures to this axis, "
                        "use 'AutoGrid' or 'QuasiUniformGrid'.",
                        capture=False,
                    )
                if snapping_used_axis:
                    log.warning(
                        f"Snapping points take no effect along {axis_ind}-axis. "
                        "If intending to apply snapping points to this axis, "
                        "use 'AutoGrid' or 'QuasiUniformGrid'.",
                        capture=False,
                    )

            if self.layer_refinement_used and not isinstance(grid_axis, AutoGrid):
                log.warning(
                    f"layer_refinement_specs take no effect along {axis_ind}-axis. "
                    "If intending to apply automatic refinement to this axis, "
                    "use 'AutoGrid'.",
                    capture=False,
                )

        grids_1d = [self.grid_x, self.grid_y, self.grid_z]

        if any(s._strip_traced_fields() for s in self.override_structures):
            log.warning(
                "The override structures were detected as having a dependence on the objective "
                "function parameters. This is not supported by our automatic differentiation "
                "framework. The derivative will be un-traced through the override structures. "
                "To make this explicit and remove this warning, use 'y = autograd.tracer.getval(x)'"
                " to remove any derivative information from values being passed to create "
                "override structures. Alternatively, 'obj = obj.to_static()' will create a copy of "
                "an instance without any autograd tracers."
            )

        sim_size = list(structures[0].geometry.size)
        all_structures = list(structures) + self.all_override_structures(
            list(structures),
            wavelength,
            sim_size,
            lumped_elements,
            structure_priority_mode,
            internal_override_structures,
        )

        # apply internal `dl_min` if any AutoGrid has unset `dl_min`
        update_dl_min = False
        for grid in grids_1d:
            if isinstance(grid, AutoGrid) and grid._undefined_dl_min:
                update_dl_min = True
                break
        if update_dl_min:
            new_dl_min = self._dl_min(
                wavelength,
                list(structures) + self.external_override_structures,
                sim_size,
                lumped_elements,
            )
            new_dl_min = min(new_dl_min, dl_min_from_gaps)
            for ind, grid in enumerate(grids_1d):
                if isinstance(grid, AutoGrid) and grid._undefined_dl_min:
                    grids_1d[ind] = grid.updated_copy(dl_min=new_dl_min)

        coords_dict = {}
        for idim, (dim, grid_1d) in enumerate(zip("xyz", grids_1d)):
            coords_dict[dim] = grid_1d.make_coords(
                axis=idim,
                structures=all_structures,
                symmetry=symmetry,
                periodic=periodic[idim],
                wavelength=wavelength,
                num_pml_layers=num_pml_layers[idim],
                snapping_points=self.all_snapping_points(
                    structures, lumped_elements, internal_snapping_points
                ),
            )

        coords = Coords(**coords_dict)
        return Grid(boundaries=coords)

    @classmethod
    def from_grid(cls, grid: Grid) -> GridSpec:
        """Import grid directly from another simulation, e.g. ``grid_spec = GridSpec.from_grid(sim.grid)``."""
        grid_dict = {}
        for dim in "xyz":
            grid_dict["grid_" + dim] = CustomGridBoundaries(coords=grid.boundaries.to_dict[dim])
        return cls(**grid_dict)

    @classmethod
    def auto(
        cls,
        wavelength: pd.PositiveFloat = None,
        min_steps_per_wvl: pd.PositiveFloat = 10.0,
        max_scale: pd.PositiveFloat = 1.4,
        override_structures: list[StructureType] = (),
        snapping_points: tuple[CoordinateOptional, ...] = (),
        layer_refinement_specs: list[LayerRefinementSpec] = (),
        dl_min: pd.NonNegativeFloat = 0.0,
        min_steps_per_sim_size: pd.PositiveFloat = 10.0,
        mesher: MesherType = Undefined,
    ) -> GridSpec:
        """Use the same :class:`.AutoGrid` along each of the three directions.

        Parameters
        ----------
        wavelength : pd.PositiveFloat, optional
            Free-space wavelength for automatic nonuniform grid. It can be 'None'
            if there is at least one source in the simulation, in which case it is defined by
            the source central frequency.
        min_steps_per_wvl : pd.PositiveFloat, optional
            Minimal number of steps per wavelength in each medium.
        max_scale : pd.PositiveFloat, optional
            Sets the maximum ratio between any two consecutive grid steps.
        override_structures : List[StructureType]
            A list of structures that is added on top of the simulation structures in
            the process of generating the grid. This can be used to refine the grid or make it
            coarser depending than the expected need for higher/lower resolution regions.
        snapping_points : Tuple[CoordinateOptional, ...]
            A set of points that enforce grid boundaries to pass through them.
        layer_refinement_specs: List[LayerRefinementSpec]
            Mesh refinement according to layer specifications.
        dl_min: pd.NonNegativeFloat
            Lower bound of grid size.
        min_steps_per_sim_size : pd.PositiveFloat, optional
            Minimal number of steps per longest edge length of simulation domain.
        mesher : MesherType = GradedMesher()
            The type of mesher to use to generate the grid automatically.

        Returns
        -------
        GridSpec
            :class:`.GridSpec` with the same automatic nonuniform grid settings in each direction.
        """
        if mesher is Undefined:
            mesher = GradedMesher()

        grid_1d = AutoGrid(
            min_steps_per_wvl=min_steps_per_wvl,
            min_steps_per_sim_size=min_steps_per_sim_size,
            max_scale=max_scale,
            dl_min=dl_min,
            mesher=mesher,
        )
        return cls(
            wavelength=wavelength,
            grid_x=grid_1d,
            grid_y=grid_1d,
            grid_z=grid_1d,
            override_structures=override_structures,
            snapping_points=snapping_points,
            layer_refinement_specs=layer_refinement_specs,
        )

    @classmethod
    def uniform(cls, dl: float) -> GridSpec:
        """Use the same :class:`.UniformGrid` along each of the three directions.

        Parameters
        ----------
        dl : float
            Grid size for uniform grid generation.

        Returns
        -------
        GridSpec
            :class:`.GridSpec` with the same uniform grid size in each direction.
        """

        grid_1d = UniformGrid(dl=dl)
        return cls(grid_x=grid_1d, grid_y=grid_1d, grid_z=grid_1d)

    @classmethod
    def quasiuniform(
        cls,
        dl: float,
        max_scale: pd.PositiveFloat = 1.4,
        override_structures: list[StructureType] = (),
        snapping_points: tuple[CoordinateOptional, ...] = (),
        mesher: MesherType = Undefined,
    ) -> GridSpec:
        """Use the same :class:`.QuasiUniformGrid` along each of the three directions.

        Parameters
        ----------
        dl : float
            Grid size for quasi-uniform grid generation.
        max_scale : pd.PositiveFloat, optional
            Sets the maximum ratio between any two consecutive grid steps.
        override_structures : List[StructureType]
            A list of structures that is added on top of the simulation structures in
            the process of generating the grid. This can be used to snap grid points to
            the bounding box boundary.
        snapping_points : Tuple[CoordinateOptional, ...]
            A set of points that enforce grid boundaries to pass through them.
        mesher : MesherType = GradedMesher()
            The type of mesher to use to generate the grid automatically.

        Returns
        -------
        GridSpec
            :class:`.GridSpec` with the same uniform grid size in each direction.
        """
        if mesher is Undefined:
            mesher = GradedMesher()

        grid_1d = QuasiUniformGrid(dl=dl, max_scale=max_scale, mesher=mesher)
        return cls(
            grid_x=grid_1d,
            grid_y=grid_1d,
            grid_z=grid_1d,
            override_structures=override_structures,
            snapping_points=snapping_points,
        )
