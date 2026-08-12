"""Crystal Planet Formation (CPF) simulation.

Models crystal nucleation → growth → accretion in a gradient-driven medium
(the 'bipolar sun': hot/light source vs cold/dark void):

  Thermal field   - analytic gradient from sun to void
  Nucleation      - P_nucleate = exp(-dG* / (kB * T))   (classical nucleation theory)
  Growth          - mass += rate * local_density (feedback loop)
  Stabilization   - proto-planet flag when crystal mass fraction is reached

HONESTY: implements the thermodynamics (CNT is established physics); the
document's teleological framing ('crystals calculate their own evolution')
is not reproduced.
"""
from .engine import CPFEngine, nucleation_probability

__all__ = ["CPFEngine", "nucleation_probability"]
