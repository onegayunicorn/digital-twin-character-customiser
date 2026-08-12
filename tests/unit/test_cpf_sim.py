import math

import numpy as np
import pytest

from cpf_sim.engine import CPFEngine, KB, nucleation_probability


def test_nucleation_probability_analytic():
    dg = 5e-21
    assert nucleation_probability(dg, 600.0) == pytest.approx(
        math.exp(-dg / (KB * 600.0)))
    # higher barrier -> lower probability
    assert nucleation_probability(1e-20, 600.0) < nucleation_probability(5e-21, 600.0)
    # higher temperature -> higher probability
    assert nucleation_probability(dg, 900.0) > nucleation_probability(dg, 300.0)
    assert nucleation_probability(dg, 0.0) == 0.0


def test_thermal_field_gradient():
    e = CPFEngine(size=16)
    assert e.thermal[0, 0] > e.thermal[-1, 0]  # sun side hotter
    assert e.thermal[0, 0] == pytest.approx(e.t_sun)
    assert e.thermal[-1, 0] == pytest.approx(e.t_void)


def test_engine_runs_to_stabilization():
    e = CPFEngine(size=32, seed=1)
    final = e.run(max_steps=300)
    assert final["n_crystals"] > 0
    assert final["crystal_mass"] > 0
    assert final["stabilized"] is True  # mass fraction reached
    assert final["step"] <= 300


def test_engine_deterministic():
    e1 = CPFEngine(size=16, seed=5)
    e2 = CPFEngine(size=16, seed=5)
    f1 = e1.run(max_steps=50)
    f2 = e2.run(max_steps=50)
    assert f1["crystal_mass"] == f2["crystal_mass"]
    assert f1["n_crystals"] == f2["n_crystals"]


def test_growth_increases_mass():
    e = CPFEngine(size=16, seed=3)
    m0 = e.metrics()["crystal_mass"]
    e.step()
    m1 = e.metrics()["crystal_mass"]
    assert m1 >= m0
