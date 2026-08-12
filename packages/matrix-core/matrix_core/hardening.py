"""Mathematical hardening: numerical stability checks for sim outputs."""
from __future__ import annotations

import numpy as np


def condition_estimate(a: np.ndarray) -> float:
    """Condition number estimate via SVD singular-value ratio (2-norm)."""
    a = np.asarray(a, dtype=float)
    if a.size == 0 or a.shape[0] == 0:
        return 1.0
    s = np.linalg.svd(a, compute_uv=False)
    if s[-1] <= 0:
        return float("inf")
    return float(s[0] / s[-1])


def residual_norm(a: np.ndarray, x: np.ndarray, b: np.ndarray) -> float:
    """||A x - b||_2 — how well x solves A x = b."""
    return float(np.linalg.norm(a @ x - b, ord=2))


def relative_error_bound(cond: float, machine_eps: float = 2.22e-16) -> float:
    """Upper bound on relative error from conditioning: cond * eps."""
    if cond == float("inf"):
        return float("inf")
    return cond * machine_eps


def stability_report(a: np.ndarray, x: np.ndarray | None = None,
                     b: np.ndarray | None = None) -> dict:
    """Full hardening report for a system/simulation output matrix."""
    cond = condition_estimate(a)
    report = {
        "condition_number": cond,
        "stability_grade": _grade(cond),
        "relative_error_bound": relative_error_bound(cond),
    }
    if x is not None and b is not None:
        report["residual_norm"] = residual_norm(a, x, b)
    return report


def _grade(cond: float) -> str:
    if cond == float("inf"):
        return "singular"
    if cond < 1e3:
        return "well-conditioned"
    if cond < 1e6:
        return "moderately conditioned"
    return "ill-conditioned"
