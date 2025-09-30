"""Provide interface classes for manifold data access in connection discovery.

This module provides interface classes that abstract manifold data access
for the connection discovery system. These interfaces handle the conversion
between manifold representations and the synodic section intersections
needed for connection analysis.

The interfaces serve as adapters between the manifold system and the
connection discovery algorithms, providing a clean separation of concerns
and enabling flexible data access patterns.

All coordinates are in nondimensional CR3BP rotating-frame units.

See Also
--------
:mod:`~hiten.system.manifold`
    Manifold classes that these interfaces wrap.
:mod:`~hiten.algorithms.poincare.synodic.base`
    Synodic map functionality used for section intersections.
:mod:`~hiten.algorithms.connections.engine`
    ConnectionPipeline engine that uses these interfaces.
"""

from typing import TYPE_CHECKING, Literal

import numpy as np

from hiten.algorithms.connections.config import _ConnectionConfig
from hiten.algorithms.connections.types import (ConnectionResults,
                                                _ConnectionProblem)
from hiten.algorithms.poincare.core.types import _Section
from hiten.algorithms.poincare.synodic.config import _SynodicMapConfig
from hiten.algorithms.types.core import _HitenBaseInterface
from hiten.algorithms.types.exceptions import EngineError
from hiten.system.maps.synodic import SynodicMap

if TYPE_CHECKING:
    from hiten.system.manifold import Manifold


