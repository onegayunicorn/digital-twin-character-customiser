"""Sovereign orchestrator CLI.

Usage:
  python3 -m sovereign --serve [--port N]        # HTTP API
  python3 -m sovereign --run task.json [--path DATA_DIR]  # one-shot run
  python3 -m sovereign --handshake agent1 reasoner   # test handshake
"""
from __future__ import annotations

import argparse
import json
import sys

from .agents import AgentFactory
from .api import OrchestratorAPI, serve
from .governance import AuditLogger
from .handshake import HandshakeRegistry
from .memory import MemoryManager
from .queue import TaskQueue
from .scheduler import Scheduler


def _build(queue, memory, audit, handshake, roles: tuple = ("reasoner", "coder", "tool", "coordinator")):
    agents = {r: AgentFactory.create(r, r) for r in roles}
    for a in agents.values():
        a.transition("ready")
    return agents


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="sovereign")
    ap.add_argument("--serve", action="store_true")
    ap.add_argument("--port", type=int, default=8787)
    ap.add_argument("--run", type=str, help="path to task JSON (one-shot)")
    ap.add_argument("--handshake", nargs=2, metavar=("ID", "ROLE"))
    ap.add_argument("--path", type=str, default=None, help="data dir for persistence")
    args = ap.parse_args(argv)

    if args.handshake:
        reg = HandshakeRegistry()
        ack = reg.hello(*args.handshake)
        print(json.dumps(ack, indent=2))
        return 0

    queue = TaskQueue(f"{args.path}/queue.json" if args.path else None)
    memory = MemoryManager(f"{args.path}/memory.json" if args.path else None)
    audit = AuditLogger(f"{args.path}/audit.jsonl" if args.path else None)
    handshake = HandshakeRegistry()
    agents = _build(queue, memory, audit, handshake)
    api = OrchestratorAPI(queue=queue, agents=agents, memory=memory,
                          audit=audit, handshake=handshake)

    if args.serve:
        serve(api, port=args.port)
        return 0

    if args.run:
        with open(args.run, encoding="utf-8") as fh:
            task = json.load(fh)
        tid = queue.push(task)
        scheduler = Scheduler(queue, agents)
        dispatched = scheduler.run(max_ticks=50)
        done = queue.get(tid)
        audit.log({"event": "task_completed", "task": tid, "dispatched": dispatched})
        print(json.dumps({"dispatched": dispatched, "task": done}, indent=2))
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
