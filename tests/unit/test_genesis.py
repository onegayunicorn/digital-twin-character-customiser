import math

import numpy as np
import pytest

from genesis.fitness import FITNESS_REGISTRY, molecule_score_stub, rastrigin, sphere
from genesis.ga import GeneticAlgorithm
from genesis.spsa import spsa_optimize


def test_sphere_analytic_optimum():
    assert sphere(np.zeros(5)) == pytest.approx(0.0)
    assert sphere(np.array([1.0, 2.0])) == pytest.approx(5.0)


def test_rastrigin_optimum():
    assert rastrigin(np.zeros(3)) == pytest.approx(0.0)
    # far from optimum, rastrigin is positive
    assert rastrigin(np.array([3.0, 3.0])) > 10.0


def test_ga_converges_on_sphere():
    ga = GeneticAlgorithm(sphere, dims=5, pop_size=80, generations=300, seed=7)
    res = ga.run()
    assert res["best_fitness"] < 0.05  # near-optimal on the smooth sphere
    assert len(res["history"]) == 300
    assert "disclaimer" in res


def test_ga_deterministic_with_seed():
    a = GeneticAlgorithm(sphere, dims=3, generations=50, seed=11).run()
    b = GeneticAlgorithm(sphere, dims=3, generations=50, seed=11).run()
    assert a["best_fitness"] == b["best_fitness"]
    assert a["best"] == b["best"]


def test_ga_improves_over_generations():
    ga = GeneticAlgorithm(sphere, dims=5, pop_size=60, generations=150, seed=3)
    res = ga.run()
    assert res["history"][0] >= res["best_fitness"]  # never worse at the end
    assert res["best_fitness"] < res["history"][0]


def test_spsa_reduces_sphere_fitness():
    res = spsa_optimize(sphere, np.array([2.0, 2.0, 2.0]), max_iter=200, seed=5)
    assert res["best_fitness"] < 3.0 * 4.0  # below starting fitness 12
    assert res["best_fitness"] > 0.0
    assert "disclaimer" in res


def test_fitness_registry():
    assert set(FITNESS_REGISTRY) == {"sphere", "rastrigin", "molecule"}
    assert molecule_score_stub(np.array([0.5, -0.25, 1.0, 0.0, 0.75])) == pytest.approx(0.0)
