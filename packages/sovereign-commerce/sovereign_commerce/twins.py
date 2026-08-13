"""Digital twins for platform entities: payments, orders, escrows, nodes.

Wires the digital-twin package (event bus + state store + realtime hub) to
commerce entities so every entity has a twin that replays its state events.
"""
from __future__ import annotations

import time

from digital_twin import EventBus, RealtimeHub, TwinStateStore


class CommerceTwinHub:
    def __init__(self):
        self.bus = EventBus()
        self.store = TwinStateStore()
        self.hub = RealtimeHub()

    def create_twin(self, entity_type: str, entity_id: str, initial: dict) -> str:
        twin_id = f"{entity_type}:{entity_id}"
        for field, value in initial.items():
            self.store.set(twin_id, field, value)
        event = {"twin": twin_id, "op": "created", "state": initial, "ts": time.time()}
        self.bus.publish("twin.created", event)
        return twin_id

    def update_twin(self, entity_type: str, entity_id: str, field: str,
                    value) -> int:
        twin_id = f"{entity_type}:{entity_id}"
        version = self.store.set(twin_id, field, value)
        self.bus.publish("twin.updated", {"twin": twin_id, "field": field,
                                          "value": value, "version": version})
        self.hub.publish(twin_id, self.store.get(twin_id))
        return version

    def twin_state(self, entity_type: str, entity_id: str) -> dict | None:
        return self.store.get(f"{entity_type}:{entity_id}")

    def snapshot(self, twin_id: str) -> dict | None:
        return self.hub.snapshot(twin_id)

    def subscribe(self, twin_id: str, callback) -> bool:
        return self.hub.subscribe(twin_id, callback)
