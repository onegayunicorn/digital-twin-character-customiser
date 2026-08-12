"""Agent handshake registry: hello/ack registration with heartbeats."""
from __future__ import annotations

import secrets
import time


class HandshakeRegistry:
    def __init__(self, stale_after_s: float = 10.0):
        self.stale_after = stale_after_s
        self._agents: dict[str, dict] = {}

    def hello(self, agent_id: str, role: str, token: str | None = None) -> dict:
        """Register/refresh an agent; returns an ack with a fresh token."""
        if token is None:
            token = secrets.token_hex(8)
        self._agents[agent_id] = {"role": role, "token": token,
                                  "last_beat": time.time()}
        return {"ack": "ok", "agent": agent_id, "token": token,
                "expires_in_s": self.stale_after}

    def beat(self, agent_id: str, token: str) -> bool:
        reg = self._agents.get(agent_id)
        if not reg or not secrets.compare_digest(reg["token"], token):
            return False
        reg["last_beat"] = time.time()
        return True

    def alive(self, now: float | None = None) -> list[str]:
        now = now or time.time()
        return [a for a, r in self._agents.items()
                if now - r["last_beat"] <= self.stale_after]

    def count(self) -> int:
        return len(self._agents)
