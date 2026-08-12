"""In-process realtime hub with late-join snapshots (WS-hub analogue)."""
from __future__ import annotations

import threading


class RealtimeHub:
    def __init__(self):
        self._subs: dict[str, list] = {}
        self._snapshots: dict[str, dict] = {}
        self._lock = threading.Lock()
        self.update_count = 0

    def subscribe(self, channel: str, callback) -> bool:
        with self._lock:
            self._subs.setdefault(channel, []).append(callback)
        return True

    def unsubscribe(self, channel: str, callback) -> bool:
        with self._lock:
            try:
                self._subs[channel].remove(callback)
                return True
            except ValueError:
                return False

    def publish(self, channel: str, state: dict) -> int:
        with self._lock:
            self._snapshots[channel] = dict(state)
            callbacks = list(self._subs.get(channel, []))
        self.update_count += 1
        for cb in callbacks:
            cb(channel, state)
        return len(callbacks)

    def snapshot(self, channel: str) -> dict | None:
        snap = self._snapshots.get(channel)
        return dict(snap) if snap else None

    def subscriber_count(self, channel: str) -> int:
        return len(self._subs.get(channel, []))
