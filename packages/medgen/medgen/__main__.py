"""medgen CLI.

Usage:
  python3 -m medgen --mode dmd           # DMD nonsense table + classification
  python3 -m medgen --mode repair --exon 44 --cdna c.7912C>T --protein p.Arg2638*
  python3 -m medgen --mode tumor [--kill 0.05] [--resistance 0.01]
"""
from __future__ import annotations

import argparse
import sys

import numpy as np


def _dmd(quiet: bool) -> int:
    from .dmd_mutations import NONSENSE_TABLE, all_classified
    rows = all_classified()
    if quiet:
        print(f"medgen dmd ok: {len(rows)} mutations, "
              f"{sum(1 for r in rows if r['exon_skipping_eligible'])} skipping-eligible")
        return 0
    print("=" * 64)
    print("DMD nonsense mutations — classification (SIMULATED reference data)")
    print("=" * 64)
    print(f"{'Exon':<6}{'cDNA':<18}{'Protein':<14}{'Stop':<6}{'Skip-elig'}")
    for r in rows:
        print(f"{r['exon']:<6}{r['cdna_change']:<18}{r['protein_change']:<14}"
              f"{str(r['stop_codon']):<6}{r['exon_skipping_eligible']}")
    print("Source: UMD-TREAT-NMD 2025 / ClinVar / PPMD (as cited). SIMULATED data,")
    print("clinical_claim_level=none.")
    return 0


def _repair(args) -> int:
    from .repair_sim import repair_strategies
    import json
    res = repair_strategies(args.exon, args.cdna, args.protein)
    if args.quiet:
        print(f"medgen repair ok: exon {args.exon} -> "
              f"{[s['mechanism'] for s in res['strategies']]}")
    else:
        print(json.dumps(res, indent=2))
    return 0


def _tumor(args, quiet: bool) -> int:
    from .cancer_dynamics import therapy_response
    t = np.linspace(0, 150, 300)
    res = therapy_response(t, n0=1e6, alpha=0.3, beta=0.02,
                           kill_rate=args.kill, resistance_rate=args.resistance)
    if quiet:
        print(f"medgen tumor ok: nadir={res['nadir']:.1f} cells @ t={res['nadir_time']:.0f} "
              f"rebound={res['rebound_detected']}")
        return 0
    print("=" * 64)
    print("Tumor dynamics — Gompertz + therapy response (SIMULATED model)")
    print("=" * 64)
    print(f"  Nadir cells : {res['nadir']:.2e} @ t={res['nadir_time']:.0f}")
    print(f"  End tumor   : {res['end_tumor']:.2e}")
    print(f"  Rebound     : {res['rebound_detected']}")
    print(f"  {res['disclaimer']}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="medgen")
    ap.add_argument("--mode", choices=["dmd", "repair", "tumor"], default="dmd")
    ap.add_argument("--exon", type=int, default=44)
    ap.add_argument("--cdna", default="c.7912C>T")
    ap.add_argument("--protein", default="p.Arg2638*")
    ap.add_argument("--kill", type=float, default=0.05)
    ap.add_argument("--resistance", type=float, default=0.01)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    if args.mode == "dmd":
        return _dmd(args.quiet)
    if args.mode == "repair":
        return _repair(args)
    return _tumor(args, args.quiet)


if __name__ == "__main__":
    sys.exit(main())
