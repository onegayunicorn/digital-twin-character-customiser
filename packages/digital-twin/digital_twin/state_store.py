"""Versioned twin state store."""
from __future__ import annotations


class TwinStateStore:
    def __init__(self):
        self._state: dict[str, dict] = {}
        self._versions: dict[str, int] = {}

    def set(self, entity: str, field: str, value) -> int:
        """Set a field; returns the new entity version."""
        if entity not in self._state:
            self._state[entity] = {}
            self._versions[entity] = 0
        self._state[entity][field] = value
        self._versions[entity] += 1
        return self._versions[entity]

    def get(self, entity: str, field: str | None = None):
        if entity not in self._state:
            return None
        if field is None:
            return dict(self._state[entity])
        return self._state[entity].get(field)

    def version(self, entity: str) -> int:
        return self._versions.get(entity, 0)

    def snapshot(self) -> dict:
        return {e: dict(s) for e, s in self._state.items()}
