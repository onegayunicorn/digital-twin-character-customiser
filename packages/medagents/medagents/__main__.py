"""Healthcare agency CLI.

Usage:
  python3 -m medagents --agent hospital --task triage --vitals '{"hr": 115, "spo2": 92}'
  python3 -m medagents --agent doctor --exon 44 --cdna c.7912C>T --protein p.Arg2638*
  python3 -m medagents --agent researcher --query "exon skipping DMD"
"""
from __future__ import annotations

import argparse
import json
import sys

from .agents import DoctorAgent, HospitalAgent, ResearcherAgent


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="medagents")
    ap.add_argument("--agent", choices=["hospital", "doctor", "researcher"],
                    default="hospital")
    ap.add_argument("--task", default="triage")
    ap.add_argument("--vitals", type=json.loads, default=None)
    ap.add_argument("--exon", type=int, default=44)
    ap.add_argument("--cdna", default="c.7912C>T")
    ap.add_argument("--protein", default="p.Arg2638*")
    ap.add_argument("--query", default="")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    if args.agent == "hospital":
        a = HospitalAgent()
        task = {"vitals": args.vitals or {"hr": 80, "spo2": 98}}
    elif args.agent == "doctor":
        a = DoctorAgent()
        task = {"exon": args.exon, "cdna": args.cdna, "protein": args.protein}
    else:
        a = ResearcherAgent()
        task = {"query": args.query}
    a.transition("ready")
    a.transition("busy")
    res = a.execute(task)
    if args.quiet:
        key = "band" if args.agent == "hospital" else "matches"
        print(f"medagents {args.agent} ok: "
              f"{res.get(key, list(res)[:2])}")
        return 0
    print(json.dumps(res, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
