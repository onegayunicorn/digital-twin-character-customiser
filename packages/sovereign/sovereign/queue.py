"""Persistent task queue (FIFO with priority)."""
from __future__ import annotations

import heapq
import itertools
import json
import time


class TaskQueue:
    def __init__(self, path: str | None = None):
        self.path = path
        self._seq = itertools.count()
        self._heap: list[tuple] = []
        self._tasks: dict[str, dict] = {}
        if path:
            self._load()

    def push(self, task: dict, priority: int = 0) -> str:
        tid = task.get("id") or f"task-{next(self._seq)}"
        task = {**task, "id": tid, "priority": priority,
                "status": "queued", "created_at": time.time()}
        self._tasks[tid] = task
        heapq.heappush(self._heap, (priority, task.get("created_at", 0.0), tid))
        self._save()
        return tid

    def pop(self) -> dict | None:
        while self._heap:
            _, _, tid = heapq.heappop(self._heap)
            task = self._tasks.get(tid)
            if task and task["status"] == "queued":
                task["status"] = "running"
                self._save()
                return task
        return None

    def get(self, tid: str) -> dict | None:
        t = self._tasks.get(tid)
        return dict(t) if t else None

    def complete(self, tid: str, result: dict | None = None) -> dict | None:
        t = self._tasks.get(tid)
        if t:
            t["status"] = "done"
            t["result"] = result
            t["finished_at"] = time.time()
            self._save()
        return t

    def fail(self, tid: str, error: str) -> dict | None:
        t = self._tasks.get(tid)
        if t:
            t["status"] = "failed"
            t["error"] = error
            self._save()
        return t

    def queued_count(self) -> int:
        return sum(1 for t in self._tasks.values() if t["status"] == "queued")

    def all(self) -> list[dict]:
        return [dict(t) for t in self._tasks.values()]

    def _load(self) -> None:
        try:
            with open(self.path, encoding="utf-8") as fh:
                data = json.load(fh)
            self._tasks = data.get("tasks", {})
            for t in self._tasks.values():
                if t["status"] == "queued":
                    heapq.heappush(self._heap,
                                   (t["priority"], t.get("created_at", 0.0), t["id"]))
        except FileNotFoundError:
            pass

    def _save(self) -> None:
        if self.path:
            with open(self.path, "w", encoding="utf-8") as fh:
                json.dump({"tasks": self._tasks}, fh, indent=2)
