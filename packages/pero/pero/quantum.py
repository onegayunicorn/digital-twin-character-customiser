"""Quantum-optics verification models: what REAL entanglement requires.

Standard results used:
  CHSH Bell parameter: S = E(a,b) - E(a,b') + E(a',b) + E(a',b')
    - classical bound:  S <= 2
    - quantum max:      S <= 2*sqrt(2) ~ 2.828
  SPDC: pair production rate ~ 1 in 1e6..1e11 pump photons (probability p_spdc);
  coincidence counting validates pairs arriving within a ns-level window.
"""
from __future__ import annotations

import math


def bell_s_parameter(e_ab: float, e_abp: float, e_apb: float, e_apbp: float) -> float:
    """CHSH S parameter from four expectation values (each in [-1, 1])."""
    return e_ab - e_abp + e_apb + e_apbp


def classify_quantum_evidence(s: float) -> dict:
    """Classify an S value against Bell limits."""
    if s > 2.0 + 1e-9:
        kind = "quantum-evidence" if s <= 2.0 * math.sqrt(2) + 1e-9 else "superluminal/nonphysical"
        return {"S": s, "classical_limit": 2.0, "quantum_max": 2.0 * math.sqrt(2),
                "verdict": kind}
    return {"S": s, "classical_limit": 2.0, "quantum_max": 2.0 * math.sqrt(2),
            "verdict": "classical (no Bell violation)"}


def spdc_pair_rate(pump_photons: float, p_spdc: float = 1e-9) -> float:
    """Expected entangled pairs from a pump photon count given SPDC probability."""
    return pump_photons * p_spdc


def spdc_coincidence_rate(pair_rate: float, detection_efficiency: float = 0.3,
                          window_ns: float = 5.0, dark_count_hz: float = 100.0) -> dict:
    """Model coincidence counting: true coincidences + accidental background.

    Accidental rate ~ (dark+signal rates product) * window — simplified model.
    """
    true_rate = pair_rate * detection_efficiency ** 2
    accidental = (dark_count_hz ** 2) * (window_ns * 1e-9)
    total = true_rate + accidental
    return {
        "true_coincidence_hz": true_rate,
        "accidental_hz": accidental,
        "total_coincidence_hz": total,
        "signal_to_accidental": true_rate / accidental if accidental > 0 else float("inf"),
    }
