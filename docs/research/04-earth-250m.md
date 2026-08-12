# Earth in 250 Million Years (Pangaea Proxima) — Analysis & Incorporation

**Source:** "🌍 Earth in 250 Million Years — Complete Synthesis" (AI-generated, but *data-model-backed*)
**Date analyzed:** 2026-08-12 · **Overall status:** SIMULATED (models implemented and tested)

## 1. What the document provides

A structured Pangaea Proxima synthesis with *real, implementable models*:

- **Tectonics:** plate list with present centroids + velocity vectors (deg/Myr), collision
  pair detection, orogeny events; narrative timeline (Atlantic cessation @150 Myr, Himalaya
  peak @180 Myr, Mediterranean closure @210 Myr, final assembly @250 Myr).
- **Climate:** exponential CO₂ ramp 420 → 950 ppm; temperature forcing
  `ΔT = 3.0 × log₂(CO₂/280)` (IPCC mid-range climate sensitivity); sea level = thermal +
  ice-melt; biome distribution; paleogeographic coordinate dataset.

## 2. Model verification (what we found running it)

| Quantity | Narrative claim | Model output (implemented) | Status |
|---|---|---|---|
| End CO₂ | 950 ppm | 950 ppm | Consistent |
| End temperature | 21.5 °C (+7.5 °C) | 19.3 °C (+5.3 °C) | **Narrative ≠ its own model** |
| Sea level | +65 m | +30.4 m | **Narrative ≠ its own model** |
| Plate assembly events | 4 orogenies by 250 Myr | 0 derived collisions (documented vectors ~10× too slow) | **Motion engine doesn't assemble; events are narrative boundary conditions** |

The document's narrative numbers (+7.5 °C, +65 m) do not follow from its own documented
equations — we implement the equations (SIMULATED) and register the narrative claims as
UNVERIFIED. The plate-velocity issue is a real finding: the documented vectors
(0.05–0.4 deg/Myr) are ~10× slower than real plate rates.

## 3. Claims register mapping

| Claim | Status |
|---|---|
| Climate model equations (exp CO₂ ramp, log forcing α=3.0) | SIMULATED (implemented, tested) |
| End state 950 ppm / 19.3 °C / +30.4 m | SIMULATED |
| Narrative +7.5 °C / +65 m / Pangaea Proxima assembly | UNVERIFIED-CLAIM |
| Wilson-cycle supercontinent cycling | VERIFIED (established geology) |

## 4. Incorporation into the platform

- **New package:** `packages/earth-sim` — `earth_sim/climate.py` + `earth_sim/tectonics.py`,
  CLI (`python3 -m earth_sim --mode climate|tectonic`), tests in
  `tests/unit/test_earth_sim.py` (6 tests).
- **Value:** a credible, tested geoscience simulation for the platform's research
  portfolio; can feed AR/VR visualizations (Pangaea Proxima globe in `packages/ar-vr`).
- **Honesty:** outputs documented as SIMULATED; narrative mismatches recorded in the
  claims register — this is exactly the discipline that makes the platform publishable.
