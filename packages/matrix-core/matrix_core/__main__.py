"""matrix-core CLI.

Usage:
  python3 -m matrix_core --mode integrate --inventory docs/repo-inventory.csv
  python3 -m matrix_core --mode evolve --nodes 12 --density 0.35
  python3 -m matrix_core --mode harden
"""
from __future__ import annotations

import argparse
import json
import sys


def _integrate(args) -> int:
    from .integration import integrate_inventory
    res = integrate_inventory(args.inventory)
    if args.quiet:
        print(f"matrix integrate ok: {len(res['domains'])} domains, "
              f"density={res['metrics']['density']:.3f}")
        return 0
    print(json.dumps({"domains": res["domains"], "metrics": res["metrics"],
                      "families": res["families"]}, indent=2))
    return 0


def _evolve(args) -> int:
    from .evolution import evolve_matrix
    res = evolve_matrix(args.nodes, target_density=args.density, seed=args.seed)
    if args.quiet:
        print(f"matrix evolve ok: density={res['metrics']['density']:.3f} "
              f"edges={res['metrics']['edges']} fitness={res['fitness']:.4f}")
        return 0
    print(json.dumps({"metrics": res["metrics"], "fitness": res["fitness"],
                      "disclaimer": res["disclaimer"]}, indent=2))
    return 0


def _harden(args) -> int:
    import numpy as np
    from .hardening import stability_report
    a = np.eye(5) + 0.01 * np.ones((5, 5))
    x = np.ones(5)
    b = a @ x
    rep = stability_report(a, x, b)
    if args.quiet:
        print(f"matrix harden ok: cond={rep['condition_number']:.2f} "
              f"grade={rep['stability_grade']}")
        return 0
    print(json.dumps(rep, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="matrix_core")
    ap.add_argument("--mode", choices=["integrate", "evolve", "harden"], default="integrate")
    ap.add_argument("--inventory", default="docs/repo-inventory.csv")
    ap.add_argument("--nodes", type=int, default=12)
    ap.add_argument("--density", type=float, default=0.35)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    if args.mode == "integrate":
        return _integrate(args)
    if args.mode == "evolve":
        return _evolve(args)
    return _harden(args)


if __name__ == "__main__":
    sys.exit(main())
