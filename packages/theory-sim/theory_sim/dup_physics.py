"""DUP physics core: pressure field, force laws, orbital models.

Equations implemented (all SI units):
  P  = rho * v^2                    (DUP pressure from particle flux speed)
  Fp = -grad(P)                     (pressure-gradient force)
  Fg = G * m1 * m2 / r^2            (Newtonian gravity, for comparison)
  v_kepler = sqrt(G * M / r)        (Newtonian orbital speed)
  v_dup    = k / r                  (DUP prediction: speed falls as 1/r)

The 1/r prediction is the theory's distinctive, falsifiable claim. For the
solar system the Kepler law v ~ 1/sqrt(r) matches observations to ~1%; the
comparison below quantifies that gap honestly.
"""
from __future__ import annotations

import math

import numpy as np

G = 6.67430e-11  # m^3 kg^-1 s^-2
M_SUN = 1.98847e30  # kg
AU = 1.495978707e11  # m
YEAR = 3.15576e7  # s


def dup_pressure(rho: float, v: float) -> float:
    """DUP pressure: P = rho * v^2 (Pa)."""
    return rho * v * v


def pressure_gradient_force(grad_p: float, volume: float = 1.0) -> float:
    """Force from a pressure gradient: F = -grad(P) * V (N)."""
    return -grad_p * volume


def newton_gravity(m1: float, m2: float, r: float) -> float:
    """Newtonian gravitational force (N)."""
    return G * m1 * m2 / (r * r)


def kepler_orbital_speed(M: float, r: float) -> float:
    """Newton/Kepler circular orbital speed: v = sqrt(GM/r) (m/s)."""
    return math.sqrt(G * M / r)


def dup_orbital_speed(k: float, r: float) -> float:
    """DUP orbital speed: v = k / r (m/s)."""
    return k / r


def fit_dup_constant(r: np.ndarray, v: np.ndarray) -> float:
    """Fit the DUP constant k in v = k/r by least squares (k = mean(v*r))."""
    return float(np.mean(v * r))


def compare_orbital_models(
    radii_au: np.ndarray, v_observed: np.ndarray, M: float = M_SUN
) -> dict:
    """Compare Kepler vs DUP orbital-speed predictions against observed data.

    Returns residuals (observed - predicted) / observed for both models and
    a summary verdict based on RMS relative error.
    """
    r_m = np.asarray(radii_au) * AU
    v_obs_ms = np.asarray(v_observed) * 1e3  # input is km/s -> internal m/s

    v_kepler = np.array([kepler_orbital_speed(M, r) for r in r_m])
    k_dup = fit_dup_constant(r_m, v_obs_ms)
    v_dup = np.array([dup_orbital_speed(k_dup, r) for r in r_m])

    rel_kepler = (v_obs_ms - v_kepler) / v_obs_ms
    rel_dup = (v_obs_ms - v_dup) / v_obs_ms
    rms_kepler = float(np.sqrt(np.mean(rel_kepler ** 2)))
    rms_dup = float(np.sqrt(np.mean(rel_dup ** 2)))

    return {
        "radii_au": np.asarray(radii_au),
        "v_observed_kms": v_obs_ms / 1e3,
        "v_kepler_kms": v_kepler / 1e3,
        "v_dup_kms": v_dup / 1e3,
        "rel_error_kepler": rel_kepler,
        "rel_error_dup": rel_dup,
        "rms_rel_error_kepler": rms_kepler,
        "rms_rel_error_dup": rms_dup,
        "fitted_k_dup": k_dup,
        "verdict": (
            f"Kepler RMS rel. error {rms_kepler:.4%} vs DUP {rms_dup:.4%} — "
            f"{'Kepler matches planetary data; DUP 1/r prediction is falsified for this dataset'
              if rms_kepler < rms_dup else 'DUP matches better'} — "
            "galaxy-scale rotation curves remain the open test (flat v ~ const)."
        ),
    }


# Real mean orbital data for the solar system planets (approx., IAU-ish values).
SOLAR_SYSTEM = {
    "name": np.array(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]),
    "a_au": np.array([0.387, 0.723, 1.000, 1.524, 5.203, 9.537, 19.191, 30.069]),
    "v_kms": np.array([47.36, 35.02, 29.78, 24.07, 13.06, 9.68, 6.80, 5.43]),
}
