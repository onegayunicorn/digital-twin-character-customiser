"""Base agent + factory with lifecycle state machine."""
from __future__ import annotations

STATES = ("idle", "ready", "busy", "done", "failed")


class BaseAgent:
    def __init__(self, agent_id: str, role: str):
        self.agent_id = agent_id
        self.role = role
        self.state = "idle"

    def transition(self, target: str) -> None:
        if target not in STATES:
            raise ValueError(f"invalid state {target!r}")
        if target == "busy" and self.state != "ready":
            raise ValueError(f"cannot go busy from {self.state}")
        if target == "ready" and self.state not in ("idle", "done", "failed"):
            raise ValueError(f"cannot go ready from {self.state}")
        self.state = target

    def execute(self, task: dict) -> dict:
        """Execute a task; returns a result dict. Override in subclasses."""
        return {"agent": self.agent_id, "task": task.get("id"), "status": "ok"}


class ReasonerAgent(BaseAgent):
    def execute(self, task: dict) -> dict:
        return {**super().execute(task), "mode": "reasoner", "summary": task.get("prompt", "")[:80]}


class CoderAgent(BaseAgent):
    def execute(self, task: dict) -> dict:
        return {**super().execute(task), "mode": "coder", "lines": len(str(task.get("code", "")))}


class ToolAgent(BaseAgent):
    def execute(self, task: dict) -> dict:
        return {**super().execute(task), "mode": "tool", "tool": task.get("tool", "none")}


class CoordinatorAgent(BaseAgent):
    def execute(self, task: dict) -> dict:
        subtasks = task.get("subtasks", [])
        return {**super().execute(task), "mode": "coordinator", "decomposed": len(subtasks)}


class AgentFactory:
    ROLES = {
        "reasoner": ReasonerAgent,
        "coder": CoderAgent,
        "tool": ToolAgent,
        "coordinator": CoordinatorAgent,
    }

    @classmethod
    def create(cls, agent_id: str, role: str) -> BaseAgent:
        cls_ = cls.ROLES.get(role)
        if cls_ is None:
            raise ValueError(f"unknown role {role!r}; roles: {sorted(cls.ROLES)}")
        return cls_(agent_id, role)
