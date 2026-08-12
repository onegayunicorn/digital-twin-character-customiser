"""Scheduler tick loop: dispatch queued tasks to registered agents."""
from __future__ import annotations

import time

from .agents import BaseAgent


class Scheduler:
    def __init__(self, queue, agents: dict[str, BaseAgent], tick_s: float = 0.05):
        self.queue = queue
        self.agents = agents
        self.tick_s = tick_s
        self.ticks = 0
        self.dispatched = 0

    def tick(self) -> int:
        """Dispatch one queued task (round-robin over ready agents). Returns
        number of tasks dispatched (0 or 1)."""
        self.ticks += 1
        ready = [a for a in self.agents.values() if a.state == "ready"]
        if not ready:
            return 0
        task = self.queue.pop()
        if task is None:
            return 0
        agent = ready[self.ticks % len(ready)]
        agent.transition("busy")
        try:
            result = agent.execute(task)
            self.queue.complete(task["id"], result)
        except Exception as exc:  # noqa: BLE001
            self.queue.fail(task["id"], str(exc))
        finally:
            agent.transition("done")
            agent.transition("ready")
        self.dispatched += 1
        return 1

    def run(self, max_ticks: int = 1000) -> int:
        dispatched = 0
        for _ in range(max_ticks):
            if self.queue.queued_count() == 0:
                break
            if self.tick():
                dispatched += 1
            time.sleep(self.tick_s)
        return dispatched
