"""Convenience functions for estimating antenna radiation by applying array factor."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, Union

import numpy as np
import pydantic.v1 as pd
from pydantic.v1 import NonNegativeFloat, PositiveInt, conint
from scipy.signal.windows import blackman, blackmanharris, chebwin, hamming, hann, kaiser, taylor
from scipy.special import j0, jn_zeros

from tidy3d.components.base import Tidy3dBaseModel, skip_if_fields_missing
from tidy3d.components.data.monitor_data import AbstractFieldProjectionData, DirectivityData
from tidy3d.components.data.sim_data import SimulationData
from tidy3d.components.geometry.base import Box, Geometry
from tidy3d.components.grid.grid_spec import GridSpec, LayerRefinementSpec
from tidy3d.components.lumped_element import LumpedElement
from tidy3d.components.medium import Medium, MediumType3D
from tidy3d.components.monitor import AbstractFieldProjectionMonitor, MonitorType
from tidy3d.components.simulation import Simulation
from tidy3d.components.source.utils import SourceType
from tidy3d.components.structure import MeshOverrideStructure, Structure
from tidy3d.components.types import TYPE_TAG_STR, ArrayLike, Axis, Bound, Undefined
from tidy3d.constants import C_0, inf
from tidy3d.exceptions import Tidy3dNotImplementedError
from tidy3d.log import log


class AbstractAntennaArrayCalculator(Tidy3dBaseModel, ABC):
    """Abstract base for phased array calculators."""

    taper: Union[RectangularTaper, RadialTaper] = pd.Field(
        None,
        discriminator=TYPE_TAG_STR,
        title="Antenna Array Taper",
        description="Amplitude weighting of array elements to control main lobe width and suppress side lobes.",
    )

    @property
    @abstractmethod
    def _antenna_locations(self) -> ArrayLike:
        """Locations of antennas' centers in an array."""

    @property
    @abstractmethod
    def _antenna_amps(self) -> ArrayLike:
        """Amplitude multipliers of antennas in an array."""

    @property
    @abstractmethod
    def _antenna_phases(self) -> ArrayLike:
        """Phase shifts of antennas in an array."""

    @property
    @abstractmethod
    def _extend_dims(self):
        """Dimensions along which antennas will be duplicated."""

    @property
    def _antenna_nominal_size(self) -> ArrayLike:
        """Size of the antenna array without taking into account size of a single antenna."""
        rmin = np.min(self._antenna_locations, axis=0)
        rmax = np.max(self._antenna_locations, axis=0)

        return rmax - rmin

    @property
    def _antenna_nominal_center(self) -> ArrayLike:
        """Center of the antenna array without taking into account size of a single antenna."""
        rmin = np.min(self._antenna_locations, axis=0)
        rmax = np.max(self._antenna_locations, axis=0)

        return 0.5 * (rmax + rmin)

    def _detect_antenna_bounds(self, simulation: Simulation):
        """Detect the bounds of the antenna in the simulation."""
        # directions in which we will need to tile simulation
        extend_dims = self._extend_dims

        # detect bounding box of all structures, sources, and lumped elements in the simulation
        sim_bounds = np.array(simulation.bounds)
        antenna_bounds = sim_bounds.copy()
        for dim in extend_dims:
            antenna_bounds[0][dim] = inf
            antenna_bounds[1][dim] = -inf

        all_objects = list(simulation.structures)
        all_objects += list(simulation.sources)
        all_objects += list(simulation.lumped_elements)

        for obj in all_objects:
            # get bounding box of the object
            if isinstance(obj, Structure):
                obj_bounds = np.array(obj.geometry.bounds)
            else:
                obj_bounds = np.array(obj.bounds)

            for dim in extend_dims:
                # update minimum and maximum bounds in each dimension
                # check if object extends beyond the simulation bounds on both sides
                extends_beyond_min = obj_bounds[0][dim] < sim_bounds[0][dim]
                extends_beyond_max = obj_bounds[1][dim] > sim_bounds[1][dim]
                if extends_beyond_min or extends_beyond_max:
                    # in case of a box, we just ignore it, since we will be able to extend it later
                    if (
                        isinstance(obj, Structure)
                        and isinstance(obj.geometry, Box)
                        and extends_beyond_min
                        and extends_beyond_max
                    ):
                        continue
                    # otherwise shrink the object bounds to simulation bounds
                    obj_bounds[0][dim] = max(obj_bounds[0][dim], sim_bounds[0][dim])
                    obj_bounds[1][dim] = min(obj_bounds[1][dim], sim_bounds[1][dim])
                    # and show a warning
                    log.warning(
                        f"Object {obj.name} (type: {obj.type}) extends beyond simulation bounds along"
                        f" '{'xyz'[dim]}' axis. Please check your antenna setup for correctness."
                    )
                # update minimum and maximum bounds in each dimension
                antenna_bounds[0][dim] = min(antenna_bounds[0][dim], obj_bounds[0][dim])
                antenna_bounds[1][dim] = max(antenna_bounds[1][dim], obj_bounds[1][dim])

        return antenna_bounds

    def _try_to_expand_geometry(
        self, geometry: Geometry, old_sim_bounds: Bound, new_sim_bounds: Bound
    ):
        """Try to expand geometry to cover the entire simulation domain."""

        can_expand = isinstance(geometry, Box) and all(
            geometry.bounds[0][dim] < old_sim_bounds[0][dim]
            or geometry.bounds[1][dim] > old_sim_bounds[1][dim]
            for dim in self._extend_dims
        )

        if not can_expand:
            return None  # could not expand geometry, so we will duplicate

        # get original structure bounds
        box_bounds = np.array(geometry.bounds)
        box_size = np.array(geometry.size)
        box_center = np.array(geometry.center)

        for dim in self._extend_dims:
            # if it extends beyond simulation bounds, but size is not inf
            # we will adjust it so that it goes out of bounds by the same amount as in the initial simulation.
            # No need to do anything if size is inf.
            if box_size[dim] != np.inf:
                # shift min bounds to new location
                box_bounds[0][dim] = new_sim_bounds[0][dim] + (
                    box_bounds[0][dim] - old_sim_bounds[0][dim]
                )

                # shift max bounds to new location
                box_bounds[1][dim] = new_sim_bounds[1][dim] - (
                    old_sim_bounds[1][dim] - box_bounds[1][dim]
                )

                # calculate new structure size and center
                box_size[dim] = box_bounds[1][dim] - box_bounds[0][dim]
                box_center[dim] = 0.5 * (box_bounds[0][dim] + box_bounds[1][dim])

        return geometry.updated_copy(
            center=tuple(box_center),
            size=tuple(box_size),
        )

    def _duplicate_or_expand_list_of_objects(
        self,
        objects: tuple[
            Union[Structure, MeshOverrideStructure, LayerRefinementSpec, LumpedElement], ...
        ],
        old_sim_bounds: Bound,
        new_sim_bounds: Bound,
    ):
        """Duplicate or expand a list of objects."""

        locations = self._antenna_locations

        array_objects = []
        for obj in objects:
            if isinstance(obj, (Structure, MeshOverrideStructure)):
                geometry = obj.geometry
                if isinstance(obj, Structure) and obj.medium.is_custom:
                    log.warning(
                        f"Object '{obj.name}' contains a custom medium which has limited support "
                        "in automatic antenna array generation. The custom medium's spatial distribution "
                        "will remain fixed and will not be translated along with the structure geometry."
                    )
            elif isinstance(obj, (LayerRefinementSpec, LumpedElement)):
                geometry = obj
            else:
                raise ValueError(f"Object of type {type(obj)} is not supported.")

            # check if it is a box and extends beyond simulation bounds
            expanded_geometry = self._try_to_expand_geometry(
                geometry=geometry, old_sim_bounds=old_sim_bounds, new_sim_bounds=new_sim_bounds
            )

            if expanded_geometry is None:
                # could not expand geometry, so we duplicate
                for ind, translation_vector in enumerate(locations):
                    if isinstance(obj, Structure):
                        new_obj = obj.updated_copy(
                            geometry=obj.geometry.translated(*translation_vector),
                            name=None if obj.name is None else f"{obj.name}_{ind}",
                        )
                    elif isinstance(obj, MeshOverrideStructure):
                        new_obj = obj.updated_copy(
                            geometry=obj.geometry.translated(*translation_vector).bounding_box,
                            name=None if obj.name is None else f"{obj.name}_{ind}",
                        )
                    elif isinstance(obj, LayerRefinementSpec):
                        new_obj = obj.updated_copy(
                            center=tuple(obj.center + translation_vector),
                        )
                    elif isinstance(obj, LumpedElement):
                        new_obj = obj.updated_copy(
                            center=tuple(obj.center + translation_vector),
                            name=None if obj.name is None else f"{obj.name}_{ind}",
                        )
                    array_objects.append(new_obj)
            else:
                # could expand geometry, so we create a copy of the original object with updated size and center
                if isinstance(obj, (Structure, MeshOverrideStructure)):
                    new_obj = obj.updated_copy(
                        geometry=expanded_geometry,
                    )
                elif isinstance(obj, (LayerRefinementSpec, LumpedElement)):
                    new_obj = expanded_geometry

                # add the new object to the list of objects
                array_objects.append(new_obj)

        return array_objects

    def _expand_monitors(
        self,
        monitors: tuple[MonitorType, ...],
        antenna_bounds: Bound,
        new_sim_bounds: Bound,
        old_sim_bounds: Bound,
    ):
        """Expand monitors."""

        extend_dims = self._extend_dims

        # expand far-field monitors
        array_monitors = []
        for monitor in monitors:
            # we only expand field projection monitors
            if isinstance(monitor, AbstractFieldProjectionMonitor):
                # get original monitor bounds
                mnt_bounds = np.array(monitor.bounds)
                mnt_size = np.array(monitor.size)
                mnt_center = np.array(monitor.center)

                if any(mnt_size[dim] == 0 for dim in extend_dims):
                    log.warning(
                        f"Monitor '{monitor.name}' (type: '{monitor.type}') has zero size along "
                        f"one of the axes. It will not be included in the resulting simulation."
                    )
                    continue

                for dim in extend_dims:
                    if mnt_size[dim] != np.inf:
                        # check that monitor covers the estimated antenna box
                        if (
                            mnt_bounds[0][dim] > antenna_bounds[0][dim]
                            or mnt_bounds[1][dim] < antenna_bounds[1][dim]
                        ):
                            log.warning(
                                f"Monitor '{monitor.name}' (type: '{monitor.type}') does not cover "
                                f"the estimated antenna box along '{'xyz'[dim]}' axis. "
                                "The automatically extended monitor will likely be wrong. "
                                "Please double check the resulting simulation."
                            )
                        # shift min bounds to new location
                        mnt_bounds[0][dim] = new_sim_bounds[0][dim] + (
                            mnt_bounds[0][dim] - old_sim_bounds[0][dim]
                        )

                        # shift max bounds to new location
                        mnt_bounds[1][dim] = new_sim_bounds[1][dim] - (
                            old_sim_bounds[1][dim] - mnt_bounds[1][dim]
                        )

                        # calculate new monitor size and center
                        mnt_size[dim] = mnt_bounds[1][dim] - mnt_bounds[0][dim]
                        mnt_center[dim] = 0.5 * (mnt_bounds[0][dim] + mnt_bounds[1][dim])

                # create a copy of the original monitor with updated size and center
                new_mnt = monitor.updated_copy(
                    center=tuple(mnt_center),
                    size=tuple(mnt_size),
                )

                # add the new monitor to the list of monitors
                array_monitors.append(new_mnt)

            # otherwise we ignore and warn the user
            else:
                log.warning(
                    f"Monitor '{monitor.name}' (type: '{monitor.type}') will not be automatically "
                    "transferred into the resulting antenna array simulation."
                )

        return array_monitors

    def _duplicate_structures(
        self, structures: tuple[Structure, ...], new_sim_bounds: Bound, old_sim_bounds: Bound
    ):
        """Duplicate structures."""

        return self._duplicate_or_expand_list_of_objects(
            objects=structures, old_sim_bounds=old_sim_bounds, new_sim_bounds=new_sim_bounds
        )

    def _duplicate_sources(
        self,
        sources: tuple[SourceType, ...],
        lumped_elements: tuple[LumpedElement, ...],
        old_sim_bounds: Bound,
        new_sim_bounds: Bound,
    ):
        """Duplicate sources and lumped elements."""
        array_lumped_elements = self._duplicate_or_expand_list_of_objects(
            objects=lumped_elements, old_sim_bounds=old_sim_bounds, new_sim_bounds=new_sim_bounds
        )

        array_sources = []
        for ind, (translation_vector, phase_shift, amp_multiplier) in enumerate(
            zip(self._antenna_locations, self._antenna_phases, self._antenna_amps)
        ):
            if amp_multiplier != 0.0:
                for source in sources:
                    new_source = source.updated_copy(
                        center=tuple(source.center + translation_vector),
                        name=f"{source.name}_{ind}",
                        source_time=source.source_time.updated_copy(
                            phase=source.source_time.phase + phase_shift,
                            amplitude=source.source_time.amplitude * amp_multiplier,
                        ),
                    )
                    array_sources.append(new_source)

        return array_sources, array_lumped_elements

    def _duplicate_grid_specs(
        self, grid_spec: GridSpec, old_sim_bounds: Bound, new_sim_bounds: Bound
    ):
        """Duplicate grid specs."""

        array_overrides = self._duplicate_or_expand_list_of_objects(
            objects=grid_spec.override_structures,
            old_sim_bounds=old_sim_bounds,
            new_sim_bounds=new_sim_bounds,
        )
        array_layer_refinement_specs = self._duplicate_or_expand_list_of_objects(
            objects=grid_spec.layer_refinement_specs,
            old_sim_bounds=old_sim_bounds,
            new_sim_bounds=new_sim_bounds,
        )

        array_snapping_points = []
        for translation_vector in self._antenna_locations:
            for snapping_point in grid_spec.snapping_points:
                new_snapping_point = [
                    snapping_point[dim] + translation_vector[dim]
                    if snapping_point[dim] is not None
                    else None
                    for dim in range(3)
                ]
                array_snapping_points.append(new_snapping_point)

        return grid_spec.updated_copy(
            override_structures=array_overrides,
            layer_refinement_specs=array_layer_refinement_specs,
            snapping_points=array_snapping_points,
        )

    def make_antenna_array(self, simulation: Simulation) -> Simulation:
        """
        Converts a single antenna simulation into an antenna array simulation.
        This function identifies the size and position of the single antenna
        in the input simulation and uses this information to compute the dimensions
        of the resulting antenna array simulation. All structures, sources, lumped elements,
        and mesh override structures are duplicated, while monitors are extended in size.
        Only projection monitors are transferred into the resulting simulation.

        For best results, the antenna assembly should be contained within the simulation bounds.

        Parameters:
        ----------
        simulation : Simulation
            The simulation specification describing a single antenna setup.

        Returns:
        --------
        Simulation
            The simulation specification describing the antenna array.
        """

        # detect bounding box of all structures, sources, and lumped elements in the simulation
        sim_bounds = np.array(simulation.bounds)
        antenna_bounds = self._detect_antenna_bounds(simulation)

        # compute the center and size of the antenna
        antenna_size = antenna_bounds[1] - antenna_bounds[0]
        antenna_center = 0.5 * (antenna_bounds[0] + antenna_bounds[1])

        # compute buffer between the antenna and simulation bounds on each side
        buffer_min = antenna_bounds[0] - sim_bounds[0]
        buffer_max = sim_bounds[1] - antenna_bounds[1]

        # compute total size of the antenna array in x, y, and z directions
        antenna_array_size = self._antenna_nominal_size + antenna_size

        new_sim_bounds = [
            antenna_center + self._antenna_nominal_center - antenna_array_size / 2 - buffer_min,
            antenna_center + self._antenna_nominal_center + antenna_array_size / 2 + buffer_max,
        ]

        # compute the total size of the simulation domain
        new_sim_size = new_sim_bounds[1] - new_sim_bounds[0]
        new_sim_center = 0.5 * (new_sim_bounds[0] + new_sim_bounds[1])

        # duplicate structures, sources, lumped elements, and override structures
        array_structures = self._duplicate_structures(
            structures=simulation.structures,
            new_sim_bounds=new_sim_bounds,
            old_sim_bounds=sim_bounds,
        )
        array_sources, array_lumped_elements = self._duplicate_sources(
            sources=simulation.sources,
            lumped_elements=simulation.lumped_elements,
            old_sim_bounds=sim_bounds,
            new_sim_bounds=new_sim_bounds,
        )
        array_monitors = self._expand_monitors(
            monitors=simulation.monitors,
            antenna_bounds=antenna_bounds,
            new_sim_bounds=new_sim_bounds,
            old_sim_bounds=sim_bounds,
        )
        array_grid_spec = self._duplicate_grid_specs(
            grid_spec=simulation.grid_spec, old_sim_bounds=sim_bounds, new_sim_bounds=new_sim_bounds
        )

        new_sim = simulation.updated_copy(
            center=tuple(new_sim_center),
            size=tuple(new_sim_size),
            structures=array_structures,
            monitors=array_monitors,
            sources=array_sources,
            lumped_elements=array_lumped_elements,
            grid_spec=array_grid_spec,
        )

        return new_sim

    @abstractmethod
    def array_factor(
        self,
        theta: Union[float, ArrayLike],
        phi: Union[float, ArrayLike],
        frequency: Union[NonNegativeFloat, ArrayLike],
    ) -> ArrayLike:
        """
        Compute the array factor for an antenna array.

        Parameters:
        -----------
        theta : Union[float, ArrayLike]
            Observation angles in the elevation plane (in radians).
        phi : Union[float, ArrayLike]
            Observation angles in the azimuth plane (in radians).
        frequency : Union[NonNegativeFloat, ArrayLike]
            Signal frequency (in Hz).

        Returns:
        --------
        ArrayLike
            Array factor values for each combination of theta and phi.
        """

    def monitor_data_from_array_factor(
        self,
        monitor_data: AbstractFieldProjectionData,
        new_monitor: AbstractFieldProjectionMonitor = None,
    ) -> AbstractFieldProjectionData:
        """Apply the array factor to the monitor data of a single antenna.

        Parameters
        ----------
        monitor_data : AbstractFieldProjectionData
            The monitor data of a single antenna.
        new_monitor : AbstractFieldProjectionMonitor = None
            The new monitor to be used in the resulting data.

        Returns
        -------
        AbstractFieldProjectionData
            The monitor data of the antenna array.
        """

        # Get spherical coordinates
        r, theta, phi = list(monitor_data.coords_spherical.values())
        freqs = monitor_data.f
        coords_shape = list(np.shape(r))
        coords_shape.append(len(freqs))

        # Compute the array factor
        af = self.array_factor(theta.ravel(), phi.ravel(), freqs, monitor_data.medium)
        af = np.reshape(af, coords_shape)

        update_dict = {}

        # Apply the array factor to the monitor data
        for key, field in monitor_data.field_components.items():
            update_dict[key] = field.copy() * af

        if new_monitor is not None:
            monitor = new_monitor
        else:
            monitor = monitor_data.monitor

        update_dict["monitor"] = monitor
        update_dict["projection_surfaces"] = monitor.projection_surfaces

        if isinstance(monitor_data, DirectivityData):
            # Attempt to recompute flux
            try:
                update_dict["flux"] = monitor_data.flux_from_projected_fields()
            except ValueError as e:
                log.warning(
                    "Could not recalculate flux for a 'DirectivityData' due to the following "
                    f"reason: {e} This monitor will not be included in the resulting data."
                )
                return None

        # Create a new monitor data with the updated fields
        new_mnt_data = monitor_data.updated_copy(
            **update_dict,
        )

        return new_mnt_data

    def simulation_data_from_array_factor(
        self,
        antenna_data: SimulationData,
    ) -> SimulationData:
        """
        Computes the far-field data of a rectangular antenna array based on the far-field data of
        a single antenna. Additionaly, it automatically converts a single antenna simulation setup
        into the corresponding antenna array simulation setup.

        Note that any near-field monitor data will be ignored.

        Parameters
        ----------
        antenna_data : SimulationData
            The far-field data of a single antenna.

        Returns
        -------
        SimulationData
            The far-field data of the antenna array.
        """

        # create an expanded simulation for reference
        sim_array = self.make_antenna_array(antenna_data.simulation)

        # names of transferred monitors
        mnt_dict = {mnt.name: mnt for mnt in sim_array.monitors}

        # process far field data
        data_array = []
        good_monitors = []
        for mnt_data in antenna_data.data:
            mnt_name = mnt_data.monitor.name
            if mnt_name in mnt_dict:
                array_mnt_data = self.monitor_data_from_array_factor(
                    monitor_data=mnt_data,
                    new_monitor=mnt_dict[mnt_name],
                )
                if array_mnt_data is not None:
                    good_monitors.append(mnt_dict[mnt_name])
                    data_array.append(array_mnt_data)

        return SimulationData(
            simulation=sim_array.updated_copy(monitors=good_monitors), data=data_array
        )

    @pd.root_validator(pre=False)
    def _warn_rf_license(cls, values):
        log.warning(
            "ℹ️ ⚠️ RF simulations are subject to new license requirements in the future. You have instantiated at least one RF-specific component.",
            log_once=True,
        )
        return values

    def _rect_taper_array_factor(
        self, exp_x: ArrayLike, exp_y: ArrayLike, exp_z: ArrayLike
    ) -> ArrayLike:
        """
        Compute the array factor assuming a separable rectangular (Cartesian) taper.

        This method evaluates the array factor using separable amplitude weights
        along the x, y, and z dimensions.

        Parameters
        ----------
        exp_x: ArrayLike
            3D array of phases along x axis [N_x, N_theta, N_freq].
        exp_y: ArrayLike
            3D array of phases along x axis [N_y, N_theta, N_freq].
        exp_z: ArrayLike
            3D array of phases along x axis [N_z, N_theta, N_freq].

        Returns
        -------
        ArrayLike
            Array factor values for each combination of theta and phi.
        """

        # if taper is not defined set all amplitudes to 1.0
        if self.taper is None:
            amp_x = (
                1.0 if self.amp_multipliers[0] is None else self.amp_multipliers[0][:, None, None]
            )
            amp_y = (
                1.0 if self.amp_multipliers[1] is None else self.amp_multipliers[1][:, None, None]
            )
            amp_z = (
                1.0 if self.amp_multipliers[2] is None else self.amp_multipliers[2][:, None, None]
            )

        # if rectangular taper is spacified
        elif isinstance(self.taper, RectangularTaper):
            # get amplitudes along x, y and z axes
            amp_x, amp_y, amp_z = self.taper.amp_multipliers(self.array_size)

            # broadcast amplitudes to [N_x,1,1], [N_y,1,1] and [Nz,1,1], respectively
            amp_x = amp_x[:, None, None]
            amp_y = amp_y[:, None, None]
            amp_z = amp_z[:, None, None]

        # Tapers with non-separable amplitude weights are not supported by this function
        else:
            raise ValueError(f"Unsupported taper type {type(self.taper)} was passed.")

        # Calculate individual array factors in x, y, and z directions
        af_x = np.sum(
            amp_x * exp_x,
            axis=0,
        )
        af_y = np.sum(
            amp_y * exp_y,
            axis=0,
        )
        af_z = np.sum(
            amp_z * exp_z,
            axis=0,
        )

        # Calculate the overall array factor
        array_factor = af_x * af_y * af_z

        return array_factor

    def _general_taper_array_factor(
        self, exp_x: ArrayLike, exp_y: ArrayLike, exp_z: ArrayLike
    ) -> ArrayLike:
        """
        Compute the array factor assuming a non-separable (non-Cartesian) taper.

        This method evaluates the array factor using non-separable amplitude weights
        along the x, y, and z dimensions.

        Parameters
        ----------
        exp_x: ArrayLike
            3D array of phases along x axis [N_x, N_theta, N_freq].
        exp_y: ArrayLike
            3D array of phases along x axis [N_y, N_theta, N_freq].
        exp_z: ArrayLike
            3D array of phases along x axis [N_z, N_theta, N_freq].

        Returns
        -------
        ArrayLike
            Array factor values for each combination of theta / phi and frequency.
        """
        # get taper weights
        amps = self.taper.amp_multipliers(self.array_size)

        # ensure amplitude weights are in format tuple[ArrayLike, ]
        if len(amps) != 1:
            raise ValueError(
                "Non-cartesian taper was expected. Please ensure a valid taper is used."
            )

        # compute array factor: AF(theta,f) = sum_{x,y,z} amp(x,y,z) * exp_x(x,theta,f)*exp_y(y,theta,f)*exp_z(z,theta,f)
        array_factor = np.einsum("xpf,ypf,zpf,xyz->pf", exp_x, exp_y, exp_z, amps[0])

        return array_factor


