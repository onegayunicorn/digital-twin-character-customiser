import math

import numpy as np
import pytest

from sensor.ips_model import (ATTOSCALE, WIEN_B, capacitor_energy,
                              capacitor_response_time, energy_density,
                              entropy_reclaim_rate, inward_potential_force,
                              lorentz_force, phase_shift,
                              planckian_color_fraction, sensitivity_check,
                              wien_peak_wavelength)


def test_phase_shift_scales_with_path():
    p1 = phase_shift(532e-9, 1e-9, 0.01)
    p2 = phase_shift(532e-9, 1e-9, 0.02)
    assert p2 == pytest.approx(2 * p1)


def test_phase_shift_exact_value():
    # dphi = 2*pi/lambda * n * L
    lam, n, L = 532e-9, 1e-9, 0.01
    assert phase_shift(lam, n, L) == pytest.approx(2 * math.pi / lam * n * L)


def test_sensitivity_floor():
    assert sensitivity_check(1e-18)
    assert sensitivity_check(1e-20)
    assert not sensitivity_check(1e-12)


def test_lorentz_force_perpendicular():
    q = 1.602176634e-19
    E = np.array([0.0, 0.0, 0.0])
    v = np.array([1.0, 0.0, 0.0])
    B = np.array([0.0, 0.0, 1.0])
    F = lorentz_force(q, E, v, B)
    assert F[0] == pytest.approx(0.0)
    assert F[1] == pytest.approx(q)  # v x B = (0,1,0)*|v||B|


def test_inward_potential_force():
    F = inward_potential_force(1e-19, np.array([-100.0, 0.0, 0.0]))
    assert F[0] == pytest.approx(1e-17)  # -q * (-100)


def test_entropy_reclaim_rate():
    assert entropy_reclaim_rate(175.0, 350.0) == pytest.approx(0.5)
    assert entropy_reclaim_rate(10.0, 0.0) == 0.0  # no waste -> no claim


def test_energy_density():
    u = energy_density(0.0, 1.0)
    assert u == pytest.approx(0.5 / 1.25663706212e-6)


def test_capacitor_energy_and_response():
    C, V = 1e-3, 12.0
    assert capacitor_energy(C, V) == pytest.approx(0.5 * C * V ** 2)
    R_esr = 4e-6
    tau = capacitor_response_time(R_esr, C)
    assert tau == pytest.approx(4e-9)
    assert tau < 5e-9  # spec: < 5 ns


def test_wien_law():
    T = 14000.0
    lam = wien_peak_wavelength(T)
    assert lam == pytest.approx(WIEN_B / T)
    # violet visible range ~400-450 nm corresponds to T ~ 6400-7200 K
    lam_violet = wien_peak_wavelength(6800.0)
    assert 400e-9 < lam_violet < 450e-9


def test_planckian_color_fraction():
    assert planckian_color_fraction(8000.0) == pytest.approx(0.0)
    assert planckian_color_fraction(20000.0) == pytest.approx(1.0)
    assert 0.0 <= planckian_color_fraction(14000.0) <= 1.0
