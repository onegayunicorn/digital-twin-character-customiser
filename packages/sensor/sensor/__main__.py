"""CLI runner for the IPS sensor model.

Usage:
  python3 -m sensor --mode detect [--quiet]
  python3 -m sensor --mode specs    # print the documented spec summary
"""
from __future__ import annotations

import argparse
import sys


def _detect(quiet: bool) -> int:
    import numpy as np

    from .ips_model import (capacitor_energy, capacitor_response_time,
                            entropy_reclaim_rate, lorentz_force, phase_shift,
                            sensitivity_check, wien_peak_wavelength)

    # Documented spec values (from the IPS nanophotonic spec)
    wavelength = 532e-9          # green laser (m)
    n_change = 1e-9              # refractive index change from a passing ion
    path_length = 0.01           # micro-gap path (m)
    dphi = phase_shift(wavelength, n_change, path_length)

    E = np.array([0.0, 0.0, 1e3])        # V/m
    B = np.array([0.0, 1e-3, 0.0])       # T
    v = np.array([1e3, 0.0, 0.0])        # m/s
    q = 1.602176634e-19                  # electron charge (C)
    F = lorentz_force(q, E, v, B)

    e_waste = 350.0   # W (GPU thermal waste, example)
    e_recovered = 175.0
    eta = entropy_reclaim_rate(e_recovered, e_waste)

    C = 1e-3          # F (graphene supercap, prototype)
    V = 12.0          # V
    R_esr = 4e-6      # ohm (CNT architecture, optimistic prototype value)
    U = capacitor_energy(C, V)
    tau = capacitor_response_time(R_esr, C)
    T_sphere = 14000.0
    lam_peak = wien_peak_wavelength(T_sphere)

    if quiet:
        print(f"detect ok: dphi={dphi:.3e} rad, eta={eta:.1%}, tau={tau:.2e} s")
        return 0

    print("=" * 66)
    print("IPS — Invisible Pressure Sensor (nanophotonic) — model run")
    print("=" * 66)
    print(f"Phase shift (dphi=2pi/lambda*n*L) : {dphi:.4e} rad")
    print(f"Attopascal sensitivity reachable   : {sensitivity_check(1e-18):}")
    print(f"Lorentz force on single electron   : {np.linalg.norm(F):.3e} N")
    print(f"Entropy reclaim rate (eta_S)       : {eta:.1%} (spec band 40-60%)")
    print(f"Capacitor energy U_C=0.5*C*V^2     : {U:.3f} J")
    print(f"Capacitor response tau=R*C         : {tau:.2e} s (target < 5 ns)")
    print(f"Wien peak lambda=b/T @ {T_sphere} K : {lam_peak*1e9:.1f} nm (violet)")
    return 0


def _specs(quiet: bool) -> int:
    spec = [
        ("Sensor Transparency", "> 99.9% (nanophotonic lattice)"),
        ("Detection Threshold", "1e-18 Pa (attopascals)"),
        ("Containment Method", "Dynamic Electrostatic Containment"),
        ("Recovery Efficiency", "~40-60% of thermal waste"),
        ("Capacitor Response", "< 5 ns"),
    ]
    if quiet:
        print(f"specs ok: {len(spec)} rows")
        return 0
    print("IPS Technical Specification Summary")
    for k, v in spec:
        print(f"  {k:<22}: {v}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="sensor", description="IPS sensor models")
    ap.add_argument("--mode", choices=["detect", "specs"], default="detect")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    return _detect(args.quiet) if args.mode == "detect" else _specs(args.quiet)


if __name__ == "__main__":
    sys.exit(main())
