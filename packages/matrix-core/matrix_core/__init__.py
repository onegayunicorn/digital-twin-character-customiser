"""matrix-core — integration, evolution, and hardening.

  integration - build adjacency matrices from repo inventories / dependency
                declarations; graph metrics (density, degree centrality)
  evolution   - GA over adjacency matrices (via the genesis engine) toward
                target density/centrality objectives
  hardening   - numerical stability: condition estimate, residual norms,
                relative error bounds for simulation outputs

HONESTY: evolution optimizes *structure metrics*, not physics; hardened
outputs report their own numerical limits.
"""
from .integration import (adjacency_from_pairs, graph_metrics, integrate_inventory)
from .evolution import evolve_matrix
from .hardening import (condition_estimate, residual_norm, relative_error_bound,
                        stability_report)

__all__ = ["adjacency_from_pairs", "graph_metrics", "integrate_inventory",
           "evolve_matrix", "condition_estimate", "residual_norm",
           "relative_error_bound", "stability_report"]
