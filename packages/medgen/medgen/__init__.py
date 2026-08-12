"""medgen — medical-genetics simulation toolkit (research/simulation only).

Modules:
  dmd_mutations    - DMD nonsense-mutation reference table + stop-codon analysis
  repair_sim       - mechanism-level repair-strategy simulation (NO cure claims)
  cancer_dynamics  - Gompertz tumor growth + therapy-response simulation

HONESTY NOTICE: every output carries clinical_claim_level. Simulations model
mechanisms; they do NOT establish clinical efficacy, safety, or regulatory
acceptability. Nothing here is medical advice or a treatment claim.
"""
from . import dmd_mutations, repair_sim, cancer_dynamics

__all__ = ["dmd_mutations", "repair_sim", "cancer_dynamics"]
