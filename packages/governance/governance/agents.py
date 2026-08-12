"""Governance agents implementation."""
from __future__ import annotations

from sovereign.agents import BaseAgent

UNVERIFIED_MARKERS = ("100%", "cure", "guaranteed", "undetectable",
                      "stealth", "fabricate", "bypass", "weaponize")


class OrchestratorAgent(BaseAgent):
    """Dispatch coordination: accept a batch, route to agents by role."""

    def __init__(self, agent_id: str = "orchestrator", role: str = "orchestrator"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        batch = task.get("tasks", [])
        routed = {}
        for item in batch:
            role = item.get("role", "reasoner")
            routed.setdefault(role, []).append(item.get("id", "?"))
        return {"agent": self.agent_id, "routed": routed,
                "total": len(batch), "status": "dispatched"}


class GatekeeperAgent(BaseAgent):
    """Policy gate: reject unverified medical/scientific claims and
    permission violations. The enforcement point for the claims register."""

    def __init__(self, agent_id: str = "gatekeeper", role: str = "gatekeeper"):
        super().__init__(agent_id, role)

    def check_claims(self, text: str) -> dict:
        text_l = text.lower()
        hits = [m for m in UNVERIFIED_MARKERS if m in text_l]
        allowed = len(hits) == 0
        return {"allowed": allowed, "flagged": hits,
                "reason": ("contains unverified claim markers: "
                           + ", ".join(hits)) if hits else "pass"}

    def check_acl(self, caller_role: str, resource: str) -> bool:
        # admin overrides; agents can read-only; guests nothing
        if caller_role == "admin":
            return True
        if caller_role == "agent":
            return not resource.startswith("admin:")
        return False

    def execute(self, task: dict) -> dict:
        text = task.get("text", "")
        claims = self.check_claims(text)
        acl_ok = self.check_acl(task.get("caller_role", "guest"),
                                task.get("resource", ""))
        return {"agent": self.agent_id, "claims_gate": claims,
                "acl_gate": {"allowed": acl_ok},
                "status": "allowed" if (claims["allowed"] and acl_ok) else "blocked"}


class WatcherAgent(BaseAgent):
    """Health watch: heartbeat staleness, spec file counts, test status."""

    def __init__(self, agent_id: str = "watcher", role: str = "watcher"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        staleness = task.get("stale_entities", [])
        spec = task.get("spec_counts", {})
        tests = task.get("tests", {})
        ok = (len(staleness) == 0
              and all(v >= 1 for v in spec.values())
              and tests.get("passed", 0) >= 0
              and tests.get("failed", 1) == 0)
        return {"agent": self.agent_id, "stale": staleness,
                "spec": spec, "tests": tests,
                "status": "healthy" if ok else "attention"}


class TallymanAgent(BaseAgent):
    """Accounting: aggregate counts and cost metrics."""

    def __init__(self, agent_id: str = "tallyman", role: str = "tallyman"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        data = task.get("metrics", {})
        total = sum(data.values())
        return {"agent": self.agent_id, "metrics": data, "total": total,
                "status": "tallied"}


class ChatAgent(BaseAgent):
    """Conversational router: intent -> governance agent or direct reply."""

    def __init__(self, agent_id: str = "chat", role: str = "chat"):
        super().__init__(agent_id, role)

    def execute(self, task: dict) -> dict:
        msg = str(task.get("message", "")).lower()
        if any(k in msg for k in ("gate", "claim", "policy")):
            intent = "gatekeeper"
        elif any(k in msg for k in ("watch", "health", "status")):
            intent = "watcher"
        elif any(k in msg for k in ("tally", "count", "metrics")):
            intent = "tallyman"
        elif any(k in msg for k in ("dispatch", "route", "orchestrate")):
            intent = "orchestrator"
        else:
            intent = "direct"
        return {"agent": self.agent_id, "intent": intent,
                "reply": f"routed to {intent} (operator dialogue)"}