class RectangularAntennaArrayCalculator(AbstractAntennaArrayCalculator):
    """This class provides methods to calculate the array factor and far-field radiation patterns
    for rectangular phased antenna arrays. It handles arrays with arbitrary size, spacing,
    phase shifts, and amplitude tapering in x, y, and z directions.

    Notes
    -----

    The array factor is calculated using the standard array factor formula for rectangular arrays,
    which accounts for the spatial distribution of antennas and their relative phases and amplitudes.
    This can be used to analyze beam steering, sidelobe levels, and other array characteristics.

    In addition, this class provides a convenience method to create an antenna array simulation
    from a single antenna simulation. This can be used to compute the behavior (near-field and/or
    far-field) of the full antenna array directly without any approximations. Such a simulation setup
    can be obtained by directly calling the `make_antenna_array` function, or by accessing the field `.simulation`
    of the :class:`SimulationData` object returned by the `simulation_data_from_array_factor` method.

    Example:
    --------
    >>> array_calculator = RectangularAntennaArrayCalculator(
    ...    array_size=(3, 4, 5),
    ...    spacings=(0.5, 0.5, 0.5),
    ...    phase_shifts=(0, 0, 0),
    ... ) # doctest: +SKIP
    """

    array_size: tuple[PositiveInt, PositiveInt, PositiveInt] = pd.Field(
        title="Array Size",
        description="Number of antennas along x, y, and z directions.",
    )

    spacings: tuple[NonNegativeFloat, NonNegativeFloat, NonNegativeFloat] = pd.Field(
        title="Antenna Spacings",
        description="Center-to-center spacings between antennas along x, y, and z directions.",
    )

    phase_shifts: tuple[float, float, float] = pd.Field(
        (0, 0, 0),
        title="Phase Shifts",
        description="Phase-shifts between antennas along x, y, and z directions.",
    )

    amp_multipliers: tuple[Optional[ArrayLike], Optional[ArrayLike], Optional[ArrayLike]] = (
        pd.Field(
            (None, None, None),
            title="Amplitude Multipliers",
            description="Amplitude multipliers spatially distributed along x, y, and z directions.",
        )
    )

    @pd.validator("amp_multipliers", pre=True, always=True)
    @skip_if_fields_missing(["array_size"])
    def _check_amp_multipliers(cls, val, values):
        """Check that the length of the amplitude multipliers is equal to the array size along each dimension."""
        array_size = values.get("array_size")
        if len(val) != 3:
            raise ValueError("'amp_multipliers' must have 3 elements.")
        if val[0] is not None and len(val[0]) != array_size[0]:
            raise ValueError(
                f"'amp_multipliers' has length of {len(val[0])} along the x direction, but the array size is {array_size[0]}."
            )
        if val[1] is not None and len(val[1]) != array_size[1]:
            raise ValueError(
                f"'amp_multipliers' has length of {len(val[1])} along the y direction, but the array size is {array_size[1]}."
            )
        if val[2] is not None and len(val[2]) != array_size[2]:
            raise ValueError(
                f"'amp_multipliers' has length of {len(val[2])} along the z direction, but the array size is {array_size[2]}."
            )
        return val

    @property
    def _antenna_locations(self) -> ArrayLike:
        """Locations of antennas' centers in an array."""

        x = (np.arange(self.array_size[0]) - (self.array_size[0] - 1) / 2) * self.spacings[0]
        y = (np.arange(self.array_size[1]) - (self.array_size[1] - 1) / 2) * self.spacings[1]
        z = (np.arange(self.array_size[2]) - (self.array_size[2] - 1) / 2) * self.spacings[2]

        X, Y, Z = np.meshgrid(x, y, z, indexing="ij")

        return np.transpose([X.ravel(), Y.ravel(), Z.ravel()])

    @property
    def _antenna_amps(self) -> ArrayLike:
        """Amplitude multipliers of antennas in an array."""

        if self.taper is not None:
            if isinstance(self.taper, RectangularTaper):
                amp_x, amp_y, amp_z = self.taper.amp_multipliers(self.array_size)

                # broadcast amplitudes to [N_x,1,1], [N_y,1,1] and [Nz,1,1], respectively
                amp_x = amp_x[:, None, None]
                amp_y = amp_y[None, :, None]
                amp_z = amp_z[None, None, :]

                amps = amp_x * amp_y * amp_z

            else:
                amps = self.taper.amp_multipliers(self.array_size)

            return np.ravel(amps)

        amps_per_dim = [
            np.ones(size) if multiplier is None else multiplier
            for multiplier, size in zip(self.amp_multipliers, self.array_size)
        ]

        amps_grid = np.meshgrid(*amps_per_dim, indexing="ij")

        return np.ravel(amps_grid[0] * amps_grid[1] * amps_grid[2])

    @property
    def _antenna_phases(self) -> ArrayLike:
        """Phase shifts of antennas in an array."""

        phase_shifts_per_dim = [
            np.arange(self.array_size[dim]) * self.phase_shifts[dim] for dim in range(3)
        ]

        phase_shifts_grid = np.meshgrid(*phase_shifts_per_dim, indexing="ij")

        return np.ravel(sum(p for p in phase_shifts_grid))

    @property
    def _extend_dims(self) -> tuple[Axis, ...]:
        """Dimensions along which antennas will be duplicated."""
        return [ind for ind, size in enumerate(self.array_size) if size > 1]

    def array_factor(
        self,
        theta: Union[float, ArrayLike],
        phi: Union[float, ArrayLike],
        frequency: Union[NonNegativeFloat, ArrayLike],
        medium: MediumType3D = Undefined,
    ) -> ArrayLike:
        """
        Compute the array factor for a 3D antenna array.

        Parameters
        ----------
        theta : Union[float, ArrayLike]
            Observation angles in the elevation plane (in radians).
        phi : Union[float, ArrayLike]
            Observation angles in the azimuth plane (in radians).
        frequency : Union[NonNegativeFloat, ArrayLike]
            Signal frequency (in Hz).

        Returns
        -------
        ArrayLike
            Array factor values for each combination of azimuth and zenith angles.
        """
        if medium is Undefined:
            medium = Medium()

        # Convert all inputs to numpy arrays
        theta_array = np.atleast_1d(theta)
        phi_array = np.atleast_1d(phi)

        # ensure that theta and phi have the same length
        if len(theta_array) != len(phi_array):
            raise ValueError("'theta' and 'phi' must have the same length.")

        # reshape inputs for easier broadcasting
        theta_array = np.reshape(theta_array, (len(theta_array), 1))
        phi_array = np.reshape(phi_array, (len(phi_array), 1))
        f_array = np.reshape(frequency, (1, len(np.atleast_1d(frequency))))

        eps_complex = np.array(medium.eps_model(f_array))

        wavelength = C_0 / f_array / np.sqrt(eps_complex)
        k = 2 * np.pi / wavelength  # Wavenumber

        # Calculate the phase shift in the x, y, and z directions
        psi_x = (
            k * self.spacings[0] * np.sin(theta_array) * np.cos(phi_array) - self.phase_shifts[0]
        )
        psi_y = (
            k * self.spacings[1] * np.sin(theta_array) * np.sin(phi_array) - self.phase_shifts[1]
        )
        psi_z = k * self.spacings[2] * np.cos(theta_array) - self.phase_shifts[2]

        # Calculate resulting complex exponentials
        exp_x = np.exp(-1j * np.arange(self.array_size[0])[:, None, None] * psi_x[np.newaxis, :])
        exp_y = np.exp(-1j * np.arange(self.array_size[1])[:, None, None] * psi_y[np.newaxis, :])
        exp_z = np.exp(-1j * np.arange(self.array_size[2])[:, None, None] * psi_z[np.newaxis, :])

        # Compute array factor based on the defined taper
        if self.taper is None or isinstance(self.taper, RectangularTaper):
            return self._rect_taper_array_factor(exp_x, exp_y, exp_z)
        else:
            return self._general_taper_array_factor(exp_x, exp_y, exp_z)


