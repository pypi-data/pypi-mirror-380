"""Utilities for autograd derivative computation and field gradient evaluation."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Callable, Optional, Union

import numpy as np
import xarray as xr

from tidy3d.components.data.data_array import FreqDataArray, ScalarFieldDataArray
from tidy3d.components.types import ArrayLike, Bound, tidycomplex
from tidy3d.constants import C_0, EPSILON_0, LARGE_NUMBER, MU_0
from tidy3d.log import log

from .constants import (
    DEFAULT_WAVELENGTH_FRACTION,
    GRADIENT_DTYPE_COMPLEX,
    GRADIENT_DTYPE_FLOAT,
    MINIMUM_SPACING_FRACTION,
)
from .types import PathType
from .utils import get_static

FieldData = dict[str, ScalarFieldDataArray]
PermittivityData = dict[str, ScalarFieldDataArray]
EpsType = Union[tidycomplex, FreqDataArray]


class LazyInterpolator:
    """Lazy wrapper for interpolators that creates them on first access."""

    def __init__(self, creator_func: Callable):
        """Initialize with a function that creates the interpolator when called."""
        self.creator_func = creator_func
        self._interpolator = None

    def __call__(self, *args, **kwargs):
        """Create interpolator on first call and delegate to it."""
        if self._interpolator is None:
            self._interpolator = self.creator_func()
        return self._interpolator(*args, **kwargs)


@dataclass
class DerivativeInfo:
    """Stores derivative information passed to the ``._compute_derivatives`` methods.

    This dataclass contains all the field data and parameters needed for computing
    gradients with respect to geometry perturbations.
    """

    # Required fields
    paths: list[PathType]
    """List of paths to the traced fields that need derivatives calculated."""

    E_der_map: FieldData
    """Electric field gradient map.
    Dataset where the field components ("Ex", "Ey", "Ez") store the multiplication
    of the forward and adjoint electric fields. The tangential components of this
    dataset are used when computing adjoint gradients for shifting boundaries.
    All components are used when computing volume-based gradients."""

    D_der_map: FieldData
    """Displacement field gradient map.
    Dataset where the field components ("Ex", "Ey", "Ez") store the multiplication
    of the forward and adjoint displacement fields. The normal component of this
    dataset is used when computing adjoint gradients for shifting boundaries."""

    E_fwd: FieldData
    """Forward electric fields.
    Dataset where the field components ("Ex", "Ey", "Ez") represent the forward
    electric fields used for computing gradients for a given structure."""

    E_adj: FieldData
    """Adjoint electric fields.
    Dataset where the field components ("Ex", "Ey", "Ez") represent the adjoint
    electric fields used for computing gradients for a given structure."""

    D_fwd: FieldData
    """Forward displacement fields.
    Dataset where the field components ("Ex", "Ey", "Ez") represent the forward
    displacement fields used for computing gradients for a given structure."""

    D_adj: FieldData
    """Adjoint displacement fields.
    Dataset where the field components ("Ex", "Ey", "Ez") represent the adjoint
    displacement fields used for computing gradients for a given structure."""

    eps_data: PermittivityData
    """Permittivity dataset.
    Dataset of relative permittivity values along all three dimensions.
    Used for automatically computing permittivity inside or outside of a simple geometry."""

    eps_in: EpsType
    """Permittivity inside the Structure.
    Typically computed from Structure.medium.eps_model.
    Used when it cannot be computed from eps_data or when eps_approx=True."""

    eps_out: EpsType
    """Permittivity outside the Structure.
    Typically computed from Simulation.medium.eps_model.
    Used when it cannot be computed from eps_data or when eps_approx=True."""

    bounds: Bound
    """Geometry bounds.
    Bounds corresponding to the structure, used in Medium calculations."""

    bounds_intersect: Bound
    """Geometry and simulation intersection bounds.
    Bounds corresponding to the minimum intersection between the structure
    and the simulation it is contained in."""

    simulation_bounds: Bound
    """Simulation bounds.
    Bounds corresponding to the simulation domain containing this structure.
    Unlike bounds_intersect, this is independent of the structure's bounds and
    is purely based on the simulation geometry."""

    frequencies: ArrayLike
    """Frequencies at which the adjoint gradient should be computed."""

    H_der_map: Optional[FieldData] = None
    """Magnetic field gradient map.
    Dataset where the field components ("Hx", "Hy", "Hz") store the multiplication
    of the forward and adjoint magnetic fields. The tangential component of this
    dataset is used when computing adjoint gradients for shifting boundaries of
    structures composed of PEC mediums."""

    H_fwd: Optional[FieldData] = None
    """Forward magnetic fields.
    Dataset where the field components ("Hx", "Hy", "Hz") represent the forward
    magnetic fields used for computing gradients for a given structure."""

    H_adj: Optional[FieldData] = None
    """Adjoint magnetic fields.
    Dataset where the field components ("Hx", "Hy", "Hz") represent the adjoint
    magnetic fields used for computing gradients for a given structure."""

    # Optional fields with defaults
    eps_background: Optional[EpsType] = None
    """Permittivity in background.
    Permittivity outside of the Structure as manually specified by
    Structure.background_medium."""

    eps_no_structure: Optional[ScalarFieldDataArray] = None
    """Permittivity without structure.
    The permittivity of the original simulation without the structure that is
    being differentiated with respect to. Used to approximate permittivity
    outside of the structure for shape optimization."""

    eps_inf_structure: Optional[ScalarFieldDataArray] = None
    """Permittivity with infinite structure.
    The permittivity of the original simulation where the structure being
    differentiated with respect to is infinitely large. Used to approximate
    permittivity inside of the structure for shape optimization."""

    eps_approx: bool = False
    """Use permittivity approximation.
    If True, approximates outside permittivity using Simulation.medium and
    the inside permittivity using Structure.medium. Only set True for
    GeometryGroup handling where it is difficult to automatically evaluate
    the inside and outside relative permittivity for each geometry."""

    is_medium_pec: bool = False
    """Indicates if structure material is PEC.
    If True, the structure contains a PEC material which changes the gradient
    formulation at the boundary compared to the dielectric case."""

    interpolators: Optional[dict] = None
    """Pre-computed interpolators.
    Optional pre-computed interpolators for field components and permittivity data.
    When provided, avoids redundant interpolator creation for multiple geometries
    sharing the same field data. This significantly improves performance for
    GeometryGroup processing."""

    # private cache for interpolators
    _interpolators_cache: dict = field(default_factory=dict, init=False, repr=False)

    def updated_copy(self, **kwargs):
        """Create a copy with updated fields."""
        kwargs.pop("deep", None)
        kwargs.pop("validate", None)
        return replace(self, **kwargs)

    @staticmethod
    def _nan_to_num_if_needed(coords: np.ndarray) -> np.ndarray:
        """Convert NaN and infinite values to finite numbers, optimized for finite inputs."""
        # skip check for small arrays
        if coords.size < 1000:
            return np.nan_to_num(coords, posinf=LARGE_NUMBER, neginf=-LARGE_NUMBER)

        if np.isfinite(coords).all():
            return coords
        return np.nan_to_num(coords, posinf=LARGE_NUMBER, neginf=-LARGE_NUMBER)

    @staticmethod
    def _evaluate_with_interpolators(
        interpolators: dict, coords: np.ndarray
    ) -> dict[str, np.ndarray]:
        """Evaluate field components at coordinates using cached interpolators.

        Parameters
        ----------
        interpolators : dict
            Dictionary mapping field component names to ``RegularGridInterpolator`` objects.
        coords : np.ndarray
            Spatial coordinates (N, 3) where fields are evaluated.

        Returns
        -------
        dict[str, np.ndarray]
            Dictionary mapping component names to field values at coordinates.
        """
        coords = DerivativeInfo._nan_to_num_if_needed(coords)
        if coords.dtype != GRADIENT_DTYPE_FLOAT and coords.dtype != GRADIENT_DTYPE_COMPLEX:
            coords = coords.astype(GRADIENT_DTYPE_FLOAT, copy=False)
        return {name: interp(coords) for name, interp in interpolators.items()}

    def create_interpolators(self, dtype=GRADIENT_DTYPE_FLOAT) -> dict:
        """Create interpolators for field components and permittivity data.

        Creates and caches ``RegularGridInterpolator`` objects for all field components
        (E_fwd, E_adj, D_fwd, D_adj) and permittivity data (eps_inf, eps_no).
        This caching strategy significantly improves performance by avoiding
        repeated interpolator construction in gradient evaluation loops.

        Parameters
        ----------
        dtype : np.dtype = GRADIENT_DTYPE_FLOAT
            Data type for interpolation coordinates and values.

        Returns
        -------
        dict
            Nested dictionary structure:
            - Field data: {"E_fwd": {"Ex": interpolator, ...}, ...}
            - Permittivity: {"eps_inf": interpolator, "eps_no": interpolator}
        """
        from scipy.interpolate import RegularGridInterpolator

        cache_key = str(dtype)
        if cache_key in self._interpolators_cache:
            return self._interpolators_cache[cache_key]

        interpolators = {}
        coord_cache = {}

        def _make_lazy_interpolator_group(field_data_dict, group_key, is_field_group=True):
            """Helper to create a group of lazy interpolators."""
            if is_field_group:
                interpolators[group_key] = {}

            for component_name, arr in field_data_dict.items():
                # use object ID for caching to handle shared grids
                arr_id = id(arr.data)
                if arr_id not in coord_cache:
                    points = tuple(c.data.astype(dtype, copy=False) for c in (arr.x, arr.y, arr.z))
                    coord_cache[arr_id] = points
                points = coord_cache[arr_id]

                def creator_func(arr=arr, points=points):
                    data = arr.data.astype(
                        GRADIENT_DTYPE_COMPLEX if np.iscomplexobj(arr.data) else dtype, copy=False
                    )
                    # create interpolator with frequency dimension
                    if "f" in arr.dims:
                        freq_coords = arr.coords["f"].data.astype(dtype, copy=False)
                        # ensure frequency dimension is last
                        if arr.dims != ("x", "y", "z", "f"):
                            freq_dim_idx = arr.dims.index("f")
                            axes = list(range(data.ndim))
                            axes.append(axes.pop(freq_dim_idx))
                            data = np.transpose(data, axes)
                    else:
                        # single frequency case - add singleton dimension
                        freq_coords = np.array([0.0], dtype=dtype)
                        data = data[..., np.newaxis]

                    points_with_freq = (*points, freq_coords)
                    # If PEC, use nearest interpolation instead of linear to avoid interpolating
                    # with field values inside the PEC (which are 0). Instead, we make sure to
                    # choose interplation points such that their nearest location is outside of
                    # the PEC surface.
                    method = "nearest" if self.is_medium_pec else "linear"
                    interpolator_obj = RegularGridInterpolator(
                        points_with_freq, data, method=method, bounds_error=False, fill_value=None
                    )

                    def interpolator(coords):
                        # coords: (N, 3) spatial points
                        n_points = coords.shape[0]
                        n_freqs = len(freq_coords)

                        # build coordinates with frequency dimension
                        coords_with_freq = np.empty((n_points * n_freqs, 4), dtype=coords.dtype)
                        coords_with_freq[:, :3] = np.repeat(coords, n_freqs, axis=0)
                        coords_with_freq[:, 3] = np.tile(freq_coords, n_points)

                        result = interpolator_obj(coords_with_freq)
                        return result.reshape(n_points, n_freqs)

                    return interpolator

                if is_field_group:
                    interpolators[group_key][component_name] = LazyInterpolator(creator_func)
                else:
                    interpolators[component_name] = LazyInterpolator(creator_func)

        # process field interpolators (nested dictionaries)
        interpolator_groups = [
            ("E_fwd", self.E_fwd),
            ("E_adj", self.E_adj),
            ("D_fwd", self.D_fwd),
            ("D_adj", self.D_adj),
        ]
        if self.is_medium_pec:
            interpolator_groups += [("H_fwd", self.H_fwd), ("H_adj", self.H_adj)]
        for group_key, data_dict in interpolator_groups:
            _make_lazy_interpolator_group(data_dict, group_key, is_field_group=True)

        if self.eps_inf_structure is not None:
            _make_lazy_interpolator_group(
                {"eps_inf": self.eps_inf_structure}, None, is_field_group=False
            )
        if self.eps_no_structure is not None:
            _make_lazy_interpolator_group(
                {"eps_no": self.eps_no_structure}, None, is_field_group=False
            )

        self._interpolators_cache[cache_key] = interpolators
        return interpolators

    def evaluate_gradient_at_points(
        self,
        spatial_coords: np.ndarray,
        normals: np.ndarray,
        perps1: np.ndarray,
        perps2: np.ndarray,
        interpolators: Optional[dict] = None,
    ) -> np.ndarray:
        """Compute adjoint gradients at surface points for shape optimization.

        Implements the surface integral formulation for computing gradients with respect
        to geometry perturbations.

        Parameters
        ----------
        spatial_coords : np.ndarray
            (N, 3) array of surface evaluation points.
        normals : np.ndarray
            (N, 3) array of outward-pointing normal vectors at each surface point.
        perps1 : np.ndarray
            (N, 3) array of first tangent vectors perpendicular to normals.
        perps2 : np.ndarray
            (N, 3) array of second tangent vectors perpendicular to both normals and perps1.
        interpolators : dict = None
            Pre-computed field interpolators for efficiency.

        Returns
        -------
        np.ndarray
            (N,) array of gradient values at each surface point. Must be integrated
            with appropriate quadrature weights to get total gradient.
        """
        if interpolators is None:
            raise NotImplementedError(
                "Direct field evaluation without interpolators is not implemented. "
                "Please create interpolators using 'create_interpolators()' first."
            )

        if "eps_no" in interpolators:
            eps_out = interpolators["eps_no"](spatial_coords)
        else:
            # use eps_background if available, otherwise use eps_out
            eps_to_prepare = (
                self.eps_background if self.eps_background is not None else self.eps_out
            )
            eps_out = self._prepare_epsilon(eps_to_prepare)

        if self.is_medium_pec:
            vjps = self._evaluate_pec_gradient_at_points(
                spatial_coords, normals, perps1, perps2, interpolators, eps_out
            )
        else:
            vjps = self._evaluate_dielectric_gradient_at_points(
                spatial_coords, normals, perps1, perps2, interpolators, eps_out
            )

        # sum over frequency dimension
        vjps = np.sum(vjps, axis=-1)

        return vjps

    def _evaluate_dielectric_gradient_at_points(
        self,
        spatial_coords: np.ndarray,
        normals: np.ndarray,
        perps1: np.ndarray,
        perps2: np.ndarray,
        interpolators: dict,
        # todo: type
        eps_out,
    ) -> np.ndarray:
        # evaluate all field components at surface points
        E_fwd_at_coords = {
            name: interp(spatial_coords) for name, interp in interpolators["E_fwd"].items()
        }
        E_adj_at_coords = {
            name: interp(spatial_coords) for name, interp in interpolators["E_adj"].items()
        }
        D_fwd_at_coords = {
            name: interp(spatial_coords) for name, interp in interpolators["D_fwd"].items()
        }
        D_adj_at_coords = {
            name: interp(spatial_coords) for name, interp in interpolators["D_adj"].items()
        }

        if "eps_inf" in interpolators:
            eps_in = interpolators["eps_inf"](spatial_coords)
        else:
            eps_in = self._prepare_epsilon(self.eps_in)

        delta_eps_inv = 1.0 / eps_in - 1.0 / eps_out
        delta_eps = eps_in - eps_out

        # project fields onto local surface basis (normal + two tangents)
        D_fwd_norm = self._project_in_basis(D_fwd_at_coords, basis_vector=normals)
        D_adj_norm = self._project_in_basis(D_adj_at_coords, basis_vector=normals)

        E_fwd_perp1 = self._project_in_basis(E_fwd_at_coords, basis_vector=perps1)
        E_adj_perp1 = self._project_in_basis(E_adj_at_coords, basis_vector=perps1)

        E_fwd_perp2 = self._project_in_basis(E_fwd_at_coords, basis_vector=perps2)
        E_adj_perp2 = self._project_in_basis(E_adj_at_coords, basis_vector=perps2)

        D_der_norm = D_fwd_norm * D_adj_norm
        E_der_perp1 = E_fwd_perp1 * E_adj_perp1
        E_der_perp2 = E_fwd_perp2 * E_adj_perp2

        vjps = -delta_eps_inv * D_der_norm + E_der_perp1 * delta_eps + E_der_perp2 * delta_eps

        return vjps

    def _evaluate_pec_gradient_at_points(
        self,
        spatial_coords: np.ndarray,
        normals: np.ndarray,
        perps1: np.ndarray,
        perps2: np.ndarray,
        interpolators: dict,
        # todo: type
        eps_out,
    ) -> np.ndarray:
        def _adjust_spatial_coords_pec(grid_centers: dict[str, np.ndarray]):
            """Assuming a nearest interpolation, adjust the interpolation points given the grid
            defined by `grid_centers` and using `spatial_coords` as a starting point such that we
            select a point outside of the PEC boundary.

                 *** (nearest point outside boundary)
                  ^
                  | n (normal direction)
                  |
            _.-~'`-._.-~'`-._ (PEC surface)
                  * (nearest point)

            Parameters
            ----------
            grid_centers: dict[str, np.ndarray]
                The grid points for a given field component indexed by dimension. These grid points
                are used to find the nearest snapping point and adjust the inerpolation coordinates
                to ensure we fall outside of the PEC surface.

            Returns
            -------
            (np.ndarray, np.ndarray)
                (N, 3) array of coordinate centers at which to interpolate such that they line up
                with a grid center and are outside the PEC surface
                (N,) array of distances from the nearest interpolation points to the desired surface
                edge points specified by `spatial_coords`

            """
            grid_ddim = np.zeros_like(normals)
            for idx, dim in enumerate("xyz"):
                expanded_coords = np.expand_dims(spatial_coords[:, idx], axis=1)
                grid_centers_select = grid_centers[dim]

                diff = np.abs(expanded_coords - grid_centers_select)

                nearest_grid = np.argmin(diff, axis=-1)
                nearest_grid = np.minimum(np.maximum(nearest_grid, 1), len(grid_centers_select) - 1)

                # compute the local grid spacing near the boundary
                grid_ddim[:, idx] = (
                    grid_centers_select[nearest_grid] - grid_centers_select[nearest_grid - 1]
                )

            # assuming we move in the normal direction, finds which dimension we need to move the least
            # in order to ensure we snap to a point outside the boundary in the worst case (i.e. - the
            # nearest point is just inside the surface)
            min_movement_index = np.argmin(
                np.abs(grid_ddim) / (np.abs(normals) + np.finfo(normals.dtype).min), axis=1
            )

            selection = (np.arange(normals.shape[0]), min_movement_index)
            coords_dn = np.expand_dims(np.abs(grid_ddim[selection]), axis=1)

            # adjust coordinates by half a grid point outside boundary such that nearest interpolation
            # point snaps to outside the boundary
            adjust_spatial_coords = spatial_coords + normals * 0.5 * coords_dn

            edge_distance = np.zeros_like(adjust_spatial_coords[:, 0])
            for idx, dim in enumerate("xyz"):
                expanded_adjusted_coords = np.expand_dims(adjust_spatial_coords[:, idx], axis=1)
                grid_centers_select = grid_centers[dim]

                # find nearest grid point from the adjusted coordinates
                diff = np.abs(expanded_adjusted_coords - grid_centers_select)
                nearest_grid = np.argmin(diff, axis=-1)

                # compute edge distance from the nearest interpolated point to the boundary edge
                edge_distance += (
                    np.abs(spatial_coords[:, idx] - grid_centers_select[nearest_grid]) ** 2
                )

            # this edge distance is useful when correcting for edge singularities from the PEC material
            # and is used when the PEC PolySlab structure has zero thickness
            edge_distance = np.sqrt(edge_distance)

            return adjust_spatial_coords, edge_distance

        def _snap_coordinate_outside(field_components: FieldData):
            """Helper function to perform coordinate adjustment and compute edge distance for each
            component in `field_components`.

            Parameters
            ----------
            field_components: FieldData
                The field components (i.e - Ex, Ey, Ez, Hx, Hy, Hz) that we would like to sample just
                outside the PEC surface using nearest interpolation.

            Returns
            -------
            dict[str, dict[str, np.ndarray]]
                Dictionary mapping each field component name to a dictionary of adjusted coordinates
                and edge distances for that component.
            """
            adjustment = {}
            for name in field_components:
                field_component = field_components[name]
                field_component_coords = field_component.coords

                adjusted_coords, edge_distance = _adjust_spatial_coords_pec(
                    {
                        key: np.array(field_component_coords[key].values)
                        for key in field_component_coords
                    }
                )
                adjustment[name] = {"coords": adjusted_coords, "edge_distance": edge_distance}

            return adjustment

        def _interpolate_field_components(interp_coords, field_name):
            return {
                name: interp(interp_coords[name]["coords"])
                for name, interp in interpolators[field_name].items()
            }

        # adjust coordinates for PEC to be outside structure bounds and get edge distance for singularity correction.
        E_fwd_coords_adjusted = _snap_coordinate_outside(self.E_fwd)
        E_adj_coords_adjusted = _snap_coordinate_outside(self.E_adj)

        H_fwd_coords_adjusted = _snap_coordinate_outside(self.H_fwd)
        H_adj_coords_adjusted = _snap_coordinate_outside(self.H_adj)

        # using the adjusted coordinates, evaluate all field components at surface points
        E_fwd_at_coords = _interpolate_field_components(E_fwd_coords_adjusted, "E_fwd")
        E_adj_at_coords = _interpolate_field_components(E_adj_coords_adjusted, "E_adj")
        H_fwd_at_coords = _interpolate_field_components(H_fwd_coords_adjusted, "H_fwd")
        H_adj_at_coords = _interpolate_field_components(H_adj_coords_adjusted, "H_adj")

        structure_sizes = np.array(
            [self.bounds[1][idx] - self.bounds[0][idx] for idx in range(len(self.bounds[0]))]
        )

        is_flat_perp_dim1 = np.isclose(np.abs(np.sum(perps1[0] * structure_sizes)), 0.0)
        is_flat_perp_dim2 = np.isclose(np.abs(np.sum(perps2[0] * structure_sizes)), 0.0)
        flat_perp_dims = [is_flat_perp_dim1, is_flat_perp_dim2]

        # check if this integration is happening along an edge in which case we will eliminate
        # on of the H field integration components and apply singularity correction
        pec_line_integration = is_flat_perp_dim1 or is_flat_perp_dim2

        def _compute_singularity_correction(adjustment_: dict[str, dict[str, np.ndarray]]):
            """
            Given the `adjustment_` which contains the distance from the PEC edge each field
            component is nearest interpolated at, computes the singularity correction when
            working with 2D PEC using the average edge_distance for each component. In the case
            of 3D PEC gradients, no singularity correction is applied so an array of ones is returned.

            Parameters
            ----------
            adjustment_: dict[str, dict[str, np.ndarray]]
                Dictionary that maps field component name to a dictionary containing the coordinate
                adjustment and the distance to the PEC edge for those coordinates. The edge distance
                is used for 2D PEC singularity correction.

            Returns
            -------
            np.ndarray
                Returns the singularity correction which has shape (N,) where there are N points in
                `spatial_coords`
            """
            return (
                (
                    0.5
                    * np.pi
                    * np.mean([adjustment_[name]["edge_distance"] for name in adjustment_], axis=0)
                )
                if pec_line_integration
                else np.ones_like(spatial_coords, shape=spatial_coords.shape[0])
            )

        E_norm_singularity_correction = np.expand_dims(
            _compute_singularity_correction(E_fwd_coords_adjusted), axis=1
        )
        H_perp_singularity_correction = np.expand_dims(
            _compute_singularity_correction(H_fwd_coords_adjusted), axis=1
        )

        E_fwd_norm = self._project_in_basis(E_fwd_at_coords, basis_vector=normals)
        E_adj_norm = self._project_in_basis(E_adj_at_coords, basis_vector=normals)

        # compute the normal E contribution to the gradient (the tangential E contribution
        # is 0 in the case of PEC since this field component is continuous and thus 0 at
        # the boundary)
        contrib_E = E_norm_singularity_correction * eps_out * E_fwd_norm * E_adj_norm
        vjps = contrib_E

        # compute the tangential H contribution to the gradient (the normal H contribution
        # is 0 for PEC)
        H_fwd_perp1 = self._project_in_basis(H_fwd_at_coords, basis_vector=perps1)
        H_adj_perp1 = self._project_in_basis(H_adj_at_coords, basis_vector=perps1)

        H_fwd_perp2 = self._project_in_basis(H_fwd_at_coords, basis_vector=perps2)
        H_adj_perp2 = self._project_in_basis(H_adj_at_coords, basis_vector=perps2)

        H_der_perp1 = H_perp_singularity_correction * H_fwd_perp1 * H_adj_perp1
        H_der_perp2 = H_perp_singularity_correction * H_fwd_perp2 * H_adj_perp2

        H_integration_components = (H_der_perp1, H_der_perp2)
        if pec_line_integration:
            # if we are integrating along the line, we choose the H component normal to
            # the edge which corresponds to a surface current along the edge whereas the other
            # tangential component corresponds to a surface current along the flat dimension.
            H_integration_components = tuple(
                H_comp for idx, H_comp in enumerate(H_integration_components) if flat_perp_dims[idx]
            )

        # for each of the tangential components we are integrating the H fields over,
        # adjust weighting to account for pre-weighting of the source by `EPSILON_0`
        # and multiply by appropriate `MU_0` factor
        for H_perp in H_integration_components:
            contrib_H = MU_0 * H_perp / EPSILON_0
            vjps += contrib_H

        return vjps

    @staticmethod
    def _prepare_epsilon(eps: EpsType) -> np.ndarray:
        """Prepare epsilon values for multi-frequency.

        For FreqDataArray, extracts values and broadcasts to shape (1, n_freqs).
        For scalar values, broadcasts to shape (1, 1) for consistency with multi-frequency.
        """
        if isinstance(eps, FreqDataArray):
            # data is already sliced, just extract values
            eps_values = eps.values
            # shape: (n_freqs,) - need to broadcast to (1, n_freqs)
            return eps_values[np.newaxis, :]
        else:
            # scalar value - broadcast to (1, 1)
            return np.array([[eps]])

    @staticmethod
    def _project_in_basis(
        field_components: dict[str, np.ndarray],
        basis_vector: np.ndarray,
    ) -> np.ndarray:
        """Project 3D field components onto a basis vector.

        Parameters
        ----------
        field_components : dict[str, np.ndarray]
            Dictionary with keys like "Ex", "Ey", "Ez" or "Dx", "Dy", "Dz" containing field values.
            Values have shape (N, F) where F is the number of frequencies.
        basis_vector : np.ndarray
            (N, 3) array of basis vectors, one per evaluation point.

        Returns
        -------
        np.ndarray
            Projected field values with shape (N, F).
        """
        prefix = next(iter(field_components.keys()))[0]
        field_matrix = np.stack([field_components[f"{prefix}{dim}"] for dim in "xyz"], axis=0)

        # always expect (3, N, F) shape, transpose to (N, 3, F)
        field_matrix = np.transpose(field_matrix, (1, 0, 2))
        return np.einsum("ij...,ij->i...", field_matrix, basis_vector)

    def adaptive_vjp_spacing(
        self,
        wl_fraction: float = DEFAULT_WAVELENGTH_FRACTION,
        min_allowed_spacing_fraction: float = MINIMUM_SPACING_FRACTION,
    ) -> float:
        """Compute adaptive spacing for finite-difference gradient evaluation.

        Determines an appropriate spatial resolution based on the material
        properties and electromagnetic wavelength/skin depth.

        Parameters
        ----------
        wl_fraction : float = 0.1
            Fraction of wavelength/skin depth to use as spacing.
        min_allowed_spacing_fraction : float = 1e-2
            Minimum allowed spacing fraction of free space wavelength to
            prevent numerical issues.

        Returns
        -------
        float
            Adaptive spacing value for gradient evaluation.
        """
        # handle FreqDataArray or scalar eps_in
        if isinstance(self.eps_in, FreqDataArray):
            eps_real = np.asarray(self.eps_in.values, dtype=np.complex128).real
        else:
            eps_real = np.asarray(self.eps_in, dtype=np.complex128).real

        dx_candidates = []
        max_frequency = np.max(self.frequencies)

        # wavelength-based sampling for dielectrics
        if np.any(eps_real > 0):
            eps_max = eps_real[eps_real > 0].max()
            lambda_min = self.wavelength_min / np.sqrt(eps_max)
            dx_candidates.append(wl_fraction * lambda_min)

        # skin depth sampling for metals
        if np.any(eps_real <= 0):
            omega = 2 * np.pi * max_frequency
            eps_neg = eps_real[eps_real <= 0]
            delta_min = C_0 / (omega * np.sqrt(np.abs(eps_neg).max()))
            dx_candidates.append(wl_fraction * delta_min)

        computed_spacing = min(dx_candidates)
        min_allowed_spacing = self.wavelength_min * min_allowed_spacing_fraction

        if computed_spacing < min_allowed_spacing:
            log.warning(
                f"Based on the material, the adaptive spacing for integrating the polyslab surface "
                f"would be {computed_spacing:.3e} μm. The spacing has been clipped to {min_allowed_spacing:.3e} μm "
                f"to prevent a performance degradation.",
                log_once=True,
            )
        return max(computed_spacing, min_allowed_spacing)

    @property
    def wavelength_min(self) -> float:
        return C_0 / np.max(self.frequencies)

    @property
    def wavelength_max(self) -> float:
        return C_0 / np.min(self.frequencies)


def integrate_within_bounds(arr: xr.DataArray, dims: list[str], bounds: Bound) -> xr.DataArray:
    """Integrate a data array within specified spatial bounds.

    Clips the integration domain to the specified bounds and performs
    numerical integration using the trapezoidal rule.

    Parameters
    ----------
    arr : xr.DataArray
        Data array to integrate.
    dims : list[str]
        Dimensions to integrate over (e.g., ['x', 'y', 'z']).
    bounds : Bound
        Integration bounds as [[xmin, ymin, zmin], [xmax, ymax, zmax]].

    Returns
    -------
    xr.DataArray
        Result of integration with specified dimensions removed.

    Notes
    -----
    - Coordinates outside bounds are clipped, effectively setting dL=0
    - Only integrates dimensions with more than one coordinate point
    - Uses xarray's integrate method (trapezoidal rule)
    """
    bounds = np.asarray(bounds).T
    all_coords = {}

    for dim, (bmin, bmax) in zip(dims, bounds):
        bmin = get_static(bmin)
        bmax = get_static(bmax)

        # clip coordinates to bounds (sets dL=0 outside bounds)
        coord_values = arr.coords[dim].data
        all_coords[dim] = np.clip(coord_values, bmin, bmax)

    _arr = arr.assign_coords(**all_coords)

    # only integrate dimensions with multiple points
    dims_integrate = [dim for dim in dims if len(_arr.coords[dim]) > 1]
    return _arr.integrate(coord=dims_integrate)


__all__ = [
    "DerivativeInfo",
    "integrate_within_bounds",
]
