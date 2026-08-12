import numpy as np
import pytest

from matrix_core.integration import adjacency_from_pairs, graph_metrics, integrate_inventory
from matrix_core.evolution import evolve_matrix, _decode, _encode
from matrix_core.hardening import (condition_estimate, relative_error_bound,
                                   residual_norm, stability_report)


def test_adjacency_from_pairs():
    m = adjacency_from_pairs(["a", "b", "c"], [(0, 1)])
    assert m[0, 1] == 1.0 and m[1, 0] == 1.0
    assert m[0, 2] == 0.0
    assert np.all(np.diag(m) == 0)


def test_graph_metrics_complete_graph():
    n = 5
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    m = adjacency_from_pairs([str(i) for i in range(n)], edges)
    g = graph_metrics(m)
    assert g["density"] == pytest.approx(1.0)
    assert g["edges"] == n * (n - 1) // 2
    assert g["isolated_nodes"] == 0


def test_graph_metrics_empty():
    g = graph_metrics(np.zeros((3, 3)))
    assert g["density"] == 0.0
    assert g["isolated_nodes"] == 3


def test_encode_decode_roundtrip():
    m = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=float)
    x = _encode(m)
    assert _decode(x, 3).shape == (3, 3)
    assert np.array_equal(_decode(x, 3), m)


def test_evolve_reaches_density_target():
    res = evolve_matrix(10, target_density=0.5, generations=80, seed=3)
    assert abs(res["metrics"]["density"] - 0.5) < 0.2
    assert res["metrics"]["nodes"] == 10
    assert "disclaimer" in res


def test_condition_estimate_identity():
    assert condition_estimate(np.eye(4)) == pytest.approx(1.0)


def test_condition_estimate_scaled():
    a = np.diag([1.0, 1e6])
    assert condition_estimate(a) == pytest.approx(1e6)


def test_residual_and_error_bound():
    a = np.eye(3)
    x = np.array([1.0, 2.0, 3.0])
    assert residual_norm(a, x, x) == pytest.approx(0.0)
    assert relative_error_bound(1.0) == pytest.approx(2.22e-16)
    rep = stability_report(a, x, x)
    assert rep["stability_grade"] == "well-conditioned"


def test_integrate_inventory(tmp_path):
    p = tmp_path / "inv.csv"
    # same family token "x" spans quantum + sovereign -> cross-domain edge
    p.write_text("owner,name,url,domain,visibility,language,stars,description\n"
                 "o,x-quantum-1,url,quantum,public,,0,\n"
                 "o,x-sovereign,url,sovereign,public,,0,\n"
                 "o,y-dashboard,url,dashboard-ui,public,,0,\n")
    res = integrate_inventory(str(p))
    assert set(res["domains"]) == {"quantum", "sovereign", "dashboard-ui"}
    assert res["metrics"]["nodes"] == 3
    assert res["metrics"]["density"] > 0  # one cross-domain edge
