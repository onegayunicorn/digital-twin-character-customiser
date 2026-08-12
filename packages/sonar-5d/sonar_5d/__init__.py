"""sonar-5d — crystal-mesh geometry + 5D sonar sweep (x, y, z, time, intensity).

  mesh  - diamond-cubic lattice: atom positions, bond edges, OBJ export
  sweep - sonar echo model: intensity = A exp(-r^2/sigma^2) sin(2*pi*f*t - k*r)
          sampled over lattice planes (3D + time + intensity = 5D)

Simulation/visualization only — geometry facts, no physical claims.
"""
from .mesh import diamond_cubic_lattice, lattice_metrics, export_obj
from .sweep import sonar_field, sweep_plane, peak_response

__all__ = ["diamond_cubic_lattice", "lattice_metrics", "export_obj",
           "sonar_field", "sweep_plane", "peak_response"]
