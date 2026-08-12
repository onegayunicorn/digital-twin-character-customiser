import numpy as np
import pytest

from theory_sim.resonance import (MODES, SCHUMANN_FUNDAMENTAL, beat_frequency,
                                  dominant_frequency, pressure_wave,
                                  spectral_power, superposition)


def test_pressure_wave_period():
    dt = 1e-3
    t = np.arange(0, 1.0, dt)
    sig = pressure_wave(t, f=SCHUMANN_FUNDAMENTAL)
    assert sig[0] == pytest.approx(1.0)
    # one full period later (1/7.83 s) the wave returns near its start
    n_period = int(round(1.0 / SCHUMANN_FUNDAMENTAL / dt))
    assert sig[n_period] == pytest.approx(1.0, abs=1e-2)


def test_dominant_frequency_recovers_carrier():
    dt = 1e-4
    t = np.arange(0, 10.0, dt)  # 10 s window -> 0.1 Hz FFT resolution
    sig = pressure_wave(t, 7.83)
    f = dominant_frequency(sig, dt)
    assert f == pytest.approx(7.83, abs=0.2)


def test_superposition_spectral_power_top_bin():
    dt = 1e-4
    t = np.arange(0, 10.0, dt)
    mix = superposition(t, {"schumann_fundamental": 1.0, "lunar_sideband": 0.5})
    f, p = spectral_power(mix, dt)
    top = sorted(zip(f, p), key=lambda x: -x[1])[:4]
    top_freqs = [round(float(freq), 2) for freq, _ in top]
    assert any(abs(freq - 7.83) <= 0.3 for freq in top_freqs)
    assert any(abs(freq - 13.66) <= 0.3 for freq in top_freqs)


def test_beat_frequency():
    assert beat_frequency(7.83, 14.1) == pytest.approx(6.27)
    assert beat_frequency(7.83, 13.66) == pytest.approx(5.83)


def test_unknown_mode_raises():
    with pytest.raises(KeyError):
        superposition(np.zeros(10), {"not_a_mode": 1.0})


def test_named_modes_present():
    for name in ("schumann_fundamental", "baseline_carrier", "healing_pulse"):
        assert name in MODES
