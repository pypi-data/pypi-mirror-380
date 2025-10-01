"""Example script: Detecting heteroclinic connections between two manifolds.

This example demonstrates how to use the ConnectionPipeline class with the to find impulsive transfers between
manifolds in the CR3BP.

Run with
    python examples/heteroclinic_connection.py
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from hiten.algorithms.connections import ConnectionPipeline
from hiten.algorithms.connections.config import _ConnectionConfig
from hiten.algorithms.poincare import SynodicMapConfig
from hiten.system import System


def main() -> None:
    system = System.from_bodies("earth", "moon")
    mu = system.mu

    l1 = system.get_libration_point(1)
    l2 = system.get_libration_point(2)

    halo_l1 = l1.create_orbit('halo', amplitude_z=0.5, zenith='southern')
    halo_l1.correct()
    halo_l1.propagate()

    halo_l2 = l2.create_orbit('halo', amplitude_z=0.3663368, zenith='northern')
    halo_l2.correct()
    halo_l2.propagate()

    manifold_l1 = halo_l1.manifold(stable=True, direction='positive')
    manifold_l1.compute(integration_fraction=0.9, step=0.005)

    manifold_l2 = halo_l2.manifold(stable=False, direction='negative')
    manifold_l2.compute(integration_fraction=1.0, step=0.005)

    section_cfg = SynodicMapConfig(
        section_axis="x",
        section_offset=1 - mu,
        plane_coords=("y", "z"),
        interp_kind="cubic",
        segment_refine=30,
        tol_on_surface=1e-9,
        dedup_time_tol=1e-9,
        dedup_point_tol=1e-9,
        max_hits_per_traj=None,
        n_workers=None,
    )

    # Create unified configuration with all parameters in one object
    config = _ConnectionConfig(
        section=section_cfg,        # Synodic section configuration
        direction=-1,                # Crossing direction (None = both directions)
        delta_v_tol=1,             # Maximum Delta-V tolerance
        ballistic_tol=1e-8,        # Threshold for ballistic classification
        eps2d=1e-3,                # 2D pairing radius
    )
    
    # Create connection using the factory method with unified config
    conn = ConnectionPipeline.with_default_engine(config=config)

    result = conn.solve(manifold_l1, manifold_l2)

    print(result)

    conn.plot(dark_mode=True)

    conn.plot_connection(dark_mode=True)


if __name__ == "__main__":
    main()