class AbstractWindow(Tidy3dBaseModel, ABC):
    """This class provides interface for window selection."""

    def _get_weights_discrete(self, N: int) -> ArrayLike:
        """Interface function for computing window weights at N points."""
        raise Tidy3dNotImplementedError(
            f"Calculation of antenna amplitudes at a discrete number of points is not yet implemented for window type {self.type}."
        )

    def _get_weights_continuous(self, p_vec: ArrayLike) -> ArrayLike:
        """Interface function for computing window weights at given locations."""
        raise Tidy3dNotImplementedError(
            f"Calculation of antenna amplitudes at arbitrary locations is not yet implemented for window type {self.type}."
        )


class HammingWindow(AbstractWindow):
    """Standard Hamming window for tapering or spectral shaping."""

    def _get_weights_discrete(self, N: int) -> ArrayLike:
        """
        Generate a 1D Hamming window of length N.

        Parameters
        ----------
        N : int
            Number of points in the window.

        Returns
        -------
        ArrayLike
            1D array of Hamming window weights.
        """
        return hamming(N)


class BlackmanWindow(AbstractWindow):
    """Standard Blackman window for tapering or spectral shaping."""

    def _get_weights_discrete(self, N: int) -> ArrayLike:
        """
        Generate a 1D Blackman window of length N.

        Parameters
        ----------
        N : int
            Number of points in the window.

        Returns
        -------
        ArrayLike
            1D array of Blackman window weights.
        """
        return blackman(N)


