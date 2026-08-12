"""sonar-5d CLI.

Usage:
  python3 -m sonar_5d --mode lattice --cells 2 [--export mesh.obj] [--quiet]
  python3 -m sonar_5d --mode sweep --cells 2 [--quiet]
"""
from __future__ import annotations

import argparse
import sys


def _lattice(args) -> int:
    from .mesh import diamond_cubic_lattice, lattice_metrics, export_obj
    metrics = lattice_metrics(args.cells)
    if args.export:
        atoms, bonds = diamond_cubic_lattice(args.cells)
        export_obj(atoms, bonds, args.export)
    if args.quiet:
        print(f"sonar lattice ok: atoms={metrics['n_atoms']} bonds={metrics['n_bonds']}")
        return 0
    print("=" * 56)
    print("Diamond-cubic crystal mesh")
    print("=" * 56)
    for k, v in metrics.items():
        print(f"  {k:<16}: {v}")
    if args.export:
        print(f"  exported      : {args.export}")
    return 0


def _sweep(args) -> int:
    import numpy as np
    from .mesh import diamond_cubic_lattice
    from .sweep import sweep_plane
    atoms, _ = diamond_cubic_lattice(args.cells)
    res = sweep_plane(atoms, plane_z=0.5, t=0.25, freq=args.freq)
    if args.quiet:
        print(f"sonar sweep ok: atoms_in_plane={res['atoms_in_plane']} "
              f"max_intensity={res['max_intensity']:.4f}")
        return 0
    print("=" * 56)
    print("5D sonar sweep (x, y, z, time, intensity)")
    print("=" * 56)
    for k, v in res.items():
        print(f"  {k:<16}: {v}")
    print("  Model: I = A exp(-r^2/2sigma^2) sin(2*pi*f*t - 2*pi*r)")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="sonar_5d")
    ap.add_argument("--mode", choices=["lattice", "sweep"], default="lattice")
    ap.add_argument("--cells", type=int, default=2)
    ap.add_argument("--freq", type=float, default=1.0)
    ap.add_argument("--export", type=str, default=None)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    return _lattice(args) if args.mode == "lattice" else _sweep(args)


if __name__ == "__main__":
    sys.exit(main())
