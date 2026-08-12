"""Classical photonic analysis: the metrics the amethyst archive actually measured."""
from __future__ import annotations

import math

import numpy as np


def splitting_efficiency(incident_power: float, lobe_left: float,
                         lobe_right: float) -> float:
    """Fraction of incident power redistributed into the two refracted lobes."""
    if incident_power <= 0:
        return 0.0
    return (lobe_left + lobe_right) / incident_power


def spatial_coherence(intensity_a: np.ndarray, intensity_b: np.ndarray) -> float:
    """Pearson correlation between left/right lobe intensity profiles."""
    a = np.asarray(intensity_a, dtype=float)
    b = np.asarray(intensity_b, dtype=float)
    if a.size < 2 or b.size < 2:
        return 0.0
    ca, cb = a - a.mean(), b - b.mean()
    denom = math.sqrt(np.sum(ca ** 2) * np.sum(cb ** 2))
    if denom == 0:
        return 0.0
    return float(np.clip(np.sum(ca * cb) / denom, -1.0, 1.0))


def spectral_decomposition(wavelengths_nm: np.ndarray, intensities: np.ndarray,
                           peak_nm: float = 450.0, width_nm: float = 30.0) -> dict:
    """Gaussian peak model fit around the dominant wavelength.

    Returns peak prominence (relative to max) and fraction of power within
    peak_nm +/- width_nm (the 'spectral purity' proxy).
    """
    w = np.asarray(wavelengths_nm, dtype=float)
    i = np.asarray(intensities, dtype=float)
    model = np.exp(-((w - peak_nm) / width_nm) ** 2)
    window = (np.abs(w - peak_nm) <= width_nm)
    total = float(i.sum()) if i.sum() > 0 else 1.0
    purity = float(i[window].sum()) / total if total else 0.0
    return {"peak_nm": float(peak_nm), "prominence": float(i.max()),
            "purity_in_window": purity, "model_amplitude": float(model.max())}


def fft_dominant_frequency(signal: np.ndarray, dt: float) -> float:
    """Dominant frequency (Hz) of a temporal oscillation via FFT."""
    s = np.asarray(signal, dtype=float) - np.mean(signal)
    n = len(s)
    if n < 4:
        return 0.0
    win = np.hanning(n)
    fft = np.abs(np.fft.rfft(s * win)) ** 2
    freqs = np.fft.rfftfreq(n, d=dt)
    return float(freqs[np.argmax(fft)])


def tilt_coherence_prediction(baseline_coherence: float, tilt_deg: float,
                              polarization_aligned: bool = True) -> float:
    """Phenomenological coherence model: tilting + polarization locking raises
    the spatial coherence proxy toward ~91 % per the source's prediction.

    Returns clipped [0, 1]. Model: linear ramp to the target over 15 degrees
    (gain = (target - baseline) * min(1, tilt/15)).
    """
    target = 0.91 if polarization_aligned else 0.78
    ramp = max(0.0, min(1.0, tilt_deg / 15.0))
    pred = baseline_coherence + (target - baseline_coherence) * ramp
    return float(max(0.0, min(1.0, pred)))
