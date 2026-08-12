"""Matrix integration: build adjacency matrices and graph metrics."""
from __future__ import annotations

import csv

import numpy as np


def adjacency_from_pairs(nodes: list[str], edges: list[tuple[int, int]]) -> np.ndarray:
    """Symmetric adjacency matrix for a node list with (i, j) edges."""
    n = len(nodes)
    m = np.zeros((n, n), dtype=float)
    for i, j in edges:
        if 0 <= i < n and 0 <= j < n and i != j:
            m[i, j] = 1.0
            m[j, i] = 1.0
    return m


def graph_metrics(m: np.ndarray) -> dict:
    """Density, degree centrality, and connectivity stats for an adjacency
    matrix. Input is treated as a simple undirected graph."""
    n = len(m)
    if n == 0:
        return {"density": 0.0, "mean_degree": 0.0, "max_degree": 0,
                "isolated_nodes": 0, "edges": 0}
    edges = int(np.count_nonzero(np.triu(m, 1)))
    density = 2.0 * edges / (n * (n - 1)) if n > 1 else 0.0
    degrees = np.count_nonzero(m, axis=1)
    return {
        "nodes": n,
        "edges": edges,
        "density": float(density),
        "mean_degree": float(np.mean(degrees)),
        "max_degree": int(np.max(degrees)),
        "isolated_nodes": int(np.sum(degrees == 0)),
    }


def integrate_inventory(csv_path: str, same_domain_only: bool = True) -> dict:
    """Build a repo-domain adjacency matrix from the repo-inventory CSV.

    Nodes: distinct domains. Edge between two domains if at least one pair of
    repos in those domains share the same first token family (name prefix
    heuristic) — a coarse integration signal for matrix routing.
    """
    rows = []
    with open(csv_path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            rows.append(r)
    domains = sorted({r["domain"] for r in rows})
    index = {d: i for i, d in enumerate(domains)}
    m = np.zeros((len(domains), len(domains)), dtype=float)
    # token families: first token of repo name (lowercased, alnum)
    families: dict[str, set] = {}
    for r in rows:
        fam = "".join(c for c in r["name"].lower().split("-")[0]
                      if c.isalnum() or c == "_") or r["name"].lower()
        families.setdefault(fam, set()).add(r["domain"])
    for fam, doms in families.items():
        doms = list(doms)
        for i in range(len(doms)):
            for j in range(i + 1, len(doms)):
                a, b = index[doms[i]], index[doms[j]]
                m[a, b] += 1.0
                m[b, a] += 1.0
    return {"domains": domains, "matrix": m,
            "metrics": graph_metrics(m), "families": len(families)}
