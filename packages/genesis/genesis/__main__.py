"""Genesis Engine CLI.

Usage:
  python3 -m genesis --mode ga --fitness sphere --dims 5 --generations 200
  python3 -m genesis --mode spsa --fitness rastrigin --dims 5
"""
from __future__ import annotations

import argparse
import json
import sys

import numpy as np

from .fitness import FITNESS_REGISTRY


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="genesis")
    ap.add_argument("--mode", choices=["ga", "spsa"], default="ga")
    ap.add_argument("--fitness", choices=sorted(FITNESS_REGISTRY), default="sphere")
    ap.add_argument("--dims", type=int, default=5)
    ap.add_argument("--generations", type=int, default=200)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    fn = FITNESS_REGISTRY[args.fitness]
    if args.mode == "ga":
        from .ga import GeneticAlgorithm
        res = GeneticAlgorithm(fn, dims=args.dims, generations=args.generations,
                               seed=args.seed).run()
    else:
        from .spsa import spsa_optimize
        res = spsa_optimize(fn, np.zeros(args.dims), seed=args.seed)

    if args.quiet:
        print(f"genesis {args.mode} ok ({args.fitness}): fitness={res['best_fitness']:.6f}")
        return 0
    print(json.dumps({"mode": args.mode, "fitness": args.fitness,
                      "result": res}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