class BlackmanHarrisWindow(AbstractWindow):
    """Standard Blackman-Harris window for tapering or spectral shaping."""

    def _get_weights_discrete(self, N: int) -> ArrayLike:
        """
        Generate a 1D Blackman-Harris window of length N.

        Parameters
        ----------
        N : int
            Number of points in the window.

        Returns
        -------
        ArrayLike
            1D array of Blackman-Harris window weights.
        """
        return blackmanharris(N)


class HannWindow(AbstractWindow):
    """Hann window with configurable sidelobe suppression and sidelobe count."""

    def _get_weights_discrete(self, N: int) -> ArrayLike:
        """
        Generate a 1D Hann window of length N.

        Parameters
        ----------
        N : int
            Number of points in the window.

        Returns
        -------
        ArrayLike
            1D array of Hann window weights.
        """
        return hann(N)


class ChebWindow(AbstractWindow):
    """Standard Chebyshev window for tapering with configurable sidelobe attenuation."""

    attenuation: pd.PositiveFloat = pd.Field(
        default=30,
        title="Attenuation",
        description="Desired attenuation level of sidelobes.",
        units="dB",
    )

    def _get_weights_discrete(self, N: int) -> ArrayLike:
        """
        Generate a 1D Chebyshev window of length N.

        Parameters
        ----------
        N : int
            Number of points in the window.

        Returns
        -------
        ArrayLike
            1D array of Chebyshev window weights.
        """
        return chebwin(N, self.attenuation)


