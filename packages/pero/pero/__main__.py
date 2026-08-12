"""PERO analysis CLI.

Usage:
  python3 -m pero --mode classical [--quiet]
  python3 -m pero --mode quantum [--quiet]
"""
from __future__ import annotations

import argparse
import sys

import numpy as np


def _classical(quiet: bool) -> int:
    from .classical import (fft_dominant_frequency, spatial_coherence,
                            spectral_decomposition, splitting_efficiency,
                            tilt_coherence_prediction)
    incident, left, right = 100.0, 28.0, 24.14  # -> ~52.14% splitting
    eff = splitting_efficiency(incident, left, right)
    # synthetic lobe profiles correlated at ~65%
    rng = np.random.default_rng(7)
    base = rng.uniform(0.2, 1.0, 64)
    left_i = base.copy()
    right_i = 0.65 * base + 0.35 * rng.uniform(0.0, 1.0, 64)
    coh = spatial_coherence(left_i, right_i)
    wl = np.linspace(380, 780, 200)
    inten = np.exp(-((wl - 450.0) / 30.0) ** 2) + 0.02
    spec = spectral_decomposition(wl, inten)
    t = np.linspace(0, 5, 500)
    sig = np.sin(2 * np.pi * 1.8 * t) + 0.1 * np.sin(2 * np.pi * 9.4 * t)
    fdom = fft_dominant_frequency(sig, t[1] - t[0])
    pred = tilt_coherence_prediction(coh, 15.0)
    if quiet:
        print(f"pero classical ok: eff={eff:.2%} coh={coh:.2%} peak={spec['peak_nm']:.0f}nm "
              f"f_dom={fdom:.2f}Hz pred15={pred:.2%}")
        return 0
    print("=" * 60)
    print("PERO — classical photonic analysis (450nm laser + amethyst model)")
    print("=" * 60)
    print(f"  Splitting efficiency      : {eff:.2%}")
    print(f"  Spatial coherence (Pearson): {coh:.2%}")
    print(f"  Spectral peak / purity    : {spec['peak_nm']:.0f} nm / {spec['purity_in_window']:.1%}")
    print(f"  Dominant oscillation      : {fdom:.2f} Hz")
    print(f"  Coherence @15deg+pol lock : {pred:.2%} (prediction, HYPOTHESIS)")
    return 0


def _quantum(quiet: bool) -> int:
    from .quantum import (bell_s_parameter, classify_quantum_evidence,
                          spdc_coincidence_rate, spdc_pair_rate)
    s_classical = bell_s_parameter(0.6, -0.6, 0.6, 0.6)
    s_quantum = bell_s_parameter(0.71, -0.71, 0.71, 0.71)  # max ~2.828
    c1 = classify_quantum_evidence(s_classical)
    c2 = classify_quantum_evidence(s_quantum)
    pairs = spdc_pair_rate(1e12, p_spdc=1e-9)
    coin = spdc_coincidence_rate(pairs)
    if quiet:
        print(f"pero quantum ok: S_class={s_classical:.2f} S_q={s_quantum:.2f} "
              f"pairs={pairs:.1f} coin={coin['total_coincidence_hz']:.4f}Hz")
        return 0
    print("=" * 60)
    print("PERO — quantum verification models (what real entanglement needs)")
    print("=" * 60)
    print(f"  CHSH S (classical data)  : {s_classical:.3f} -> {c1['verdict']}")
    print(f"  CHSH S (entangled model) : {s_quantum:.3f} -> {c2['verdict']} "
          f"(max {c2['quantum_max']:.3f})")
    print(f"  SPDC pairs (1e12 pump)   : {pairs:.1f} (p_spdc=1e-9)")
    print(f"  Coincidence rate         : {coin['total_coincidence_hz']:.4f} Hz "
          f"(S/N {coin['signal_to_accidental']:.1f}x)")
    return 0


def _engine(quiet: bool) -> int:
    from .engine import entanglement_evolution, pure_bell_rho
    res = entanglement_evolution(pure_bell_rho(), dephase_steps=50, p_step=0.02)
    if quiet:
        print(f"pero engine ok: F_end={res['final_fidelity']:.4f} "
              f"C_end={res['final_concurrence']:.4f}")
        return 0
    print("=" * 60)
    print("PERO — photonic entanglement engine (dephasing model)")
    print("=" * 60)
    print(f"  Initial fidelity (Bell |phi+>) : 1.0000")
    print(f"  Fidelity after dephasing       : {res['final_fidelity']:.4f}")
    print(f"  Concurrence after dephasing    : {res['final_concurrence']:.4f}")
    print(f"  {res['disclaimer']}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="pero", description="Photonic analysis toolkit")
    ap.add_argument("--mode", choices=["classical", "quantum", "engine"], default="classical")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    if args.mode == "engine":
        return _engine(args.quiet)
    return _classical(args.quiet) if args.mode == "classical" else _quantum(args.quiet)


if __name__ == "__main__":
    sys.exit(main())
