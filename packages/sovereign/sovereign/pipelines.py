"""Declarative pipelines: ordered steps referencing queue tasks."""
from __future__ import annotations

import json
import time


class PipelineRunner:
    def __init__(self, queue, agents, audit=None):
        self.queue = queue
        self.agents = agents
        self.audit = audit

    def run_pipeline(self, pipeline: dict) -> dict:
        """pipeline: {id, steps: [{id, task, priority, depends_on}]}
        Executes steps in dependency order by enqueuing tasks and dispatching
        through the scheduler tick. Returns step outcomes."""
        steps = pipeline.get("steps", [])
        outcomes = {}
        for step in steps:
            deps = step.get("depends_on", [])
            if any(d not in outcomes or outcomes[d].get("status") != "done"
                   for d in deps):
                outcomes[step["id"]] = {"status": "skipped",
                                        "reason": "dependency not satisfied"}
                continue
            tid = self.queue.push(step.get("task", {}),
                                  priority=step.get("priority", 0))
            dispatched = 0
            for _ in range(50):
                if self.queue.get(tid)["status"] != "queued":
                    break
                if self._dispatch_one():
                    dispatched += 1
            outcome = self.queue.get(tid)
            outcomes[step["id"]] = {"status": outcome["status"],
                                    "result": outcome.get("result"),
                                    "dispatched": dispatched}
            if self.audit:
                self.audit.log({"event": "pipeline_step", "pipeline": pipeline.get("id"),
                                "step": step["id"], "status": outcome["status"]})
        return {"pipeline": pipeline.get("id"), "steps": outcomes,
                "status": "complete"}

    def _dispatch_one(self) -> bool:
        from .scheduler import Scheduler  # local import avoids cycle
        sched = Scheduler(self.queue, self.agents, tick_s=0.0)
        return sched.tick()
