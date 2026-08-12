"""Linear interpolation for smooth twin-state transitions."""
from __future__ import annotations


def interpolate(a: float, b: float, t: float) -> float:
    """Linear interpolation: a + (b - a) * t, t in [0, 1]."""
    t = max(0.0, min(1.0, t))
    return a + (b - a) * t


def interpolate_vec(a: list, b: list, t: float) -> list:
    t = max(0.0, min(1.0, t))
    return [ai + (bi - ai) * t for ai, bi in zip(a, b)]
