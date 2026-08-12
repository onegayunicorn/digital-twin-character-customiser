# Test Plan

**Owner:** Physics-Sim / Sensor-Design Agents · CI: `.github/workflows/ci.yml`

## 1. Test levels

| Level | Scope | Where | Gate |
|---|---|---|---|
| L0 Unit | Model functions, analytic values | `tests/unit/*` | PR |
| L1 Integration | Cross-package (sim → sensor → API), CLI smoke | `tests/integration/*` | PR |
| L2 Reproducibility | Fresh-container runs of all sims (Docker) | CI job | Release |
| L3 Hardware-in-Loop (HIL) | IPS bench rig vs calibrated pressure sources | Lab | Phase gates |
| L4 App/E2E | Web/mobile/desktop flows (VRmemories consent flow, dashboard) | Per-app CI | Release |

## 2. Current coverage (verified)

- `tests/unit/test_dup_physics.py` — DUP vs Kepler comparison, force laws, orbital speeds.
- `tests/unit/test_resonance.py` — carrier recovery, superposition spectra, beats.
- `tests/unit/test_ips_model.py` — phase shift, Lorentz force, reclaim rate, capacitor,
  Wien law.
- **Result: 23 tests passing** (`python3 -m pytest tests -q`).

## 3. Simulation validation criteria

- Every model function must have ≥1 analytic-value assertion (not just smoke).
- Comparative claims (e.g., Kepler vs DUP) must report residual metrics.
- Run parameters logged with every artifact (module, version, inputs, seed).

## 4. HIL validation protocol (IPS)

1. Calibrated pressure source (µPa → nPa envelope via controlled ion flux).
2. Record phase-shift vs pressure; compare to Δφ = 2πnL/λ prediction.
3. Reclaim test: known thermal-load profile; measure recovered energy vs η_S model.
4. Dump test: <5 ns response; thermal/EMI safety interlock verification.
5. Pass criteria: model within tolerance band (to be set from phase-0 data);
   any deviation → model update → register update (E2-E5).

## 5. App/platform tests

- VRmemories: consent flow (opt-in, deletion), data-path encryption, replay labeling.
- Dashboard: Twin-State UI state sync (event-sourced), telemetry ingestion.
- API: contract tests against `platform/schemas/base-types.md`.

## 6. CI quality gates

1. `python-sims`: install → run sims (smoke) → pytest.
2. `spec-integrity`: regenerate spec, verify 131×4 file counts.
3. `js-build`: pnpm install → api/web build.
4. Release: all of the above + L2 reproducibility job + claims-register diff check
   (new claims require register update — enforced by review).
