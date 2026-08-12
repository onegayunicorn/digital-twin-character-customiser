"""SPSA (simultaneous perturbation stochastic approximation) optimizer."""
from __future__ import annotations

import numpy as np


def spsa_optimize(fitness_fn, x0: np.ndarray, max_iter: int = 100,
                  a: float = 0.5, c: float = 0.1, seed: int = 1) -> dict:
    """Minimize fitness_fn via SPSA.

    theta_{k+1} = theta_k - a_k * g_k
    g_k approx = (f(x + c*Delta) - f(x - c*Delta)) / (2c) * Delta  (per-coordinate)
    with a_k = a / (k+1)^0.602, c_k = c / (k+1)^0.101.
    """
    rng = np.random.default_rng(seed)
    x = np.array(x0, dtype=float)
    history = [float(fitness_fn(x))]
    for k in range(max_iter):
        a_k = a / (k + 1) ** 0.602
        c_k = c / (k + 1) ** 0.101
        delta = rng.choice([-1.0, 1.0], size=x.shape)
        f_plus = fitness_fn(x + c_k * delta)
        f_minus = fitness_fn(x - c_k * delta)
        g = (f_plus - f_minus) / (2.0 * c_k) * delta
        x = x - a_k * g
        history.append(float(fitness_fn(x)))
    return {"best": x.tolist(), "best_fitness": float(fitness_fn(x)),
            "history": history,
            "disclaimer": "Numerical surrogate; not quantum hardware."}
