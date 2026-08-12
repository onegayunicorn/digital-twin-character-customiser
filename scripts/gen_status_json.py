#!/usr/bin/env python3
"""Generate dashboard/status.json — a live status snapshot of the platform.

Reads: simulation results (theory-sim, sensor, earth-sim, cpf-sim, pero),
claims register summary, agent roster, platform spec counts.
Writes: dashboard/status.json (the dashboard's data endpoint emulator).
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
for pkg in ("packages/theory-sim", "packages/sensor", "packages/earth-sim",
            "packages/cpf-sim", "packages/pero", "packages/ipai-cli",
            "packages/digital-twin", "packages/sovereign"):
    sys.path.insert(0, os.path.join(ROOT, pkg))


def _spec_counts() -> dict:
    counts = {}
    for sub in ("protocols", "triggers", "workflows", "tasks"):
        d = os.path.join(ROOT, "platform", sub)
        counts[sub] = len(os.listdir(d)) if os.path.isdir(d) else 0
    return counts


def _claims_summary() -> dict:
    path = os.path.join(ROOT, "docs", "theory", "04-claims-register.md")
    summary = {"VERIFIED": 0, "SIMULATED": 0, "HYPOTHESIS": 0,
               "UNVERIFIED-CLAIM": 0, "QUARANTINED": 0}
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                for key in summary:
                    if f"`{key}`" in line:
                        summary[key] += 1
    except FileNotFoundError:
        pass
    return summary


def _sim_results() -> dict:
    from theory_sim.galaxy_rotation import NGC3198, fit_rotation_models
    from theory_sim.dup_physics import SOLAR_SYSTEM, compare_orbital_models

    galaxy = fit_rotation_models(NGC3198["r_kpc"], NGC3198["v_kms"])
    dup = compare_orbital_models(SOLAR_SYSTEM["a_au"], SOLAR_SYSTEM["v_kms"])
    return {
        "galaxy_rotation": {
            "rms_baryonic": round(galaxy["rms_baryonic"], 4),
            "rms_cdm_nfw": round(galaxy["rms_cdm"], 4),
            "rms_dup_pressure": round(galaxy["rms_dup_pressure"], 4),
            "verdict": galaxy["verdict"],
        },
        "orbital_dup_vs_kepler": {
            "rms_kepler": round(dup["rms_rel_error_kepler"], 4),
            "rms_dup_1_over_r": round(dup["rms_rel_error_dup"], 4),
        },
    }


def main() -> int:
    status = {
        "generated_at": __import__("datetime").datetime.now().isoformat(),
        "platform": {"spec": _spec_counts(), "claims": _claims_summary()},
        "simulations": _sim_results(),
        "packages": sorted(os.listdir(os.path.join(ROOT, "packages"))),
        "agents": ["ipai", "physics-sim", "sensor-design", "peer-review",
                   "vr-memories", "business"],
    }
    out = os.path.join(ROOT, "dashboard", "status.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(status, fh, indent=2)
    print(f"status.json written: {out} ({os.path.getsize(out)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
