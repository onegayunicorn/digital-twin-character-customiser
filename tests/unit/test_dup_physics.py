import math

import numpy as np
import pytest

from theory_sim.dup_physics import (AU, G, M_SUN, SOLAR_SYSTEM,
                                    compare_orbital_models, dup_orbital_speed,
                                    dup_pressure, kepler_orbital_speed,
                                    newton_gravity, pressure_gradient_force)


def test_dup_pressure_basic():
    assert dup_pressure(1.0, 2.0) == pytest.approx(4.0)  # P = rho v^2
    assert dup_pressure(1.225, 0.0) == 0.0


def test_pressure_gradient_force_sign():
    # A negative gradient (pressure decreasing outward) pushes inward: F > 0
    assert pressure_gradient_force(-10.0, volume=1.0) == pytest.approx(10.0)
    assert pressure_gradient_force(5.0, volume=2.0) == pytest.approx(-10.0)


def test_newton_gravity_inverse_square():
    f = newton_gravity(1.0, 1.0, 1.0)
    assert f == pytest.approx(G)
    f4 = newton_gravity(1.0, 1.0, 2.0)
    assert f4 == pytest.approx(G / 4.0)


def test_kepler_earth_speed():
    # Earth: v = sqrt(G*M_sun / 1 AU) ~ 29.78 km/s
    v = kepler_orbital_speed(M_SUN, AU)
    assert v / 1e3 == pytest.approx(29.78, rel=1e-3)


def test_dup_speed_1_over_r():
    k = 1.0
    assert dup_orbital_speed(k, 1.0) == pytest.approx(1.0)
    assert dup_orbital_speed(k, 2.0) == pytest.approx(0.5)


def test_compare_orbital_models_runs_and_reports():
    res = compare_orbital_models(SOLAR_SYSTEM["a_au"], SOLAR_SYSTEM["v_kms"])
    assert len(res["v_kepler_kms"]) == 8
    assert res["rms_rel_error_kepler"] < 0.05   # Kepler ~1% on planets
    assert res["rms_rel_error_dup"] > 0.1       # DUP 1/r clearly worse here
    assert "verdict" in res


def test_fit_dup_constant_perfect_line():
    r = np.array([1.0, 2.0, 4.0]) * AU
    v = 1.0 / r
    from theory_sim.dup_physics import fit_dup_constant
    k = fit_dup_constant(r, v)
    assert k == pytest.approx(1.0)
