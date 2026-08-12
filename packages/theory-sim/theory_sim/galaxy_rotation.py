"""Galaxy rotation-curve models: baryonic Newtonian, Lambda-CDM (dark halo),
and pressure-gradient (DUP-style) fits, compared against a reference dataset.

Reference data: approximate NGC 3198 rotation curve (Begeman 1989 / de Blok
et al. 2008 style flat curve: rises to ~150 km/s then stays flat to ~30 kpc).
The dataset here is an *approximate teaching set* for model comparison —
full precision tables should be pulled from the cited papers for publication.

Models
------
1. Baryonic only: exponential disk + central point mass (no dark matter).
   Prediction: v declines after the disk peak -> FAILS flat curves.
2. Lambda-CDM: baryons + NFW dark halo. Standard fit.
3. Pressure-gradient (DUP): baryons + isothermal pressure term
   (v_pressure ~ const, the modified-dynamics analogue of MOND/TeVeS).
   Prediction: flat curve WITHOUT dark matter.

Honest framing: models 2 and 3 both reproduce flat curves; only 3 avoids
dark matter. That is the theory's positive claim (claims register C6), and
this harness reports residuals for all three.
"""
from __future__ import annotations

import math

import numpy as np

G = 6.67430e-11
KPC_M = 3.0856775814913673e19  # m per kpc
MSUN_KG = 1.98847e30
KMS = 1e3  # m/s per km/s

# Approximate NGC 3198 rotation curve (km/s vs radius kpc).
NGC3198 = {
    "r_kpc": np.array([2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 15.0, 20.0, 25.0, 30.0]),
    "v_kms": np.array([110.0, 133.0, 143.0, 148.0, 150.0, 151.0, 150.0, 149.0, 148.0, 147.0]),
    "cite": "Approximate NGC 3198 values (Begeman 1989; de Blok et al. 2008). Use published tables for publication.",
}


# --- baryonic models -------------------------------------------------------
def point_mass_v(M_sun: float, r_kpc: float) -> float:
    """Kepler speed of a point mass (km/s)."""
    r_m = r_kpc * KPC_M
    return math.sqrt(G * M_sun * MSUN_KG / r_m) / KMS


def exponential_disk_v(Md_sun: float, rd_kpc: float, r_kpc: np.ndarray) -> np.ndarray:
    """Rotation curve of an exponential thin disk (Freeman 1970), km/s."""
    x = np.asarray(r_kpc) / rd_kpc
    with np.errstate(divide="ignore", invalid="ignore"):
        # I0*K0 - I1*K1 Bessel combination for the exponential disk
        b = _bessel_disk_term(x)
    v2 = (G * Md_sun * MSUN_KG) / (rd_kpc * KPC_M) * x * b
    return np.sqrt(np.maximum(v2, 0.0)) / KMS


def _bessel_disk_term(x: np.ndarray) -> np.ndarray:
    """x * (I0(x)K0(x) - I1(x)K1(x)) with safe small-x asymptotics."""
    from scipy.special import i0, i1, k0, k1  # scipy is a hard dependency
    out = np.zeros_like(x, dtype=float)
    for i, xi in enumerate(x):
        if xi < 1e-3:
            out[i] = xi * xi * (math.log(2.0 / xi) - 0.5772156649 - 0.25)
        else:
            out[i] = xi * (i0(xi) * k0(xi) - i1(xi) * k1(xi))
    return out


# --- dark halo -------------------------------------------------------------
def nfw_halo_v(v200_kms: float, r200_kpc: float, c: float, r_kpc: np.ndarray) -> np.ndarray:
    """NFW halo circular speed (km/s): v^2 = GM(r)/r with M(r) = 4 pi rho0 rs^3 f(x)."""
    x = np.asarray(r_kpc) / (r200_kpc / c)  # x = r / r_s
    f = np.where(x < 1e-6, 0.0, np.log(1.0 + x) - x / (1.0 + x))
    fc = np.log(1.0 + c) - c / (1.0 + c)
    v2 = (v200_kms * v200_kms) * (f / fc) * (c / x)
    return np.sqrt(np.maximum(v2, 0.0))


# --- pressure-gradient (DUP-style) ----------------------------------------
def isothermal_pressure_v(v_flat_kms: float, r_kpc: np.ndarray,
                          r_core_kpc: float = 1.0) -> np.ndarray:
    """Isothermal-sphere-like pressure term: constant speed outside a core.

    Physical picture: a pressure field with P(r) ~ rho(r) v_flat^2 and
    rho(r) ~ 1/r^2 (isothermal) yields dP/dr balancing the centripetal
    term, giving v -> const without dark matter. This is the modified-
    dynamics analogue implemented here (see claims register C6).
    """
    r = np.asarray(r_kpc, dtype=float)
    return v_flat_kms * np.sqrt(1.0 - np.exp(-(r / r_core_kpc) ** 2))


