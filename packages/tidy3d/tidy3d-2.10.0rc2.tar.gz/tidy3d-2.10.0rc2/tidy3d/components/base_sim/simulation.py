"""Abstract base for defining simulation classes of different solvers"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

import autograd.numpy as anp
import pydantic.v1 as pd

from tidy3d.components.base import cached_property, skip_if_fields_missing
from tidy3d.components.geometry.base import Box
from tidy3d.components.medium import Medium, MediumType3D
from tidy3d.components.scene import Scene
from tidy3d.components.structure import Structure
from tidy3d.components.types import (
    TYPE_TAG_STR,
    Ax,
    Axis,
    Bound,
    LengthUnit,
    PriorityMode,
    Symmetry,
)
from tidy3d.components.validators import (
    _warn_unsupported_traced_argument,
    assert_objects_in_sim_bounds,
    assert_unique_names,
)
from tidy3d.components.viz import PlotParams, add_ax_if_none, equal_aspect, plot_params_symmetry
from tidy3d.exceptions import Tidy3dKeyError
from tidy3d.log import log
from tidy3d.version import __version__

from .monitor import AbstractMonitor


class AbstractSimulation(Box, ABC):
    """Base class for simulation classes of different solvers."""

    medium: MediumType3D = pd.Field(
        Medium(),
        title="Background Medium",
        description="Background medium of simulation, defaults to vacuum if not specified.",
        discriminator=TYPE_TAG_STR,
    )
    """
    Background medium of simulation, defaults to vacuum if not specified.
    """

    structures: tuple[Structure, ...] = pd.Field(
        (),
        title="Structures",
        description="Tuple of structures present in simulation. "
        "Note: Structures defined later in this list override the "
        "simulation material properties in regions of spatial overlap.",
    )
    """
    Tuple of structures present in simulation. Structures defined later in this list override the simulation
    material properties in regions of spatial overlap.

    Example
    -------
    Simple application reference:

    .. code-block:: python

        Simulation(
            ...
            structures=[
                 Structure(
                 geometry=Box(size=(1, 1, 1), center=(0, 0, 0)),
                 medium=Medium(permittivity=2.0),
                 ),
            ],
            ...
        )
    """

    symmetry: tuple[Symmetry, Symmetry, Symmetry] = pd.Field(
        (0, 0, 0),
        title="Symmetries",
        description="Tuple of integers defining reflection symmetry across a plane "
        "bisecting the simulation domain normal to the x-, y-, and z-axis "
        "at the simulation center of each axis, respectively. ",
    )

    sources: tuple[None, ...] = pd.Field(
        (),
        title="Sources",
        description="Sources in the simulation.",
    )

    boundary_spec: None = pd.Field(
        None,
        title="Boundaries",
        description="Specification of boundary conditions.",
    )

    monitors: tuple[None, ...] = pd.Field(
        (),
        title="Monitors",
        description="Monitors in the simulation. ",
    )

    grid_spec: None = pd.Field(
        None,
        title="Grid Specification",
        description="Specifications for the simulation grid.",
    )

    version: str = pd.Field(
        __version__,
        title="Version",
        description="String specifying the front end version number.",
    )

    plot_length_units: Optional[LengthUnit] = pd.Field(
        "μm",
        title="Plot Units",
        description="When set to a supported ``LengthUnit``, "
        "plots will be produced with proper scaling of axes and "
        "include the desired unit specifier in labels.",
    )

    structure_priority_mode: PriorityMode = pd.Field(
        "equal",
        title="Structure Priority Setting",
        description="This field only affects structures of `priority=None`. "
        "If `equal`, the priority of those structures is set to 0; if `conductor`, "
        "the priority of structures made of :class:`LossyMetalMedium` is set to 90, "
        ":class:`PECMedium` to 100, and others to 0.",
    )

    """ Validating setup """

    @pd.root_validator(pre=True)
    def _update_simulation(cls, values):
        """Update the simulation if it is an earlier version."""

        # dummy upgrade of version number
        # this should be overriden by each simulation class if needed
        current_version = values.get("version")
        if current_version != __version__ and current_version is not None:
            log.warning(f"updating {cls.__name__} from {current_version} to {__version__}")
            values["version"] = __version__
        return values

    # make sure all names are unique
    _unique_monitor_names = assert_unique_names("monitors")
    _unique_structure_names = assert_unique_names("structures")
    _unique_source_names = assert_unique_names("sources")

    _monitors_in_bounds = assert_objects_in_sim_bounds("monitors", strict_inequality=True)
    _structures_in_bounds = assert_objects_in_sim_bounds("structures", error=False)

    _warn_traced_center = _warn_unsupported_traced_argument("center")
    _warn_traced_size = _warn_unsupported_traced_argument("size")

    @pd.validator("structures", always=True)
    @skip_if_fields_missing(["size", "center"])
    def _structures_not_at_edges(cls, val, values):
        """Warn if any structures lie at the simulation boundaries."""

        if val is None:
            return val

        sim_box = Box(size=values.get("size"), center=values.get("center"))
        sim_bound_min, sim_bound_max = sim_box.bounds
        sim_bounds = list(sim_bound_min) + list(sim_bound_max)

        with log as consolidated_logger:
            for istruct, structure in enumerate(val):
                struct_bound_min, struct_bound_max = structure.geometry.bounds
                struct_bounds = list(struct_bound_min) + list(struct_bound_max)

                for sim_val, struct_val in zip(sim_bounds, struct_bounds):
                    if anp.isclose(sim_val, struct_val):
                        consolidated_logger.warning(
                            f"Structure at 'structures[{istruct}]' has bounds that extend exactly "
                            "to simulation edges. This can cause unexpected behavior. "
                            "If intending to extend the structure to infinity along one dimension, "
                            "use td.inf as a size variable instead to make this explicit.",
                            custom_loc=["structures", istruct],
                        )
                        continue

        return val

    """ Post-init validators """

    def _post_init_validators(self) -> None:
        """Call validators taking z`self` that get run after init."""
        _ = self.scene

    def validate_pre_upload(self) -> None:
        """Validate the fully initialized simulation is ok for upload to our servers."""

    """ Accounting """

    @cached_property
    def scene(self) -> Scene:
        """Scene instance associated with the simulation."""

        return Scene(
            medium=self.medium,
            structures=self.structures,
            plot_length_units=self.plot_length_units,
            structure_priority_mode=self.structure_priority_mode,
        )

    def get_monitor_by_name(self, name: str) -> AbstractMonitor:
        """Return monitor named 'name'."""
        for monitor in self.monitors:
            if monitor.name == name:
                return monitor
        raise Tidy3dKeyError(f"No monitor named '{name}'")

    @cached_property
    def simulation_bounds(self) -> Bound:
        """Simulation bounds including auxiliary boundary zones such as PML layers."""
        # in this default implementation we just take self.bounds
        # this should be changed in different solvers depending on whether automatic extensions
        # (like pml) are present
        return self.bounds

    @cached_property
    def simulation_geometry(self) -> Box:
        """The entire simulation domain including auxiliary boundary zones such as PML layers.
        It is identical to ``Simulation.geometry`` in the absence of such auxiliary zones.
        """
        rmin, rmax = self.simulation_bounds
        return Box.from_bounds(rmin=rmin, rmax=rmax)

    @cached_property
    def simulation_structure(self) -> Structure:
        """Returns structure representing the domain of the simulation. This differs from
        ``Simulation.scene.background_structure`` in that it has finite extent."""
        return Structure(geometry=self.simulation_geometry, medium=self.medium)

    @equal_aspect
    @add_ax_if_none
    def plot(
        self,
        x: Optional[float] = None,
        y: Optional[float] = None,
        z: Optional[float] = None,
        ax: Ax = None,
        source_alpha: Optional[float] = None,
        monitor_alpha: Optional[float] = None,
        hlim: Optional[tuple[float, float]] = None,
        vlim: Optional[tuple[float, float]] = None,
        fill_structures: bool = True,
        **patch_kwargs,
    ) -> Ax:
        """Plot each of simulation's components on a plane defined by one nonzero x,y,z coordinate.

        Parameters
        ----------
        x : float = None
            position of plane in x direction, only one of x, y, z must be specified to define plane.
        y : float = None
            position of plane in y direction, only one of x, y, z must be specified to define plane.
        z : float = None
            position of plane in z direction, only one of x, y, z must be specified to define plane.
        source_alpha : float = None
            Opacity of the sources. If ``None``, uses Tidy3d default.
        monitor_alpha : float = None
            Opacity of the monitors. If ``None``, uses Tidy3d default.
        ax : matplotlib.axes._subplots.Axes = None
            Matplotlib axes to plot on, if not specified, one is created.
        hlim : Tuple[float, float] = None
            The x range if plotting on xy or xz planes, y range if plotting on yz plane.
        vlim : Tuple[float, float] = None
            The z range if plotting on xz or yz planes, y plane if plotting on xy plane.
        fill_structures : bool = True
            Whether to fill structures with color or just draw outlines.
        Returns
        -------
        matplotlib.axes._subplots.Axes
            The supplied or created matplotlib axes.
        """

        hlim, vlim = Scene._get_plot_lims(
            bounds=self.simulation_bounds, x=x, y=y, z=z, hlim=hlim, vlim=vlim
        )

        ax = self.scene.plot_structures(
            ax=ax, x=x, y=y, z=z, hlim=hlim, vlim=vlim, fill=fill_structures
        )
        ax = self.plot_sources(ax=ax, x=x, y=y, z=z, hlim=hlim, vlim=vlim, alpha=source_alpha)
        ax = self.plot_monitors(ax=ax, x=x, y=y, z=z, hlim=hlim, vlim=vlim, alpha=monitor_alpha)
        ax = Scene._set_plot_bounds(
            bounds=self.simulation_bounds, ax=ax, x=x, y=y, z=z, hlim=hlim, vlim=vlim
        )
        ax = self.plot_boundaries(ax=ax, x=x, y=y, z=z)
        ax = self.plot_symmetries(ax=ax, x=x, y=y, z=z, hlim=hlim, vlim=vlim)

        # Add the default axis labels, tick labels, and title
        ax = Box.add_ax_labels_and_title(
            ax=ax, x=x, y=y, z=z, plot_length_units=self.plot_length_units
        )

        return ax

    @equal_aspect
    @add_ax_if_none
    def plot_sources(
        self,
        x: Optional[float] = None,
        y: Optional[float] = None,
        z: Optional[float] = None,
        hlim: Optional[tuple[float, float]] = None,
        vlim: Optional[tuple[float, float]] = None,
        alpha: Optional[float] = None,
        ax: Ax = None,
    ) -> Ax:
        """Plot each of simulation's sources on a plane defined by one nonzero x,y,z coordinate.

        Parameters
        ----------
        x : float = None
            position of plane in x direction, only one of x, y, z must be specified to define plane.
        y : float = None
            position of plane in y direction, only one of x, y, z must be specified to define plane.
        z : float = None
            position of plane in z direction, only one of x, y, z must be specified to define plane.
        hlim : Tuple[float, float] = None
            The x range if plotting on xy or xz planes, y range if plotting on yz plane.
        vlim : Tuple[float, float] = None
            The z range if plotting on xz or yz planes, y plane if plotting on xy plane.
        alpha : float = None
            Opacity of the sources, If ``None`` uses Tidy3d default.
        ax : matplotlib.axes._subplots.Axes = None
            Matplotlib axes to plot on, if not specified, one is created.

        Returns
        -------
        matplotlib.axes._subplots.Axes
            The supplied or created matplotlib axes.
        """
        bounds = self.bounds
        for source in self.sources:
            ax = source.plot(x=x, y=y, z=z, alpha=alpha, ax=ax, sim_bounds=bounds)
        ax = Scene._set_plot_bounds(
            bounds=self.simulation_bounds, ax=ax, x=x, y=y, z=z, hlim=hlim, vlim=vlim
        )
        # Add the default axis labels, tick labels, and title
        ax = Box.add_ax_labels_and_title(
            ax=ax, x=x, y=y, z=z, plot_length_units=self.plot_length_units
        )
        return ax

    @equal_aspect
    @add_ax_if_none
    def plot_monitors(
        self,
        x: Optional[float] = None,
        y: Optional[float] = None,
        z: Optional[float] = None,
        hlim: Optional[tuple[float, float]] = None,
        vlim: Optional[tuple[float, float]] = None,
        alpha: Optional[float] = None,
        ax: Ax = None,
    ) -> Ax:
        """Plot each of simulation's monitors on a plane defined by one nonzero x,y,z coordinate.

        Parameters
        ----------
        x : float = None
            position of plane in x direction, only one of x, y, z must be specified to define plane.
        y : float = None
            position of plane in y direction, only one of x, y, z must be specified to define plane.
        z : float = None
            position of plane in z direction, only one of x, y, z must be specified to define plane.
        hlim : Tuple[float, float] = None
            The x range if plotting on xy or xz planes, y range if plotting on yz plane.
        vlim : Tuple[float, float] = None
            The z range if plotting on xz or yz planes, y plane if plotting on xy plane.
        alpha : float = None
            Opacity of the sources, If ``None`` uses Tidy3d default.
        ax : matplotlib.axes._subplots.Axes = None
            Matplotlib axes to plot on, if not specified, one is created.

        Returns
        -------
        matplotlib.axes._subplots.Axes
            The supplied or created matplotlib axes.
        """
        bounds = self.bounds
        for monitor in self.monitors:
            ax = monitor.plot(x=x, y=y, z=z, alpha=alpha, ax=ax, sim_bounds=bounds)
        ax = Scene._set_plot_bounds(
            bounds=self.simulation_bounds, ax=ax, x=x, y=y, z=z, hlim=hlim, vlim=vlim
        )
        # Add the default axis labels, tick labels, and title
        ax = Box.add_ax_labels_and_title(
            ax=ax, x=x, y=y, z=z, plot_length_units=self.plot_length_units
        )
        return ax

    @equal_aspect
    @add_ax_if_none
    def plot_symmetries(
        self,
        x: Optional[float] = None,
        y: Optional[float] = None,
        z: Optional[float] = None,
        hlim: Optional[tuple[float, float]] = None,
        vlim: Optional[tuple[float, float]] = None,
        ax: Ax = None,
    ) -> Ax:
        """Plot each of simulation's symmetries on a plane defined by one nonzero x,y,z coordinate.

        Parameters
        ----------
        x : float = None
            position of plane in x direction, only one of x, y, z must be specified to define plane.
        y : float = None
            position of plane in y direction, only one of x, y, z must be specified to define plane.
        z : float = None
            position of plane in z direction, only one of x, y, z must be specified to define plane.
        hlim : Tuple[float, float] = None
            The x range if plotting on xy or xz planes, y range if plotting on yz plane.
        vlim : Tuple[float, float] = None
            The z range if plotting on xz or yz planes, y plane if plotting on xy plane.
        ax : matplotlib.axes._subplots.Axes = None
            Matplotlib axes to plot on, if not specified, one is created.

        Returns
        -------
        matplotlib.axes._subplots.Axes
            The supplied or created matplotlib axes.
        """

        normal_axis, _ = Box.parse_xyz_kwargs(x=x, y=y, z=z)

        for sym_axis, sym_value in enumerate(self.symmetry):
            if sym_value == 0 or sym_axis == normal_axis:
                continue
            sym_box = self._make_symmetry_box(sym_axis=sym_axis)
            plot_params = self._make_symmetry_plot_params(sym_value=sym_value)
            ax = sym_box.plot(x=x, y=y, z=z, ax=ax, **plot_params.to_kwargs())
        ax = Scene._set_plot_bounds(
            bounds=self.simulation_bounds, ax=ax, x=x, y=y, z=z, hlim=hlim, vlim=vlim
        )
        # Add the default axis labels, tick labels, and title
        ax = Box.add_ax_labels_and_title(
            ax=ax, x=x, y=y, z=z, plot_length_units=self.plot_length_units
        )
        return ax

    def _make_symmetry_plot_params(self, sym_value: Symmetry) -> PlotParams:
        """Make PlotParams for symmetry."""

        plot_params = plot_params_symmetry.copy()

        if sym_value == 1:
            plot_params = plot_params.copy(
                update={"facecolor": "lightsteelblue", "edgecolor": "lightsteelblue", "hatch": "++"}
            )
        elif sym_value == -1:
            plot_params = plot_params.copy(
                update={"facecolor": "goldenrod", "edgecolor": "goldenrod", "hatch": "--"}
            )

        return plot_params

    def _make_symmetry_box(self, sym_axis: Axis) -> Box:
        """Construct a :class:`.Box` representing the symmetry to be plotted."""
        rmin, rmax = (list(bound) for bound in self.simulation_bounds)
        rmax[sym_axis] = (rmin[sym_axis] + rmax[sym_axis]) / 2

        return Box.from_bounds(rmin, rmax)

    @abstractmethod
    @equal_aspect
    @add_ax_if_none
    def plot_boundaries(
        self,
        x: Optional[float] = None,
        y: Optional[float] = None,
        z: Optional[float] = None,
        ax: Ax = None,
        **kwargs,
    ) -> Ax:
        """Plot the simulation boundary conditions as lines on a plane
           defined by one nonzero x,y,z coordinate.

        Parameters
        ----------
        x : float = None
            position of plane in x direction, only one of x, y, z must be specified to define plane.
        y : float = None
            position of plane in y direction, only one of x, y, z must be specified to define plane.
        z : float = None
            position of plane in z direction, only one of x, y, z must be specified to define plane.
        ax : matplotlib.axes._subplots.Axes = None
            Matplotlib axes to plot on, if not specified, one is created.
        **kwargs
            Optional keyword arguments passed to the matplotlib ``LineCollection``.
            For details on accepted values, refer to
            `Matplotlib's documentation <https://tinyurl.com/2p97z4cn>`_.

        Returns
        -------
        matplotlib.axes._subplots.Axes
            The supplied or created matplotlib axes.
        """

    @equal_aspect
    @add_ax_if_none
    def plot_structures(
        self,
        x: Optional[float] = None,
        y: Optional[float] = None,
        z: Optional[float] = None,
        ax: Ax = None,
        hlim: Optional[tuple[float, float]] = None,
        vlim: Optional[tuple[float, float]] = None,
        fill: bool = True,
    ) -> Ax:
        """Plot each of simulation's structures on a plane defined by one nonzero x,y,z coordinate.

        Parameters
        ----------
        x : float = None
            position of plane in x direction, only one of x, y, z must be specified to define plane.
        y : float = None
            position of plane in y direction, only one of x, y, z must be specified to define plane.
        z : float = None
            position of plane in z direction, only one of x, y, z must be specified to define plane.
        ax : matplotlib.axes._subplots.Axes = None
            Matplotlib axes to plot on, if not specified, one is created.
        hlim : Tuple[float, float] = None
            The x range if plotting on xy or xz planes, y range if plotting on yz plane.
        vlim : Tuple[float, float] = None
            The z range if plotting on xz or yz planes, y plane if plotting on xy plane.
        fill : bool = True
            Whether to fill structures with color or just draw outlines.
        Returns
        -------
        matplotlib.axes._subplots.Axes
            The supplied or created matplotlib axes.
        """

        hlim_new, vlim_new = Scene._get_plot_lims(
            bounds=self.simulation_bounds, x=x, y=y, z=z, hlim=hlim, vlim=vlim
        )

        return self.scene.plot_structures(
            x=x, y=y, z=z, ax=ax, hlim=hlim_new, vlim=vlim_new, fill=fill
        )

    @equal_aspect
    @add_ax_if_none
    def plot_structures_eps(
        self,
        x: Optional[float] = None,
        y: Optional[float] = None,
        z: Optional[float] = None,
        freq: Optional[float] = None,
        alpha: Optional[float] = None,
        cbar: bool = True,
        reverse: bool = False,
        ax: Ax = None,
        hlim: Optional[tuple[float, float]] = None,
        vlim: Optional[tuple[float, float]] = None,
    ) -> Ax:
        """Plot each of simulation's structures on a plane defined by one nonzero x,y,z coordinate.
        The permittivity is plotted in grayscale based on its value at the specified frequency.

        Parameters
        ----------
        x : float = None
            position of plane in x direction, only one of x, y, z must be specified to define plane.
        y : float = None
            position of plane in y direction, only one of x, y, z must be specified to define plane.
        z : float = None
            position of plane in z direction, only one of x, y, z must be specified to define plane.
        freq : float = None
            Frequency to evaluate the relative permittivity of all mediums.
            If not specified, evaluates at infinite frequency.
        reverse : bool = False
            If ``False``, the highest permittivity is plotted in black.
            If ``True``, it is plotteed in white (suitable for black backgrounds).
        cbar : bool = True
            Whether to plot a colorbar for the relative permittivity.
        alpha : float = None
            Opacity of the structures being plotted.
            Defaults to the structure default alpha.
        ax : matplotlib.axes._subplots.Axes = None
            Matplotlib axes to plot on, if not specified, one is created.
        hlim : Tuple[float, float] = None
            The x range if plotting on xy or xz planes, y range if plotting on yz plane.
        vlim : Tuple[float, float] = None
            The z range if plotting on xz or yz planes, y plane if plotting on xy plane.

        Returns
        -------
        matplotlib.axes._subplots.Axes
            The supplied or created matplotlib axes.
        """

        hlim, vlim = Scene._get_plot_lims(
            bounds=self.simulation_bounds, x=x, y=y, z=z, hlim=hlim, vlim=vlim
        )

        return self.scene.plot_structures_eps(
            freq=freq,
            cbar=cbar,
            alpha=alpha,
            ax=ax,
            x=x,
            y=y,
            z=z,
            hlim=hlim,
            vlim=vlim,
            reverse=reverse,
        )

    @equal_aspect
    @add_ax_if_none
    def plot_structures_heat_conductivity(
        self,
        x: Optional[float] = None,
        y: Optional[float] = None,
        z: Optional[float] = None,
        alpha: Optional[float] = None,
        cbar: bool = True,
        reverse: bool = False,
        ax: Ax = None,
        hlim: Optional[tuple[float, float]] = None,
        vlim: Optional[tuple[float, float]] = None,
    ) -> Ax:
        """Plot each of simulation's structures on a plane defined by one nonzero x,y,z coordinate.
        The permittivity is plotted in grayscale based on its value at the specified frequency.

        Parameters
        ----------
        x : float = None
            position of plane in x direction, only one of x, y, z must be specified to define plane.
        y : float = None
            position of plane in y direction, only one of x, y, z must be specified to define plane.
        z : float = None
            position of plane in z direction, only one of x, y, z must be specified to define plane.
        freq : float = None
            Frequency to evaluate the relative permittivity of all mediums.
            If not specified, evaluates at infinite frequency.
        reverse : bool = False
            If ``False``, the highest permittivity is plotted in black.
            If ``True``, it is plotteed in white (suitable for black backgrounds).
        cbar : bool = True
            Whether to plot a colorbar for the relative permittivity.
        alpha : float = None
            Opacity of the structures being plotted.
            Defaults to the structure default alpha.
        ax : matplotlib.axes._subplots.Axes = None
            Matplotlib axes to plot on, if not specified, one is created.
        hlim : Tuple[float, float] = None
            The x range if plotting on xy or xz planes, y range if plotting on yz plane.
        vlim : Tuple[float, float] = None
            The z range if plotting on xz or yz planes, y plane if plotting on xy plane.

        Returns
        -------
        matplotlib.axes._subplots.Axes
            The supplied or created matplotlib axes.
        """

        hlim, vlim = Scene._get_plot_lims(
            bounds=self.simulation_bounds, x=x, y=y, z=z, hlim=hlim, vlim=vlim
        )

        return self.scene.plot_structures_heat_conductivity(
            cbar=cbar,
            alpha=alpha,
            ax=ax,
            x=x,
            y=y,
            z=z,
            hlim=hlim,
            vlim=vlim,
            reverse=reverse,
        )

    @classmethod
    def from_scene(cls, scene: Scene, **kwargs) -> AbstractSimulation:
        """Create a simulation from a :class:`.Scene` instance. Must provide additional parameters
        to define a valid simulation (for example, ``size``, ``run_time``, ``grid_spec``, etc).

        Parameters
        ----------
        scene : :class:`.Scene`
            Scene containing structures information.
        **kwargs
            Other arguments
        """

        return cls(
            structures=scene.structures,
            medium=scene.medium,
            **kwargs,
        )

    def plot_3d(self, width=800, height=800) -> None:
        """Render 3D plot of ``AbstractSimulation`` (in jupyter notebook only).
        Parameters
        ----------
        width : float = 800
            width of the 3d view dom's size
        height : float = 800
            height of the 3d view dom's size

        """
        return self.scene.plot_3d(width=width, height=height)
