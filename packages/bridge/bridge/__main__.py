"""Bridge CLI.

Usage:
  python3 -m bridge --register medgen dmd_repair  (wires a demo endpoint)
  python3 -m bridge --list
  python3 -m bridge --call dmd_repair --exon 44 --cdna c.7912C>T --protein p.Arg2638*
"""
from __future__ import annotations

import argparse
import sys

from .registry import BridgeRegistry


def _demo_dmd_repair(exon=44, cdna="c.7912C>T", protein="p.Arg2638*", **kw):
    from medgen.repair_sim import repair_strategies
    return repair_strategies(exon, cdna, protein)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="bridge")
    ap.add_argument("--register", nargs=2, metavar=("MODULE", "CAPABILITY"))
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--call", type=str)
    ap.add_argument("--exon", type=int, default=44)
    ap.add_argument("--cdna", default="c.7912C>T")
    ap.add_argument("--protein", default="p.Arg2638*")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    registry = BridgeRegistry()
    registry.register("medgen", "dmd_repair", _demo_dmd_repair)

    if args.register:
        registry.register(args.register[0], args.register[1], _demo_dmd_repair)
        print(f"registered: {args.register[0]} -> {args.register[1]}")
        return 0
    if args.list:
        print("capabilities:", registry.capabilities())
        print("health:", registry.health())
        return 0
    if args.call:
        res = registry.call(args.call, exon=args.exon, cdna=args.cdna,
                            protein=args.protein)
        if args.quiet:
            print(f"bridge call ok: {args.call} -> "
                  f"{[s['mechanism'] for s in res['strategies']]}")
        else:
            import json
            print(json.dumps(res, indent=2))
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
