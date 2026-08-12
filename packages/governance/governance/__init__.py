"""Governance agents — platform oversight layer (sovereign BaseAgent based).

  OrchestratorAgent - task dispatch coordination, pipeline fan-out
  GatekeeperAgent  - policy gate: blocks UNVERIFIED claims, enforces ACL
  WatcherAgent     - health watch: heartbeat staleness, spec integrity,
                     test status
  TallymanAgent    - accounting: task/test/claim counts, cost metrics
  ChatAgent        - conversational router for operator dialogue

All agents are deterministic decision-support; the Gatekeeper is the
enforcement point for the claims-register discipline.
"""
from .agents import (ChatAgent, GatekeeperAgent, OrchestratorAgent,
                     TallymanAgent, WatcherAgent)

__all__ = ["OrchestratorAgent", "GatekeeperAgent", "WatcherAgent",
           "TallymanAgent", "ChatAgent"]
