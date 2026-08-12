"""CLI runner for the theory simulation package.

Usage:
  python3 -m theory_sim --mode dup [--bodies N] [--quiet]
  python3 -m theory_sim --mode resonance [--freq HZ] [--seconds S] [--quiet]
  python3 -m theory_sim --mode galaxy [--quiet]
"""
from __future__ import annotations

import argparse
import sys


def _run_galaxy(quiet: bool) -> int:
    from .galaxy_rotation import NGC3198, compare_rotation_models

    res = compare_rotation_models(NGC3198["r_kpc"], NGC3198["v_kms"])
    if quiet:
        print(f"galaxy ok: bary={res['rms_baryonic']:.1%} cdm={res['rms_cdm']:.1%} "
              f"dup={res['rms_dup_pressure']:.1%}")
        return 0
    print("=" * 72)
    print("Galaxy rotation curves: baryonic vs Lambda-CDM vs pressure-gradient (DUP)")
    print(f"Reference: {NGC3198['cite']}")
    print("=" * 72)
    print(f"{'r (kpc)':>8}{'v_obs':>10}{'v_bary':>10}{'v_cdm':>10}{'v_dup':>10}")
    for i, r in enumerate(res["r_kpc"]):
        print(f"{r:>8.1f}{res['v_obs_kms'][i]:>10.1f}{res['v_bary_kms'][i]:>10.1f}"
              f"{res['v_cdm_kms'][i]:>10.1f}{res['v_dup_kms'][i]:>10.1f}")
    print("-" * 72)
    print(f"RMS rel. error baryonic-only : {res['rms_baryonic']:.2%}")
    print(f"RMS rel. error Lambda-CDM    : {res['rms_cdm']:.2%}")
    print(f"RMS rel. error DUP pressure  : {res['rms_dup_pressure']:.2%}")
    print(f"Fitted (CDM)  : log10 Md={res['fit_cdm']['log10_Md']:.2f} "
          f"v200={res['fit_cdm']['v200']:.0f} c={res['fit_cdm']['c']:.1f}")
    print(f"Fitted (DUP)  : log10 Md={res['fit_dup']['log10_Md']:.2f} "
          f"v_flat={res['fit_dup']['v_flat']:.1f} km/s "
          f"r_core={res['fit_dup']['r_core_kpc']:.1f} kpc")
    print(f"Verdict       : {res['verdict']}")
    return 0


def _run_dup(quiet: bool) -> int:
    from .dup_physics import SOLAR_SYSTEM, compare_orbital_models

    res = compare_orbital_models(SOLAR_SYSTEM["a_au"], SOLAR_SYSTEM["v_kms"])
    if quiet:
        print(res["verdict"])
        return 0
    print("=" * 72)
    print("DUP vs Newton orbital-speed comparison (solar system planets)")
    print("=" * 72)
    print(f"{'Planet':<10}{'a (AU)':>8}{'v_obs':>10}{'v_kepler':>10}{'v_dup':>10}{'rel err (K/D)':>16}")
    for i, name in enumerate(SOLAR_SYSTEM["name"]):
        print(f"{name:<10}{res['radii_au'][i]:>8.3f}{res['v_observed_kms'][i]:>10.2f}"
              f"{res['v_kepler_kms'][i]:>10.2f}{res['v_dup_kms'][i]:>10.2f}"
              f"{res['rel_error_kepler'][i]:>8.2%}/{res['rel_error_dup'][i]:>7.2%}")
    print("-" * 72)
    print(f"Kepler RMS relative error : {res['rms_rel_error_kepler']:.4%}")
    print(f"DUP (v=k/r) RMS rel. err : {res['rms_rel_error_dup']:.4%}")
    print(f"Fitted DUP constant k     : {res['fitted_k_dup']:.3e} m^2/s")
    print(f"Verdict                   : {res['verdict']}")
    return 0


def _run_resonance(freq: float, seconds: float, quiet: bool) -> int:
    import numpy as np

    from .resonance import (MODES, dominant_frequency, pressure_wave,
                            spectral_power, superposition)

    dt = 1.0 / (freq * 64)  # 64 samples per cycle
    t = np.arange(0.0, seconds, dt)
    sig = pressure_wave(t, freq)
    if not quiet:
        print(f"Resonance carrier: {freq} Hz over {seconds}s ({len(t)} samples)")
        print(f"  peak amplitude : {float(np.max(np.abs(sig))):.4f}")
        print(f"  dominant freq  : {dominant_frequency(sig, dt):.4f} Hz (expect {freq})")
        mix = superposition(t, {"schumann_fundamental": 1.0, "lunar_sideband": 0.5})
        f, p = spectral_power(mix, dt)
        top = sorted(zip(f, p), key=lambda x: -x[1])[:3]
        print(f"  superposition top-3 bins : "
              + ", ".join(f"{freq_:.2f} Hz (p={pow_:.3f})" for freq_, pow_ in top))
        print(f"  beat (7.83 vs 13.66 Hz)   : {abs(MODES['schumann_fundamental'] - MODES['lunar_sideband']):.3f} Hz")
    else:
        print(f"resonance ok: dominant={dominant_frequency(sig, dt):.3f} Hz")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="theory_sim", description="DUP / invisible-pressure simulations")
    ap.add_argument("--mode", choices=["dup", "resonance", "galaxy"], default="dup")
    ap.add_argument("--freq", type=float, default=7.83, help="carrier frequency (Hz)")
    ap.add_argument("--seconds", type=float, default=2.0, help="simulation window (s)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    if args.mode == "dup":
        return _run_dup(args.quiet)
    if args.mode == "galaxy":
        return _run_galaxy(args.quiet)
    return _run_resonance(args.freq, args.seconds, args.quiet)


if __name__ == "__main__":
    sys.exit(main())
