# LAZER PHOTONIC ENTANGLEMENT / PERO — Analysis & Incorporation

**Source:** "☆▪︎LAZER▪︎PHOTONIC▪︎ENTANGLEMENT▪︎☆" (104 pages, AI-generated research orchestration)
**Date analyzed:** 2026-08-12 · **Status:** SCRIPT → incorporated as `packages/pero`
**Best document in the batch:** it correctly distinguishes classical from quantum optics.

## 1. What the document provides

- **Measured results** (450 nm blue laser through amethyst): splitting efficiency 52.14 %,
  spatial coherence 64.66 %, dominant spectral peak ~450 nm, macroscopic oscillation ~1.8 Hz;
  predicted coherence 91.13 % after 15° tilt + polarization alignment.
- **Honest physics:** the doc itself explains these are *classical* refraction/internal-
  reflection correlations — orders of magnitude below genuine quantum entanglement
  (SPDC probability 10⁻⁶–10⁻¹¹; Bell violation needs correlation > 70.7 % with coincidence
  counting, not image segmentation).
- **Upgrade path to real quantum:** stabilized 405 nm UV pump → BBO/PPLN nonlinear crystal →
  SPADs → TCSPC coincidence counting → filters → optical table/darkroom.
- **Complete monorepo blueprint (PERO):** orchestrator, hardware drivers (Thorlabs/Hamamatsu/
  Newport), experiments (amethyst baseline, quartz, BBO SPDC, KTP), analysis modules
  (spectral/temporal/spatial/quantum), qutip/qiskit simulators, FastAPI + WebSocket, models,
  ML, visualization dashboard.

## 2. Reality check — this is our claims discipline in action

| Metric | Archive (classical) | Genuine quantum requirement |
|---|---|---|
| Splitting efficiency | ~52 % geometric refraction | 10⁻⁶–10⁻¹¹ SPDC probability |
| Coherence | ~65 % spatial proxy | > 70.7 % Bell correlation |
| Measurement | image segmentation | coincidence counting (ns time-tag) |
| Scaling | billions of photons | discrete photon pairs |

The archive's terminology ("entanglement") overstates classical optics — exactly the kind
of claim our register exists to catch.

## 3. Incorporation

**`packages/pero`** — photonic analysis toolkit:
- Classical: splitting efficiency, spatial coherence (Pearson correlation of left/right
  lobe intensities), spectral decomposition (synthetic peak model), FFT oscillation
  analysis (1.8 Hz baseline), tilt/polarization coherence prediction model.
- Quantum: Bell S-parameter model (S = 2√2 max, 2 classical limit), SPDC coincidence
  model (rare-pair rate, coincidence window), verdict function that classifies a dataset
  as classical vs quantum-evidence.
- CLI + tests (analytic assertions: S ≤ 2 for classical input, > 2 for entangled model).

**Hardware sourcing impact:** adds a quantum-optics upgrade line to the sourcing plan
(405 nm stabilized laser, BBO/PPLN, SPADs, TCSPC, optical table).

## 4. Claims register mapping

| Claim | Status |
|---|---|
| Amethyst setup: 52.14 % efficiency / 64.66 % coherence / 450 nm / 1.8 Hz | SIMULATED baseline (reported from source; reproduce on own bench) |
| Predicted 91.13 % coherence after tilt+polarization | HYPOTHESIS (classical optics model; testable) |
| "Photonic entanglement" in amethyst archive | UNVERIFIED-CLAIM (classical, per the doc's own analysis) |
| SPDC / Bell / coincidence framework | VERIFIED (established quantum optics) |
