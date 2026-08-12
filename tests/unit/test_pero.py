import math

import numpy as np
import pytest

from pero.classical import (fft_dominant_frequency, spatial_coherence,
                            spectral_decomposition, splitting_efficiency,
                            tilt_coherence_prediction)
from pero.quantum import (bell_s_parameter, classify_quantum_evidence,
                          spdc_coincidence_rate, spdc_pair_rate)


def test_splitting_efficiency():
    assert splitting_efficiency(100.0, 28.0, 24.14) == pytest.approx(0.5214, rel=1e-2)
    assert splitting_efficiency(0.0, 5.0, 5.0) == 0.0


def test_spatial_coherence_perfect_and_anti():
    a = np.array([1.0, 2.0, 3.0, 4.0])
    assert spatial_coherence(a, a) == pytest.approx(1.0)
    assert spatial_coherence(a, -a) == pytest.approx(-1.0)


def test_spatial_coherence_archive_level():
    rng = np.random.default_rng(7)
    base = rng.uniform(0.2, 1.0, 64)
    right = 0.65 * base + 0.35 * rng.uniform(0.0, 1.0, 64)
    coh = spatial_coherence(base, right)
    assert 0.4 < coh < 0.95  # correlated but not perfect


def test_spectral_decomposition():
    wl = np.linspace(380, 780, 200)
    inten = np.exp(-((wl - 450.0) / 30.0) ** 2)
    spec = spectral_decomposition(wl, inten)
    assert spec["peak_nm"] == pytest.approx(450.0)
    # Gaussian peak: a +-1-sigma window captures erf(1) ~= 84.3% of power
    assert spec["purity_in_window"] == pytest.approx(0.845, abs=0.02)


def test_fft_dominant_frequency():
    t = np.linspace(0, 10, 5000)
    sig = np.sin(2 * np.pi * 1.8 * t)
    f = fft_dominant_frequency(sig, t[1] - t[0])
    assert f == pytest.approx(1.8, abs=0.15)


def test_tilt_coherence_prediction():
    # baseline 0.65 -> 15deg aligned -> ~0.91 (source prediction)
    pred = tilt_coherence_prediction(0.6466, 15.0)
    assert pred == pytest.approx(0.9113, abs=0.02)
    assert 0.0 <= pred <= 1.0
    assert tilt_coherence_prediction(0.6466, 0.0) == pytest.approx(0.6466)


def test_bell_parameter_limits():
    # S = e_ab - e_abp + e_apb + e_apbp; 2.0 sits exactly on the classical limit
    s_class = bell_s_parameter(0.5, -0.5, 0.5, 0.5)
    s_ent = bell_s_parameter(0.7, -0.7, 0.7, 0.7)  # S = 2.8 -> quantum evidence
    assert classify_quantum_evidence(s_class)["verdict"] == "classical (no Bell violation)"
    assert classify_quantum_evidence(s_ent)["verdict"] == "quantum-evidence"
    assert classify_quantum_evidence(s_ent)["quantum_max"] == pytest.approx(2.0 * math.sqrt(2))
    # exceeding the Tsirelson bound -> nonphysical
    assert classify_quantum_evidence(3.2)["verdict"] == "superluminal/nonphysical"


def test_spdc_models():
    pairs = spdc_pair_rate(1e12, p_spdc=1e-9)
    assert pairs == pytest.approx(1e3)
    coin = spdc_coincidence_rate(pairs, detection_efficiency=0.3)
    assert coin["true_coincidence_hz"] == pytest.approx(90.0)
    assert coin["signal_to_accidental"] > 1.0
