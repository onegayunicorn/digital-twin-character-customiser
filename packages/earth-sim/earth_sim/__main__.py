"""CLI runner for the Pangaea Proxima (Earth 250M) simulation.

Usage:
  python3 -m earth_sim --mode climate [--t MYR] [--quiet]
  python3 -m earth_sim --mode tectonic [--quiet]
"""
from __future__ import annotations

import argparse
import sys


def _run_climate(t_myr: float, quiet: bool) -> int:
    from .climate import ClimateModel

    m = ClimateModel()
    state = m.get_climate_state(t_myr)
    if quiet:
        print(f"climate ok @{t_myr}Myr: T={state.global_mean_temp_c:.1f}C "
              f"CO2={state.co2_ppm:.0f}ppm sea={state.sea_level_m:.1f}m")
        return 0
    print("=" * 60)
    print(f"Pangaea Proxima climate @ t = {t_myr} Myr")
    print("=" * 60)
    print(f"  CO2                    : {state.co2_ppm:.0f} ppm")
    print(f"  Global mean temperature: {state.global_mean_temp_c:.1f} C "
          f"(anomaly {state.global_mean_temp_c - 14.0:+.1f} C)")
    print(f"  Sea level              : +{state.sea_level_m:.1f} m")
    print(f"  Precipitation          : {state.precipitation_mm_yr:.0f} mm/yr")
    print(f"  Ice cover              : {state.ice_cover_pct:.1f} %")
    return 0


def _run_tectonic(quiet: bool) -> int:
    from .tectonics import TectonicSimulation

    sim = TectonicSimulation()
    history = sim.run_full(250.0)
    final = history["positions"][-1]
    if quiet:
        print(f"tectonic ok: {len(history['time'])} steps, "
              f"{len(history['orogenies'])} orogenies")
        return 0
    print("=" * 60)
    print("Tectonic simulation — final plate centroids @ 250 Myr")
    print("=" * 60)
    for name, pos in final.items():
        print(f"  {name:<16} lat {pos['lat']:>7.1f}  lon {pos['lon']:>8.1f}")
    print(f"  Events ({len(history['orogenies'])}):")
    for e in history["orogenies"]:
        print(f"    - {e['event']} @ {e['time_myr']} Myr, peak {e['peak_elevation_m']:.0f} m "
              f"[{e.get('source', 'n/a')}]")
    print("  NOTE: documented plate velocities are ~10x slower than real rates;")
    print("        assembly events are narrative boundary conditions (see claims register).")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="earth_sim", description="Earth 250M simulations")
    ap.add_argument("--mode", choices=["climate", "tectonic"], default="climate")
    ap.add_argument("--t", type=float, default=250.0, help="time in Myr")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    if args.mode == "climate":
        return _run_climate(args.t, args.quiet)
    return _run_tectonic(args.quiet)


if __name__ == "__main__":
    sys.exit(main())