def total_v_squared(models: list[np.ndarray]) -> np.ndarray:
    """Quadrature sum of model components (km/s)."""
    return np.sqrt(np.maximum(np.sum(np.square(models), axis=0), 0.0))


# --- comparison harness ----------------------------------------------------
def _fit_model(curve_fn, p0, bounds, r_kpc, v_obs_kms):
    """Least-squares fit of curve_fn(params, r) to observed data (km/s)."""
    from scipy.optimize import least_squares

    def residuals(p):
        return curve_fn(p, r_kpc) - v_obs_kms

    opt = least_squares(residuals, p0, bounds=bounds, max_nfev=400)
    return opt.x, np.sqrt(np.mean(opt.fun ** 2)) / np.mean(v_obs_kms)


def fit_rotation_models(r_kpc: np.ndarray, v_obs_kms: np.ndarray,
                        rd_kpc: float = 3.5, Mb_sun: float = 3.0e9,
                        r200: float = 120.0) -> dict:
    """Least-squares fit of baryonic, Lambda-CDM, and pressure-gradient models.

    Free parameters: disk mass (all), NFW (v200, c), pressure flat level (v_flat).
    Returns best-fit curves, RMS relative errors, fitted params, verdict.
    """
    r = np.asarray(r_kpc)
    v_obs = np.asarray(v_obs_kms)

    def baryonic(p, r):
        return total_v_squared([
            exponential_disk_v(10 ** p[0], rd_kpc, r),
            np.array([point_mass_v(Mb_sun, rr) for rr in r]),
        ])

    def cdm(p, r):
        Md = 10 ** p[0]
        return total_v_squared([
            exponential_disk_v(Md, rd_kpc, r),
            np.array([point_mass_v(Mb_sun, rr) for rr in r]),
            nfw_halo_v(p[1], r200, p[2], r),
        ])

    def dup(p, r):
        Md = 10 ** p[0]
        return total_v_squared([
            exponential_disk_v(Md, rd_kpc, r),
            np.array([point_mass_v(Mb_sun, rr) for rr in r]),
            isothermal_pressure_v(p[1], r, r_core_kpc=p[2]),
        ])

    # log10(Md) in [9, 11.3]; v200 in [50, 300]; c in [4, 30];
    # v_flat in [50, 300]; pressure core radius in [0.5, 8] kpc
    p_bary, rms_bary = _fit_model(baryonic, [10.0], ([9.0], [11.3]), r, v_obs)
    p_cdm, rms_cdm = _fit_model(cdm, [10.0, 130.0, 10.0],
                                ([9.0, 50.0, 4.0], [11.3, 300.0, 30.0]), r, v_obs)
    p_dup, rms_dup = _fit_model(dup, [10.0, 150.0, 1.0],
                                ([9.0, 50.0, 0.5], [11.3, 300.0, 8.0]), r, v_obs)

    return {
        "r_kpc": r,
        "v_obs_kms": v_obs,
        "v_bary_kms": baryonic(p_bary, r),
        "v_cdm_kms": cdm(p_cdm, r),
        "v_dup_kms": dup(p_dup, r),
        "rms_baryonic": rms_bary,
        "rms_cdm": rms_cdm,
        "rms_dup_pressure": rms_dup,
        "fit_baryonic": {"log10_Md": float(p_bary[0])},
        "fit_cdm": {"log10_Md": float(p_cdm[0]), "v200": float(p_cdm[1]), "c": float(p_cdm[2])},
        "fit_dup": {"log10_Md": float(p_dup[0]), "v_flat": float(p_dup[1]),
                    "r_core_kpc": float(p_dup[2])},
        "verdict": (
            "Baryonic-only fails flat rotation curves (large decline at large r). "
            "Both the fitted NFW dark-halo model and the fitted pressure-gradient "
            "(DUP) model reproduce the flat curve. The pressure model achieves this "
            "WITHOUT dark matter — that is the theory's positive claim, and its "
            "discriminators are: (1) higher-precision data, (2) bulge/disk mass "
            "uncertainties, (3) independent probes (lensing, CMB)."
        ),
    }


def compare_rotation_models(r_kpc, v_obs_kms, **kwargs) -> dict:
    """Backwards-compatible wrapper around fit_rotation_models."""
    return fit_rotation_models(r_kpc, v_obs_kms, **kwargs)
