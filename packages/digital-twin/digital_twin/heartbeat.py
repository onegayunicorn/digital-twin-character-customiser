"""Heartbeat staleness detection with exponential-backoff reconnect signal."""
from __future__ import annotations

import random


class HeartbeatMonitor:
    def __init__(self, stale_after_s: float = 5.0, base_delay_s: float = 1.0):
        self.stale_after = stale_after_s
        self.base_delay = base_delay_s
        self._last_seen: dict[str, float] = {}

    def beat(self, entity: str, now: float) -> None:
        self._last_seen[entity] = now

    def is_stale(self, entity: str, now: float) -> bool:
        last = self._last_seen.get(entity)
        if last is None:
            return True
        return now - last > self.stale_after

    def stale_entities(self, now: float) -> list[str]:
        return [e for e in self._last_seen if self.is_stale(e, now)]

    def next_reconnect_delay(self, attempt: int, jitter: float = 0.1) -> float:
        """Exponential backoff with jitter: base * 2^attempt * (1 ± jitter)."""
        raw = self.base_delay * (2 ** attempt)
        j = 1.0 + jitter * (random.random() * 2 - 1)
        return raw * j
