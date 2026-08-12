"""5D sonar sweep: (x, y, z, time, intensity) echo field over a crystal mesh."""
from __future__ import annotations

import math

import numpy as np


def sonar_field(origin: np.ndarray, targets: np.ndarray, t: float,
                amplitude: float = 1.0, sigma: float = 1.0,
                freq: float = 1.0) -> np.ndarray:
    """Echo intensity per target point:
    I = A * exp(-r^2 / sigma^2) * sin(2*pi*f*t - 2*pi*r/lambda), lambda = 1."""
    r = np.linalg.norm(targets - origin, axis=1)
    env = amplitude * np.exp(-r ** 2 / (2.0 * sigma ** 2))
    wave = np.sin(2.0 * math.pi * freq * t - 2.0 * math.pi * r)
    return env * wave


def sweep_plane(atoms: np.ndarray, plane_z: float, t: float,
                freq: float = 1.0, sigma: float = 1.5) -> dict:
    """Sweep the echo field for lattice atoms near a plane (x-y slice)."""
    origin = np.array([0.5, 0.5, plane_z], dtype=float)
    close = atoms[np.abs(atoms[:, 2] - plane_z) < 0.6]
    if len(close) == 0:
        return {"atoms_in_plane": 0, "max_intensity": 0.0, "mean_intensity": 0.0}
    i = sonar_field(origin, close, t, freq=freq, sigma=sigma)
    return {"atoms_in_plane": len(close),
            "max_intensity": float(np.max(np.abs(i))),
            "mean_intensity": float(np.mean(np.abs(i)))}


def peak_response(times: np.ndarray, origin: np.ndarray, target: np.ndarray,
                  freq: float = 1.0) -> float:
    """Max |intensity| over a time series for a single target — the sonar
    return peak used for range/latency readouts."""
    peaks = [abs(sonar_field(origin, target[None, :], t, freq=freq)[0]) for t in times]
    return float(max(peaks))
