"""Memory manager: working / episodic / semantic stores (JSON backends)."""
from __future__ import annotations

import json
import time


class MemoryManager:
    def __init__(self, path: str | None = None, max_working: int = 50):
        self.path = path
        self.max_working = max_working
        self.working: list[dict] = []
        self.episodic: list[dict] = []
        self.semantic: dict[str, dict] = {}
        if path:
            self._load()

    def write_working(self, entry: dict) -> None:
        self.working.append({**entry, "ts": time.time()})
        self.working = self.working[-self.max_working:]
        self._save()

    def write_episodic(self, episode: dict) -> None:
        self.episodic.append({**episode, "ts": time.time()})
        self._save()

    def write_semantic(self, key: str, value: dict) -> None:
        self.semantic[key] = {**value, "updated": time.time()}
        self._save()

    def read_semantic(self, key: str) -> dict | None:
        v = self.semantic.get(key)
        return dict(v) if v else None

    def recent_working(self, n: int = 10) -> list[dict]:
        return self.working[-n:]

    def episodic_count(self) -> int:
        return len(self.episodic)

    def _save(self) -> None:
        if self.path:
            with open(self.path, "w", encoding="utf-8") as fh:
                json.dump({"working": self.working, "episodic": self.episodic,
                           "semantic": self.semantic}, fh, indent=2)

    def _load(self) -> None:
        try:
            with open(self.path, encoding="utf-8") as fh:
                data = json.load(fh)
            self.working = data.get("working", [])
            self.episodic = data.get("episodic", [])
            self.semantic = data.get("semantic", {})
        except FileNotFoundError:
            pass
