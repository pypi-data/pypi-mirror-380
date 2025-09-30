"""
Interface classes for synodic Poincare map computation.

This module provides interface classes that abstract synodic Poincare
map computation for the synodic module. These interfaces handle the
conversion between synodic map configuration and the engine interface.
"""

from typing import Literal, Sequence, Tuple

import numpy as np

from hiten.algorithms.poincare.core.interfaces import (_PoincareBaseInterface,
                                                       _SectionInterface)
from hiten.algorithms.poincare.synodic.config import _SynodicMapConfig
from hiten.algorithms.poincare.synodic.events import _AffinePlaneEvent
from hiten.algorithms.poincare.synodic.types import (SynodicMapResults,
                                                     _SynodicMapProblem)
from hiten.algorithms.types.core import _BackendCall
from hiten.algorithms.types.states import SynodicState


class _SynodicSectionInterface(_SectionInterface):
    """Stateless section interface for synodic affine hyperplanes."""

    @staticmethod
    def axis_normal(axis: str | int) -> np.ndarray:
        """Get normal vector for a given axis."""
        normal = np.zeros(6, dtype=float)
        if isinstance(axis, str):
            idx = int(SynodicState[axis.upper()])
        else:
            idx = int(axis)
        normal[idx] = 1.0
        return normal

    @staticmethod
    def build_event(normal: np.ndarray, offset: float, *, direction: Literal[1, -1, None] = None) -> _AffinePlaneEvent:
        """Build an affine plane event from normal, offset, and direction."""
        return _AffinePlaneEvent(normal=normal, offset=offset, direction=direction)

    @staticmethod
    def coordinate_index(axis: str) -> int:
        """Get coordinate index for a given axis."""
        try:
            return int(SynodicState[axis.upper()])
        except KeyError as exc:
            raise ValueError(f"Unsupported synodic axis '{axis}'") from exc

    @staticmethod
    def validate_normal(normal: Sequence[float]) -> np.ndarray:
        """Validate and convert normal vector to numpy array."""
        n_arr = np.asarray(normal, dtype=float)
        if n_arr.ndim != 1 or n_arr.size != 6 or not np.all(np.isfinite(n_arr)):
            raise ValueError("normal must be a finite 1-D array of length 6")
        return n_arr

    @staticmethod
    def validate_plane_coords(plane_coords: Tuple[str, str]) -> Tuple[str, str]:
        """Validate and convert plane coordinates to tuple of strings."""
        if not (isinstance(plane_coords, tuple) and len(plane_coords) == 2):
            raise ValueError("plane_coords must be a tuple of two axis names")
        return (str(plane_coords[0]), str(plane_coords[1]))

    @staticmethod
    def create_section_config(
        *,
        normal: Sequence[float] | np.ndarray,
        offset: float = 0.0,
        plane_coords: Tuple[str, str] = ("y", "vy"),
    ) -> dict:
        """Create a section configuration dictionary from parameters.
        
        This method provides a stateless way to create section configuration
        data without instantiating a class. Returns a dictionary with the
        validated parameters.
        """
        n_arr = _SynodicSectionInterface.validate_normal(normal)
        plane_coords_validated = _SynodicSectionInterface.validate_plane_coords(plane_coords)
        
        return {
            "normal": n_arr,
            "offset": float(offset),
            "plane_coords": plane_coords_validated,
        }


class _SynodicInterface(
    _PoincareBaseInterface[
        _SynodicMapConfig, 
        _SynodicMapProblem, 
        SynodicMapResults, 
        Tuple[np.ndarray, np.ndarray, np.ndarray | None]
    ]
):

    def __init__(self) -> None:
        super().__init__()

    def create_problem(
        self,
        *,
        domain_obj,
        config: _SynodicMapConfig,
    ) -> _SynodicMapProblem:
        normal = _SynodicSectionInterface.axis_normal(config.section_axis)
        offset = config.section_offset
        plane_coords = config.plane_coords
        direction = config.direction
        trajectories = [traj.as_arrays() for traj in domain_obj.trajectories]
        return _SynodicMapProblem(
            plane_coords=plane_coords,
            direction=direction,
            n_workers=config.n_workers or 1,
            normal=normal,
            offset=offset,
            trajectories=trajectories,
            interp_kind=config.interp_kind,
            segment_refine=config.segment_refine,
            tol_on_surface=config.tol_on_surface,
            dedup_time_tol=config.dedup_time_tol,
            dedup_point_tol=config.dedup_point_tol,
            max_hits_per_traj=config.max_hits_per_traj,
            newton_max_iter=config.newton_max_iter,
        )

    def to_backend_inputs(self, problem: _SynodicMapProblem):
        return _BackendCall(kwargs={"trajectories": problem.trajectories, "direction": problem.direction})

    def to_results(self, outputs, *, problem: _SynodicMapProblem) -> SynodicMapResults:
        points, states, times, trajectory_indices = outputs
        plane_coords = problem.plane_coords
        return SynodicMapResults(points, states, plane_coords, times, trajectory_indices)
