"""IPS (Invisible Pressure Sensor) nanophotonic detection models.

Implements the documented IPS equations (SI units where applicable):
  Phase shift:        dphi = (2*pi/lambda) * n * L        (laser interferometry)
  Sensitivity:        down to 1e-18 Pa (attopascals)
  Lorentz force:      F = q*(E + v x B)                   (DEC collection)
  Entropy reclaim:    eta_S = E_recovered / E_waste       (40-60% band)
  Capacitor:          U_C = 0.5*C*V^2,  tau = R_ESR*C     (<5 ns target)
  Wien color:         lambda_peak = b / T                 (dashboard viz)

All models are parameterized so lab data can be plugged in directly.
"""
from __future__ import annotations

import math

import numpy as np

ATTOSCALE = 1e-18  # Pa
C_EMPTY = 8.8541878128e-12  # F/m
MU_EMPTY = 1.25663706212e-6  # H/m
WIEN_B = 2.897771955e-3  # m*K
BOLTZMANN = 1.380649e-23  # J/K


# --- 1. Nanophotonic detection -------------------------------------------
def phase_shift(wavelength: float, refractive_index_change: float,
                path_length: float) -> float:
    """Interferometric phase shift: dphi = 2*pi/lambda * n * L (rad)."""
    return 2.0 * math.pi / wavelength * refractive_index_change * path_length


def sensitivity_check(pressure: float) -> bool:
    """True if the pressure is at or below the attopascal floor (1e-18 Pa)."""
    return pressure <= ATTOSCALE


# --- 2. Dynamic Electrostatic Containment (DEC) --------------------------
def lorentz_force(q: float, E: np.ndarray, v: np.ndarray, B: np.ndarray) -> np.ndarray:
    """F = q*(E + v x B) (vector)."""
    return q * (E + np.cross(v, B))


def inward_potential_force(q: float, grad_V: np.ndarray) -> np.ndarray:
    """F = -q*grad(V) — the potential-well pull toward sphere centre."""
    return -q * grad_V


# --- 3. Entropy-waste recovery -------------------------------------------
def entropy_reclaim_rate(e_recovered: float, e_waste: float) -> float:
    """eta_S = E_recovered / E_waste (0..1). Guard against div-by-zero."""
    if e_waste <= 0:
        return 0.0
    return e_recovered / e_waste


def energy_density(e_field: float, b_field: float) -> float:
    """u = 0.5*eps0*E^2 + 0.5*B^2/mu0 (J/m^3)."""
    return 0.5 * C_EMPTY * e_field ** 2 + 0.5 * b_field ** 2 / MU_EMPTY


# --- 4. Emergency capacitor ----------------------------------------------
def capacitor_energy(capacitance: float, voltage: float) -> float:
    """U_C = 0.5*C*V^2 (J)."""
    return 0.5 * capacitance * voltage * voltage


def capacitor_response_time(esr: float, capacitance: float) -> float:
    """tau = R_ESR * C (s). Target < 5 ns."""
    return esr * capacitance


def emergency_dump_time_ok(esr: float, capacitance: float,
                           target_s: float = 5e-9) -> bool:
    return capacitor_response_time(esr, capacitance) <= target_s


# --- 5. Visualization physics --------------------------------------------
def wien_peak_wavelength(temperature: float) -> float:
    """lambda_peak = b / T (m)."""
    return WIEN_B / temperature


def planckian_color_fraction(temperature: float,
                             t_blue: float = 8000.0, t_violet: float = 20000.0) -> float:
    """0=empty(blue) -> 1=saturated(violet) based on effective T."""
    return float(np.clip((temperature - t_blue) / (t_violet - t_blue), 0.0, 1.0))


def gibbs_free_energy_estimate(u_volume: float, volume: float,
                               temperature: float) -> float:
    """Rough available-work estimate G ~ U - T*S with S from ideal-gas-like
    counting: S = k_B * N * ln(V/N) is not needed here — we return U - T*kB*N
    for N density given, else U (documented as an estimate)."""
    return u_volume * volume  # placeholder: stored field energy
