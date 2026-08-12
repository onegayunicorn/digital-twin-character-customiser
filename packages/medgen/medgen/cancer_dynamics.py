"""Tumor growth + therapy-response simulation (Gompertz model).

Established mathematical model (Gompertz growth is standard in oncology
modeling). Parameters are illustrative; outputs are SIMULATED and carry no
clinical interpretation.
"""
from __future__ import annotations

import math

import numpy as np


def gompertz_growth(t: np.ndarray, n0: float, alpha: float, beta: float) -> np.ndarray:
    """N(t) = N0 * exp( (alpha/beta) * (1 - exp(-beta*t)) )."""
    return n0 * np.exp((alpha / beta) * (1.0 - np.exp(-beta * t)))


def therapy_response(t: np.ndarray, n0: float, alpha: float, beta: float,
                     kill_rate: float, resistance_rate: float = 0.0,
                     therapy_start: float = 50.0) -> dict:
    """Gompertz growth with therapy: kill reduces N; resistance reduces kill.

    Model:
      dN/dt = alpha*N*ln(C/N) - kill(t)*N
      kill(t) = kill_rate * exp(-resistance_rate*(t-therapy_start)) after start
    Returns time series + metrics (nadir, rebound flag).
    """
    n = np.zeros_like(t, dtype=float)
    n[0] = n0
    for i in range(1, len(t)):
        tt = t[i]
        grow = alpha * n[i - 1] * max(math.log(1e9 / max(n[i - 1], 1e-9)), 0.0)
        kill = kill_rate if tt < therapy_start else kill_rate * math.exp(
            -resistance_rate * (tt - therapy_start))
        n[i] = n[i - 1] + grow * (t[i] - t[i - 1]) - kill * n[i - 1] * (t[i] - t[i - 1])
        n[i] = max(n[i], 0.0)
    
    start_i = int(therapy_start)
    nadir_idx = start_i + int(np.argmin(n[start_i:]))
    rebound = n[-1] > n[nadir_idx] * 1.05 and resistance_rate > 0
    return {
        "t": t,
        "n": n,
        "nadir": float(n[nadir_idx]),
        "nadir_time": float(t[nadir_idx]),
        "end_tumor": float(n[-1]),
        "rebound_detected": bool(rebound),
        "clinical_claim_level": "none",
        "disclaimer": "Simulated mathematical model; not clinical data.",
    }
