"""Governance CLI.

Usage:
  python3 -m governance --agent gatekeeper --text "100% cure guarantee"
  python3 -m governance --agent watcher --spec protocols:131 --tests passed:98
  python3 -m governance --agent chat --message "show tally"
"""
from __future__ import annotations

import argparse
import json
import sys

from .agents import (ChatAgent, GatekeeperAgent, OrchestratorAgent,
                     TallymanAgent, WatcherAgent)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="governance")
    ap.add_argument("--agent", choices=["orchestrator", "gatekeeper", "watcher",
                                        "tallyman", "chat"], default="gatekeeper")
    ap.add_argument("--text", default="")
    ap.add_argument("--message", default="")
    ap.add_argument("--spec", default="protocols:131")
    ap.add_argument("--tests", default="passed:0 failed:0")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    if args.agent == "orchestrator":
        a, task = OrchestratorAgent(), {"tasks": [{"id": "t1", "role": "reasoner"}]}
    elif args.agent == "gatekeeper":
        a, task = GatekeeperAgent(), {"text": args.text, "caller_role": "agent",
                                      "resource": "reports"}
    elif args.agent == "watcher":
        spec = {k: int(v) for kv in args.spec.split() for k, v in [kv.split(":")]}
        tests = {k: int(v) for kv in args.tests.split() for k, v in [kv.split(":")]}
        a, task = WatcherAgent(), {"stale_entities": [], "spec_counts": spec,
                                   "tests": {"passed": tests.get("passed", 0),
                                             "failed": tests.get("failed", 0)}}
    elif args.agent == "tallyman":
        a, task = TallymanAgent(), {"metrics": {"tasks": 4, "tests": 98, "claims": 90}}
    else:
        a, task = ChatAgent(), {"message": args.message}

    a.transition("ready")
    a.transition("busy")
    res = a.execute(task)
    if args.quiet:
        print(f"governance {args.agent} ok: status={res.get('status', res.get('intent'))}")
        return 0
    print(json.dumps(res, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
