"""Pluggable fitness functions (minimization: lower is better)."""
from __future__ import annotations

import math

import numpy as np


def sphere(x: np.ndarray) -> float:
    """f = sum(x^2); global minimum 0 at x = 0."""
    return float(np.sum(np.square(x)))


def rastrigin(x: np.ndarray) -> float:
    """f = sum(x^2 - 10*cos(2*pi*x) + 10); global minimum 0 at x = 0."""
    return float(np.sum(np.square(x) - 10.0 * np.cos(2.0 * math.pi * x) + 10.0))


def molecule_score_stub(features: np.ndarray) -> float:
    """Placeholder 'molecule desirability' — minimizes distance from a target
    feature vector. Replace with real descriptors for domain work."""
    target = np.array([0.5, -0.25, 1.0, 0.0, 0.75])
    n = min(len(features), len(target))
    return float(np.sum(np.square(features[:n] - target[:n])))


FITNESS_REGISTRY = {
    "sphere": sphere,
    "rastrigin": rastrigin,
    "molecule": molecule_score_stub,
}