class _ManifoldInterface(
    _HitenBaseInterface[
        _ConnectionConfig,
        _ConnectionProblem,
        ConnectionResults,
        list,
    ]
):
    """Provide an interface for accessing manifold data in connection discovery.

    This class provides a clean interface for extracting synodic section
    intersections from manifolds. It handles the conversion between manifold
    trajectory data and the section intersection data needed for connection
    analysis.

    Notes
    -----
    This interface serves as an adapter between the manifold system and
    the connection discovery algorithms. It encapsulates the logic for:
    
    - Validating that manifold data is available
    - Converting manifold trajectories to synodic section intersections
    - Handling different crossing direction filters
    - Providing appropriate error messages for invalid states

    The interface ensures that manifolds are properly computed before
    attempting to extract section data, preventing runtime errors in
    the connection discovery process.

    Examples
    --------
    >>> from hiten.system.manifold import Manifold
    >>> from hiten.algorithms.poincare.synodic.config import _SynodicMapConfig
    >>> 
    >>> # Assuming manifold is computed
    >>> interface = _ManifoldInterface()
    >>> section_cfg = _SynodicMapConfig(x=0.8)
    >>> section = interface.to_section(manifold=computed_manifold, config=section_cfg, direction=1)
    >>> print(f"Found {len(section.points)} intersection points")

    See Also
    --------
    :class:`~hiten.system.manifold.Manifold`
        Manifold class that this interface wraps.
    :class:`~hiten.algorithms.poincare.synodic.base.SynodicMap`
        Synodic map used for computing section intersections.
    :class:`~hiten.algorithms.connections.engine._ConnectionProblem`
        Problem specification that uses these interfaces.
    """

    def __init__(self) -> None:
        super().__init__()

    def create_problem(
        self,
        *,
        domain_obj: tuple["Manifold", "Manifold"] | None = None,
        config: _ConnectionConfig | None = None,
    ) -> _ConnectionProblem:
        """Create a connection problem specification.
        
        Parameters
        ----------
        domain_obj : tuple of :class:`~hiten.system.manifold.Manifold`
            The source and target manifolds.
        config : :class:`~hiten.algorithms.connections.config._ConnectionConfig`
            The configuration for the connection problem.

        Returns
        -------
        :class:`~hiten.algorithms.connections.types._ConnectionProblem`
            The connection problem.
        """
        if domain_obj is None:
            raise ValueError("domain_obj (source, target) is required")
        if config is None:
            raise ValueError("config is required")
        
        source, target = domain_obj
        
        return _ConnectionProblem(
            source=source,
            target=target,
            section_axis=config.section.section_axis,
            section_offset=config.section.section_offset,
            plane_coords=config.section.plane_coords,
            direction=config.direction,
            n_workers=config.n_workers,
            delta_v_tol=config.delta_v_tol,
            ballistic_tol=config.ballistic_tol,
            eps2d=config.eps2d,
        )

    def to_backend_inputs(self, problem: _ConnectionProblem) -> tuple:
        """Convert problem to backend inputs.
        
        Parameters
        ----------
        problem : :class:`~hiten.algorithms.connections.types._ConnectionProblem`
            The problem to convert to backend inputs.

        Returns
        -------
        :class:`~hiten.algorithms.types.core._BackendCall`
            The backend inputs.
        """
        # Create section config from problem parameters
        section_config = _SynodicMapConfig(
            section_axis=problem.section_axis,
            section_offset=problem.section_offset,
            plane_coords=problem.plane_coords,
            direction=problem.direction
        )
        
        # Extract section data from both manifolds
        pu, Xu, traj_indices_u = self.to_numeric(problem.source, section_config, direction=problem.direction)
        ps, Xs, traj_indices_s = self.to_numeric(problem.target, section_config, direction=problem.direction)
        
        # Extract search parameters from the problem
        eps = float(problem.eps2d)
        dv_tol = float(problem.delta_v_tol)
        bal_tol = float(problem.ballistic_tol)
        
        from hiten.algorithms.types.core import _BackendCall
        return _BackendCall(
            args=(pu, ps, Xu, Xs, traj_indices_u, traj_indices_s),
            kwargs={"eps": eps, "dv_tol": dv_tol, "bal_tol": bal_tol}
        )

    def to_results(self, outputs: list, *, problem: _ConnectionProblem, domain_payload=None) -> ConnectionResults:
        """Convert backend outputs to connection results
        
        This method converts the backend outputs to connection results.

        Parameters
        ----------
        outputs : list[Any]
            The backend outputs to convert to connection results.
        problem : :class:`~hiten.algorithms.connections.types._ConnectionProblem`
            The problem to convert to connection results.
        domain_payload : Any, optional
            The domain payload to convert to connection results.

        Returns
        -------
        :class:`~hiten.algorithms.connections.types.ConnectionResults`
            The connection results.
        """
        return ConnectionResults(outputs)

    def to_section(
        self,
        manifold: "Manifold",
        config: _SynodicMapConfig | None = None,
        *,
        direction: Literal[1, -1, None] | None = None,
    ) -> _Section:
        """Extract synodic section intersection data from the manifold.

        This method computes the intersections between the manifold trajectories
        and a specified synodic section, returning the intersection points,
        states, and timing information needed for connection analysis.

        Parameters
        ----------
        manifold : :class:`~hiten.system.manifold.Manifold`
            The manifold object containing computed trajectory data.
        config : :class:`~hiten.algorithms.poincare.synodic.config._SynodicMapConfig`, optional
            Configuration for the synodic section geometry and detection settings.
            Includes section axis, offset, coordinate system, interpolation method,
            and numerical tolerances. If not provided, default settings are used.
        direction : {1, -1, None}, optional
            Filter for section crossing direction. 1 selects positive crossings
            (increasing coordinate), -1 selects negative crossings (decreasing
            coordinate), None accepts both directions (default: None).

        Returns
        -------
        :class:`~hiten.algorithms.poincare.core.types._Section`
            Section object containing intersection data with attributes:
            
            - points : 2D coordinates on the section plane
            - states : 6D phase space states at intersections  
            - times : intersection times along trajectories
            - labels : coordinate labels for the section plane

        Raises
        ------
        :class:`~hiten.algorithms.types.exceptions.EngineError`
            If the manifold has not been computed (manifold.result is None).
            Call manifold.compute() before using this method.

        Notes
        -----
        This method delegates to :class:`~hiten.system.maps.synodic.SynodicMap`
        for the actual intersection computation. The synodic map handles:
        
        - Trajectory interpolation and root finding
        - Section crossing detection and refinement
        - Coordinate transformation to section plane
        - Deduplication of nearby intersection points
        
        The resulting section data is suitable for geometric analysis in
        the connection discovery algorithms.

        Examples
        --------
        >>> # Basic usage with default section
        >>> section = interface.to_section(manifold)
        >>> 
        >>> # Custom section at x = 0.8 with positive crossings only
        >>> from hiten.algorithms.poincare.synodic.config import _SynodicMapConfig
        >>> config = _SynodicMapConfig(
        ...     section_axis="x",
        ...     section_offset=0.8,
        ...     plane_coords=("y", "z")
        ... )
        >>> section = interface.to_section(manifold, config=config, direction=1)
        >>> print(f"Points: {section.points.shape}")
        >>> print(f"States: {section.states.shape}")

        See Also
        --------
        :class:`~hiten.system.maps.synodic.SynodicMap`
            Underlying synodic map implementation.
        :class:`~hiten.algorithms.poincare.synodic.config._SynodicMapConfig`
            Configuration class for section parameters.
        :meth:`~hiten.system.manifold.Manifold.compute`
            Method to compute manifold data before section extraction.
        """

        if manifold.result is None:
            raise EngineError("Manifold must be computed before extracting section hits")

        # Create synodic map from the manifold
        synodic_map = SynodicMap(manifold)
        
        # Extract configuration parameters
        if config is not None:
            section_axis = config.section_axis
            section_offset = config.section_offset
            plane_coords = config.plane_coords
            overrides = {
                "interp_kind": config.interp_kind,
                "segment_refine": config.segment_refine,
                "newton_max_iter": config.newton_max_iter,
                "tol_on_surface": config.tol_on_surface,
                "dedup_time_tol": config.dedup_time_tol,
                "dedup_point_tol": config.dedup_point_tol,
                "max_hits_per_traj": config.max_hits_per_traj,
                "n_workers": config.n_workers,
            }
        else:
            # Use default configuration
            section_axis = "x"
            section_offset = 0.0
            plane_coords = ("y", "vy")
            overrides = {}
        
        # Compute the section
        synodic_map.compute(
            section_axis=section_axis,
            section_offset=section_offset,
            plane_coords=plane_coords,
            direction=direction,
            overrides=overrides
        )
        
        # Get the section data using the same ID format as the dynamics service
        section_id = f"{section_axis}_{section_offset}_{plane_coords[0]}_{plane_coords[1]}_{direction}"
        return synodic_map.get_section(section_id)

    def to_numeric(self, manifold: "Manifold", config: _SynodicMapConfig | None = None, *, direction: Literal[1, -1, None] | None = None):
        """Return (points2d, states6d, trajectory_indices) arrays for this manifold on a section.

        Parameters
        ----------
        manifold : :class:`~hiten.system.manifold.Manifold`
            The manifold object containing computed trajectory data.
        config : :class:`~hiten.algorithms.poincare.synodic.config._SynodicMapConfig`, optional
            Configuration for the synodic section geometry and detection settings.
        direction : {1, -1, None}, optional
            Filter for section crossing direction. 1 selects positive crossings
            (increasing coordinate), -1 selects negative crossings (decreasing
            coordinate), None accepts both directions (default: None).

        Returns
        -------
        tuple
            A tuple containing (points2d, states6d, trajectory_indices) where:
            - points2d : ndarray, shape (n, 2)
                2D coordinates on the section plane
            - states6d : ndarray, shape (n, 6) 
                6D phase space states at intersections
            - trajectory_indices : ndarray, shape (n,) or None
                Indices of trajectories that produced each intersection point
        """
        sec = self.to_section(manifold=manifold, config=config, direction=direction)
        trajectory_indices = getattr(sec, 'trajectory_indices', None)
        if trajectory_indices is not None:
            trajectory_indices = np.asarray(trajectory_indices, dtype=int)
        return (np.asarray(sec.points, dtype=float), np.asarray(sec.states, dtype=float), trajectory_indices)
