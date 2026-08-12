"""Invisible Pressure resonance model.

Fundamental law of the theory's resonance branch:
    P(x, t) = A0 * exp(i * (2*pi*f*t + phi(x)))

Default carrier: f = 7.83 Hz (Schumann fundamental); harmonics and the
documented auxiliary frequencies (1.17, 13.66, 136.1, 14.1 Hz) are provided
as named modes. The model also computes the spectral decomposition of a
superposition of modes, enabling quantitative predictions (beat frequencies,
energy distribution) that laboratory setups can test.
"""
from __future__ import annotations

import math

import numpy as np

SCHUMANN_FUNDAMENTAL = 7.83  # Hz
MODES = {
    "schumann_fundamental": 7.83,
    "schumann_first_harmonic": 14.1,
    "lunar_sideband": 13.66,
    "baseline_carrier": 1.17,
    "healing_pulse": 136.1,
}


def pressure_wave(t: np.ndarray, f: float = SCHUMANN_FUNDAMENTAL,
                  A0: float = 1.0, phi: float = 0.0) -> np.ndarray:
    """Real part of P(x,t) = A0 * exp(i(2*pi*f*t + phi)) at x = const."""
    return A0 * np.cos(2.0 * math.pi * f * t + phi)


def superposition(t: np.ndarray, amplitudes: dict[str, float]) -> np.ndarray:
    """Sum of named modes with per-mode amplitudes (real part)."""
    total = np.zeros_like(t, dtype=float)
    for name, amp in amplitudes.items():
        if name not in MODES:
            raise KeyError(f"unknown mode {name!r}; available: {sorted(MODES)}")
        total += amp * pressure_wave(t, MODES[name])
    return total


def beat_frequency(f1: float, f2: float) -> float:
    """|f1 - f2| — the low-frequency envelope of two close modes."""
    return abs(f1 - f2)


def spectral_power(signal: np.ndarray, dt: float) -> tuple[np.ndarray, np.ndarray]:
    """Power spectral density via FFT. Returns (freqs, power)."""
    n = len(signal)
    win = np.hanning(n)
    fft = np.fft.rfft(signal * win)
    power = np.abs(fft) ** 2 / (n * np.sum(win ** 2))
    freqs = np.fft.rfftfreq(n, d=dt)
    return freqs, power


def dominant_frequency(signal: np.ndarray, dt: float) -> float:
    """Frequency (Hz) of the strongest spectral bin."""
    freqs, power = spectral_power(signal, dt)
    return float(freqs[np.argmax(power)])
