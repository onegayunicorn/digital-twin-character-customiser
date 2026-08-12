"""Typed pub/sub event bus."""
from __future__ import annotations

import threading
from collections import defaultdict


class EventBus:
    def __init__(self):
        self._subs: dict[str, list] = defaultdict(list)
        self._lock = threading.Lock()

    def subscribe(self, topic: str, callback):
        with self._lock:
            self._subs[topic].append(callback)
        return callback

    def unsubscribe(self, topic: str, callback) -> bool:
        with self._lock:
            try:
                self._subs[topic].remove(callback)
                return True
            except ValueError:
                return False

    def publish(self, topic: str, event: dict) -> int:
        with self._lock:
            callbacks = list(self._subs.get(topic, []))
        for cb in callbacks:
            cb(event)
        return len(callbacks)

    def subscriber_count(self, topic: str) -> int:
        return len(self._subs.get(topic, []))