class KaiserWindow(AbstractWindow):
    """Class for Kaiser window."""

    beta: pd.NonNegativeFloat = pd.Field(
        ...,
        title="Shape Parameter",
        description="Shape parameter, determines trade-off between main-lobe width and side lobe level.",
    )

    def _get_weights_discrete(self, N: int) -> ArrayLike:
        """
        Generate a 1D Kaiser window of length N.

        Parameters
        ----------
        N : int
            Number of points in the window.

        Returns
        -------
        ArrayLike
            1D array of Kaiser window weights.
        """
        return kaiser(N, self.beta)


class TaylorWindow(AbstractWindow):
    """Taylor window with configurable sidelobe suppression and sidelobe count."""

    sll: pd.PositiveFloat = pd.Field(
        default=30,
        title="Sidelobe Suppression Level",
        description="Desired suppression of sidelobe level relative to the DC gain.",
        units="dB",
    )

    nbar: conint(gt=0, le=10) = pd.Field(
        default=4,
        title="Number of Nearly Constant Sidelobes",
        description="Number of nearly constant level sidelobes adjacent to the mainlobe.",
    )

    def _get_weights_discrete(self, N):
        """
        Generate a 1D Taylor window of length N.

        Parameters
        ----------
        N : int
            Number of points in the window.

        Returns
        -------
        ArrayLike
            1D array of Taylor window weights.
        """
        return taylor(N, self.nbar, self.sll)

    def _get_exp_weights(self, mus: np.ndarray):
        """
        Compute expansion coefficients B_l for the circular Taylor taper.

        The aperture field E_a(p) is represented as a sum over Bessel functions:
            E_a(p) ≈ 1 + sum_l B_l * J0(mu_l * p)

        where mu_l are the zeros of J1(pi * mu), and B_l are the expansion coefficients
        chosen to enforce a specified sidelobe level (sll) via the Taylor design method.

        Parameters:
        -----------
        mus : np.ndarray
            Roots of J1(pi * mu) / pi (used to construct the Bessel function basis).

        Returns:
        --------
        B : np.ndarray
            Expansion coefficients (1D array of shape (nbar - 1,)).
        """

        # calculate real-valued parameter from sidelobe attenuation level
        A = np.arccosh(10 ** (self.sll / 20)) / np.pi
        sigma = mus[-1] / np.sqrt(A**2 + (self.nbar - 0.5) ** 2)

        u = np.sqrt(A**2 + (np.arange(1, self.nbar) - 0.5) ** 2)
        B = np.zeros(self.nbar - 1)

        for i in range(self.nbar - 1):
            mu_i_sq = mus[i] ** 2

            # Numerator: product over (1 - mu_i^2 / (sigma * u_n)^2)
            num_terms = 1 - mu_i_sq / (sigma * u) ** 2
            num = np.prod(num_terms)

            # Denominator
            denom_terms = [1 - mu_i_sq / mus[n] ** 2 for n in range(self.nbar - 1) if n != i]
            denom = np.prod(denom_terms)
            B[i] = -num / (denom * j0(np.pi * mus[i]))

        return B

    def _get_weights_continuous(self, p_vec: ArrayLike) -> ArrayLike:
        """
        Sample weights from the circular Taylor taper at specified radial positions.

        Parameters
        ----------
        p_vec : ArrayLike
            1D array of radial sampling points in the range [0, π].

        Returns
        -------
        g_p_norm : ArrayLike
            1D array of Taylor taper weights evaluated at the points in ``p_vec``.
        """

        # get locations J1(np.pi * mu)=0
        mus = jn_zeros(1, self.nbar) / np.pi

        B_m = self._get_exp_weights(mus=mus)

        J = j0(np.outer(mus[0:-1], p_vec))

        g_p = 1 + B_m @ J

        return g_p


