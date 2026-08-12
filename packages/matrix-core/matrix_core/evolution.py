"""Matrix evolution: GA over adjacency matrices toward structural targets."""
from __future__ import annotations

import numpy as np


def _encode(m: np.ndarray) -> np.ndarray:
    """Upper-triangle (i<j) entries of a symmetric matrix -> flat vector."""
    n = len(m)
    return np.array([m[i, j] for i in range(n) for j in range(i + 1, n)])


def _decode(x: np.ndarray, n: int) -> np.ndarray:
    m = np.zeros((n, n), dtype=float)
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            m[i, j] = m[j, i] = 1.0 if x[k] > 0.5 else 0.0
            k += 1
    return m


def evolve_matrix(n_nodes: int, target_density: float = 0.35,
                  target_centrality_skew: float = 0.3, generations: int = 60,
                  seed: int = 7) -> dict:
    """GA-evolve an adjacency matrix toward (density, degree-skew) targets.

    Fitness (minimized): |density - target_density| * w1
                          + |skew - target_skew| * w2
    where skew = std(degrees) / mean(degrees). Returns best matrix + metrics.
    """
    from genesis.ga import GeneticAlgorithm

    def fitness(x: np.ndarray) -> float:
        m = _decode(x, n_nodes)
        from .integration import graph_metrics
        g = graph_metrics(m)
        mean_deg = g["mean_degree"]
        deg_skew = 0.0 if mean_deg == 0 else (
            np.std(np.count_nonzero(m, axis=1)) / mean_deg)
        w1, w2 = 1.0, 0.5
        return (abs(g["density"] - target_density) * w1
                + abs(deg_skew - target_centrality_skew) * w2)

    n_edges = n_nodes * (n_nodes - 1) // 2
    ga = GeneticAlgorithm(fitness, dims=n_edges, pop_size=60,
                          generations=generations, bounds=(0.0, 1.0), seed=seed)
    res = ga.run()
    best = _decode(np.array(res["best"]), n_nodes)
    from .integration import graph_metrics
    return {"matrix": best, "metrics": graph_metrics(best),
            "fitness": res["best_fitness"],
            "disclaimer": "Structural optimization only; no physical meaning."}
