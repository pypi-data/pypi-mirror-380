"""Provide a user-facing interface for discovering connections between manifolds in CR3BP.

This module provides the main :class:`~hiten.algorithms.connections.base.ConnectionPipeline`
class, which serves as a high-level facade for the connection discovery algorithm. It wraps 
the lower-level connection engine and provides convenient methods for solving connection 
problemsand visualizing results.

The connection discovery process finds ballistic and impulsive transfers between
two manifolds by intersecting them with a common synodic section and analyzing
the geometric and dynamical properties of potential transfer points.

All coordinates are in nondimensional CR3BP rotating-frame units.

See Also
--------
:mod:`~hiten.algorithms.connections.engine`
    Lower-level connection engine implementation.
:mod:`~hiten.algorithms.connections.results`
    Result classes for connection data.
:mod:`~hiten.system.manifold`
    Manifold classes for CR3BP invariant structures.
"""

from typing import TYPE_CHECKING, Generic, Optional

import numpy as np

from hiten.algorithms.types.core import (ConfigT, DomainT, InterfaceT, ResultT,
                                         _HitenBaseFacade)
from hiten.algorithms.types.exceptions import EngineError
from hiten.utils.plots import plot_poincare_connections_map

if TYPE_CHECKING:
    from hiten.algorithms.connections.engine import _ConnectionEngine
    from hiten.algorithms.connections.types import (Connections,
                                                    _ConnectionResult)

