"""CPF simulation CLI.

Usage:
  python3 -m cpf_sim [--size N] [--steps N] [--seed N] [--quiet]
"""
from __future__ import annotations

import argparse
import sys

from .engine import CPFEngine


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Crystal Planet Formation simulation")
    ap.add_argument("--size", type=int, default=64)
    ap.add_argument("--steps", type=int, default=200)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    engine = CPFEngine(size=args.size, seed=args.seed)
    final = engine.run(max_steps=args.steps)

    if args.quiet:
        print(f"cpf ok: crystals={final['n_crystals']} mass={final['crystal_mass']:.1f} "
              f"stabilized={final['stabilized']}")
        return 0

    print("=" * 60)
    print("Crystal Planet Formation — simulation result")
    print("=" * 60)
    print(f"  Steps executed     : {final['step']}")
    print(f"  Crystals formed    : {final['n_crystals']}")
    print(f"  Crystal mass       : {final['crystal_mass']:.1f}")
    print(f"  Mass fraction      : {final['mass_fraction']:.2%}")
    print(f"  Proto-planet flag  : {final['stabilized']}")
    print("  Physics: P_nucleate = exp(-dG*/(kB*T)); growth ~ local density")
    print("  Status: SIMULATED (classical nucleation theory); teleological")
    print("          framing from source document not reproduced (claims register K3).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