# define a list of acceptable rectangular windows
RectangularWindowType = Union[
    HammingWindow,
    HannWindow,
    KaiserWindow,
    TaylorWindow,
    ChebWindow,
    BlackmanWindow,
    BlackmanHarrisWindow,
]


class AbstractTaper(Tidy3dBaseModel, ABC):
    """Abstract taper class provides an interface for taper of Array antennas."""

    @abstractmethod
    def amp_multipliers(
        self, array_size: tuple[PositiveInt, PositiveInt, PositiveInt]
    ) -> tuple[np.ndarray, ...]:
        """
        Compute taper amplitudes for phased array antennas.

        Parameters:
        ----------
        array_size: tuple[PositiveInt, PositiveInt, PositiveInt]
            A tuple of array size along x,y, and z axes.
        """


class RectangularTaper(AbstractTaper):
    """Class for rectangular taper."""

    window_x: Optional[RectangularWindowType] = pd.Field(
        None,
        title="X Axis Window",
        description="Window type used to taper array antenna along x axis.",
        discriminator=TYPE_TAG_STR,
    )

    window_y: Optional[RectangularWindowType] = pd.Field(
        None,
        title="Y Axis Window",
        description="Window type used to taper array antenna along y axis.",
        discriminator=TYPE_TAG_STR,
    )

    window_z: Optional[RectangularWindowType] = pd.Field(
        None,
        title="Z Axis Window",
        description="Window type used to taper array antenna along z axis.",
        discriminator=TYPE_TAG_STR,
    )

    @classmethod
    def from_isotropic_window(cls, window: RectangularWindowType) -> RectangularTaper:
        """
        Set the same window along x, y, and z dimensions.

        Parameters
        ----------
        window: RectangularWindowType
            A supported 1D window type from ``RectangularWindowType``.

        Returns
        -------
        RectangularTaper
            A ``RectangularTaper`` instance with all three dimensions set to the specified window.
        """
        return cls(window_x=window, window_y=window, window_z=window)

    @pd.root_validator
    def check_at_least_one_window(cls, values):
        if not any([values.get("window_x"), values.get("window_y"), values.get("window_z")]):
            raise ValueError("At least one window (x, y, or z) must be provided.")
        return values

    def amp_multipliers(
        self, array_size: tuple[PositiveInt, PositiveInt, PositiveInt]
    ) -> tuple[ArrayLike, ArrayLike, ArrayLike]:
        """
        Method ``amp_multipliers()`` computes rectangular taper amplitude for phased array antennas.

        Parameters:
        ----------
        array_size: tuple[PositiveInt, PositiveInt, PositiveInt]
            A tuple of array size along x,y, and z axes.

        Returns:
        --------
        tuple[ArrayLike, ArrayLike, ArrayLike]
            a tuple of three 1D numpy arrays with taper amplitudes along x,y, and z axes.
        """

        effective_size = tuple(dim if dim is not None else 1 for dim in array_size)

        amps = (
            window._get_weights_discrete(effective_size[ind])
            if window is not None
            else np.ones(effective_size[ind])
            for ind, window in enumerate([self.window_x, self.window_y, self.window_z])
        )

        return amps


class RadialTaper(AbstractTaper):
    """Class for Radial Taper."""

    window: TaylorWindow = pd.Field(
        ..., title="Window Object", description="Window type used to taper array antenna."
    )

    def amp_multipliers(
        self, array_size: tuple[PositiveInt, PositiveInt, PositiveInt]
    ) -> tuple[ArrayLike,]:
        """
        Method ``amp_multipliers()`` computes radial taper amplitude for phased array antennas.

        Parameters:
        ----------
        array_size: tuple[PositiveInt, PositiveInt, PositiveInt]
            A tuple of array size along x,y, and z axes.

        Returns:
        --------
        tuple[ArrayLike,]
            a tuple of one 3D numpy array with taper amplitudes.
        """
        effective_size = tuple(dim if dim is not None else 1 for dim in array_size)

        # Generate grid of indices
        grid = np.indices(effective_size)
        idx_c = np.array(effective_size) // 2

        # Compute distances to center
        dists = np.linalg.norm(grid - idx_c[:, None, None, None], axis=0)

        norm_dists = dists / np.max(dists) * np.pi

        amps = self.window._get_weights_continuous(norm_dists)

        amps = np.reshape(amps, effective_size)

        return (amps,)


RectangularAntennaArrayCalculator.update_forward_refs()