class ConnectionPipeline(_HitenBaseFacade, Generic[DomainT, InterfaceT, ConfigT, ResultT]):
    """Provide a user-facing facade for connection discovery and plotting in CR3BP.

    This class provides a high-level interface for discovering ballistic and
    impulsive transfers between manifolds in the Circular Restricted Three-Body
    Problem. It wraps the lower-level connection engine and provides convenient
    methods for solving connection problems and visualizing results.

    Parameters
    ----------
    config : :class:`~hiten.algorithms.connections.config._ConnectionConfig`
        Configuration object containing section, direction, and search parameters.
    interface : :class:`~hiten.algorithms.connections.interfaces._ManifoldInterface`
        Interface for translating between domain objects and backend inputs.
    engine : :class:`~hiten.algorithms.connections.engine._ConnectionEngine`, optional
        Engine instance to use for connection discovery. If None, must be set later
        or use with_default_engine() factory method.

    Examples
    --------

    >>> from hiten.algorithms.connections import ConnectionPipeline, SearchConfig
    >>> from hiten.algorithms.poincare import SynodicMapConfig
    >>> from hiten.system import System
    >>>
    >>> system = System.from_bodies("earth", "moon")
    >>> mu = system.mu

    >>> l1 = system.get_libration_point(1)
    >>> l2 = system.get_libration_point(2)
    >>> 
    >>> halo_l1 = l1.create_orbit('halo', amplitude_z=0.5, zenith='southern')
    >>> halo_l1.correct()
    >>> halo_l1.propagate()
    >>> 
    >>> halo_l2 = l2.create_orbit('halo', amplitude_z=0.3663368, zenith='northern')
    >>> halo_l2.correct()
    >>> halo_l2.propagate()
    >>> 
    >>> manifold_l1 = halo_l1.manifold(stable=True, direction='positive')
    >>> manifold_l1.compute(integration_fraction=0.9, step=0.005)
    >>> 
    >>> manifold_l2 = halo_l2.manifold(stable=False, direction='negative')
    >>> manifold_l2.compute(integration_fraction=1.0, step=0.005)
    >>> 
    >>> section_cfg = SynodicMapConfig(
    >>>     section_axis="x",
    >>>     section_offset=1 - mu,
    >>>     plane_coords=("y", "z"),
    >>>     interp_kind="cubic",
    >>>     segment_refine=30,
    >>>     tol_on_surface=1e-9,
    >>>     dedup_time_tol=1e-9,
    >>>     dedup_point_tol=1e-9,
    >>>     max_hits_per_traj=None,
    >>>     n_workers=None,
    >>> )
    >>> 
    >>> conn = ConnectionPipeline.with_default_engine(
    >>>     config=_ConnectionConfig(
    >>>         section=section_cfg,
    >>>         direction=None,
    >>>         delta_v_tol=1,
    >>>         ballistic_tol=1e-8,
    >>>         eps2d=1e-3,
    >>>     )
    >>> )
    >>> 
    >>> conn.solve(manifold_l1, manifold_l2)
    >>> print(conn)
    >>> conn.plot(dark_mode=True)

    Notes
    -----
    The connection algorithm works by:
    1. Intersecting both manifolds with the specified synodic section
    2. Finding geometrically close points between the two intersection sets
    3. Refining matches using local segment geometry
    4. Computing Delta-V requirements and classifying transfers

    See Also
    --------
    :class:`~hiten.algorithms.connections.engine._ConnectionEngine`
        Lower-level engine that performs the actual computation.
    :class:`~hiten.algorithms.connections.types.Connections`
        Container for connection results with convenient access methods.
    """

    def __init__(self, config: ConfigT, interface: InterfaceT, engine: "_ConnectionEngine" = None) -> None:
        super().__init__(config, interface, engine)
        
        self._last_source = None
        self._last_target = None
        self._last_results: list["_ConnectionResult"] | None = None

    @classmethod
    def with_default_engine(cls, *, config: ConfigT, interface: Optional[InterfaceT] = None) -> "ConnectionPipeline[DomainT, ConfigT, ResultT]":
        """Create a facade instance with a default engine (factory).

        The default engine uses :class:`~hiten.algorithms.connections.backends._ConnectionsBackend`.

        Parameters
        ----------
        config : :class:`~hiten.algorithms.connections.config._ConnectionConfig`
            Configuration object containing section, direction, and search parameters.
        interface : :class:`~hiten.algorithms.connections.interfaces._ManifoldInterface`, optional
            Interface for translating between domain objects and backend inputs.
            If None, uses the default _ManifoldInterface.

        Returns
        -------
        :class:`~hiten.algorithms.connections.base.ConnectionPipeline`
            A connection facade instance with a default engine injected.
        """
        from hiten.algorithms.connections.backends import _ConnectionsBackend
        from hiten.algorithms.connections.engine import _ConnectionEngine
        from hiten.algorithms.connections.interfaces import _ManifoldInterface
        backend = _ConnectionsBackend()
        intf = interface or _ManifoldInterface()
        engine = _ConnectionEngine(backend=backend, interface=intf)
        return cls(config, intf, engine)

    def solve(self, source: DomainT, target: DomainT, *, override: bool = False, **kwargs) -> "Connections":
        """Discover connections between two manifolds.

        This method finds ballistic and impulsive transfers between the source
        and target manifolds by intersecting them with the configured synodic
        section and analyzing potential connection points.

        Parameters
        ----------
        source : :class:`~hiten.system.manifold.Manifold`
            Source manifold (e.g., unstable manifold of a periodic orbit).
        target : :class:`~hiten.system.manifold.Manifold`
            Target manifold (e.g., stable manifold of another periodic orbit).
        override : bool, default=False
            Whether to override configuration with provided kwargs.
        **kwargs
            Configuration parameters to update if override=True.

        Returns
        -------
        :class:`~hiten.algorithms.connections.types.Connections`
            ConnectionPipeline results sorted by increasing Delta-V requirement.
            Each result contains transfer type, Delta-V, intersection points,
            and 6D states at the connection.

        Notes
        -----
        Results are cached internally for convenient access via the 
        :attr:`~hiten.algorithms.connections.base.ConnectionPipeline.results`
        property and for plotting with the
        :meth:`~hiten.algorithms.connections.base.ConnectionPipeline.plot` method.

        The algorithm performs these steps:
        1. Convert manifolds to section interfaces
        2. Create connection problem specification
        3. Delegate to :class:`~hiten.algorithms.connections.engine._ConnectionEngine`
        4. Cache results for later use

        Examples
        --------
        >>> results = connection.solve(unstable_manifold, stable_manifold)
        >>> print(results)
        """
        domain_obj = (source, target)
        
        problem = self._create_problem(domain_obj=domain_obj, override=override, **kwargs)
        engine = self._get_engine()
        engine_result = engine.solve(problem)
        records = engine_result.connections
        self._last_source = source
        self._last_target = target
        self._last_results = records
        return engine_result.to_results()

    @property
    def results(self) -> "Connections":
        """Access the latest connection results with convenient formatting.

        Returns
        -------
        :class:`~hiten.algorithms.connections.types.Connections`
            A view over the latest results with friendly printing and
            convenient access methods. Returns an empty view if 
            :meth:`~hiten.algorithms.connections.base.ConnectionPipeline.solve`
            has not been called yet.

        Notes
        -----
        This property provides access to cached results from the most recent
        call to :meth:`~hiten.algorithms.connections.base.ConnectionPipeline.solve`. 
        The :class:`~hiten.algorithms.connections.types.Connections` 
        wrapper provides enhanced formatting and filtering capabilities.

        Examples
        --------
        >>> connection.solve(source, target)
        >>> print(connection.results)  # Pretty-printed summary
        >>> ballistic = connection.results.ballistic  # Filter by type
        """
        from hiten.algorithms.connections.types import Connections
        return Connections(self._last_results)

    def plot(self, **kwargs):
        """Create a visualization of the connection results on the synodic section.

        This method generates a Poincare map showing the intersection points
        of both manifolds with the synodic section, highlighting discovered
        connections with color-coded Delta-V values.

        Parameters
        ----------
        **kwargs
            Additional keyword arguments passed to
            :func:`~hiten.utils.plots.plot_poincare_connections_map`.
            Common options include figure size, color maps, and styling parameters.

        Returns
        -------
        matplotlib figure or axes
            The plot object, which can be further customized or saved.

        Raises
        ------
        ValueError
            If :meth:`~hiten.algorithms.connections.base.ConnectionPipeline.solve` 
            has not been called yet (no cached data to plot).

        Notes
        -----
        The plot shows:
        - Source manifold intersection points (typically unstable manifold)
        - Target manifold intersection points (typically stable manifold)
        - ConnectionPipeline points with color-coded Delta-V requirements
        - Section coordinate labels and axes

        Examples
        --------
        >>> connection.solve(source, target)
        >>> fig = connection.plot(figsize=(10, 8), cmap='viridis')
        >>> fig.savefig('connections.png')

        See Also
        --------
        :func:`~hiten.utils.plots.plot_poincare_connections_map`
            Underlying plotting function with detailed parameter documentation.
        """
        # Use cached artifacts; user should call solve() first
        if self._last_source is None or self._last_target is None:
            raise EngineError("Nothing to plot: call solve(source, target) first.")

        manifold_if = self._get_interface()
        config = self._get_config()

        # Build section hits for both manifolds on the configured synodic section
        sec_u = manifold_if.to_section(manifold=self._last_source, config=config.section, direction=config.direction)
        sec_s = manifold_if.to_section(manifold=self._last_target, config=config.section, direction=config.direction)

        pts_u = np.asarray(sec_u.points, dtype=float)
        pts_s = np.asarray(sec_s.points, dtype=float)
        labels = tuple(sec_u.labels)

        # Use cached results
        res_list = self._last_results or []

        if res_list:
            match_pts = np.asarray([r.point2d for r in res_list], dtype=float)
            match_vals = np.asarray([r.delta_v for r in res_list], dtype=float)
        else:
            match_pts = None
            match_vals = None

        return plot_poincare_connections_map(
            points_src=pts_u,
            points_tgt=pts_s,
            labels=labels,
            match_points=match_pts,
            match_values=match_vals,
            **kwargs,
        )

    def _validate_config(self, config: ConfigT) -> None:
        """Validate the configuration object.
        
        This method can be overridden by concrete facades to perform
        domain-specific configuration validation.
        
        Parameters
        ----------
        config : :class:`~hiten.algorithms.connections.config._ConnectionConfig`
            The configuration object to validate.
            
        Raises
        ------
        ValueError
            If the configuration is invalid.
        """
        super()._validate_config(config)
        
        if hasattr(config, 'section') and config.section is None:
            raise ValueError("Section configuration is required")
        if hasattr(config, 'delta_v_tol') and config.delta_v_tol <= 0:
            raise ValueError("Delta-V tolerance must be positive")
        if hasattr(config, 'ballistic_tol') and config.ballistic_tol <= 0:
            raise ValueError("Ballistic tolerance must be positive")
        if hasattr(config, 'eps2d') and config.eps2d <= 0:
            raise ValueError("2D epsilon must be positive")