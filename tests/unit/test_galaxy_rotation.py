import math

import numpy as np
import pytest

from theory_sim.galaxy_rotation import (KPC_M, MSUN_KG, NGC3198,
                                        compare_rotation_models,
                                        exponential_disk_v, isothermal_pressure_v,
                                        nfw_halo_v, point_mass_v,
                                        total_v_squared)


def test_point_mass_matches_kepler():
    v = point_mass_v(1e11, 10.0)  # 1e11 Msun at 10 kpc
    expected = math.sqrt(6.67430e-11 * 1e11 * MSUN_KG / (10.0 * KPC_M)) / 1e3
    assert v == pytest.approx(expected)


def test_exponential_disk_declines_at_large_r():
    r = np.linspace(1.0, 40.0, 100)
    v = exponential_disk_v(4e10, 3.5, r)
    # an exponential disk curve peaks then declines
    peak_i = int(np.argmax(v))
    assert v[peak_i] > v[-1]
    assert v[-1] < v[peak_i] * 0.5


def test_nfw_halo_rises_and_flattens():
    r = np.logspace(0.5, 2.5, 50)
    v = nfw_halo_v(130.0, 120.0, 10.0, r)
    assert np.all(v > 0)
    # NFW curve rises then declines slowly at large r (v ~ sqrt(GM/r))
    assert v[-1] < v[-5]


def test_isothermal_pressure_flat():
    r = np.linspace(2.0, 30.0, 20)
    v = isothermal_pressure_v(150.0, r)
    assert np.allclose(v, 150.0, rtol=0.03)


def test_total_v_quadrature():
    a = np.array([3.0, 4.0])
    b = np.array([4.0, 0.0])
    assert np.allclose(total_v_squared([a, b]), np.array([5.0, 4.0]))


def test_compare_models_honest_verdict():
    res = compare_rotation_models(NGC3198["r_kpc"], NGC3198["v_kms"])
    # baryonic-only should be clearly worse than the fitted models
    assert res["rms_baryonic"] > res["rms_cdm"]
    assert res["rms_baryonic"] > res["rms_dup_pressure"]
    assert res["rms_baryonic"] > 0.2  # baryonic-only fails flat curves (~50%)
    # both fitted models reproduce the flat curve within ~10%
    assert res["rms_cdm"] < 0.10
    assert res["rms_dup_pressure"] < 0.10
    assert "verdict" in res and "dark matter" in res["verdict"].lower()
