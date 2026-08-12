"""Healthcare agency agents — decision-support only.

Agents (built on the sovereign orchestrator BaseAgent):
  HospitalAgent    - patient-flow triage scoring (vitals -> priority band)
  DoctorAgent      - case review: mutation -> repair-mechanism simulation
                     (via medgen), with mandatory disclaimer
  ResearcherAgent  - literature/trial matching against a registry stub

SAFETY CONTRACT: every output carries clinical_claim_level="none" and
decision_support_only=true. These agents never issue treatment decisions,
diagnoses, or efficacy claims — they organize information for humans.
"""
from .agents import HospitalAgent, DoctorAgent, ResearcherAgent

__all__ = ["HospitalAgent", "DoctorAgent", "ResearcherAgent"]
