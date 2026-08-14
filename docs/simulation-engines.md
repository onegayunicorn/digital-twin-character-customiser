# Simulation Engines

All simulations are **SIMULATED** — deterministic, seeded, and watermarked. Run everything
with `npm run sim:all`, or individually:

```bash
npm run sim:lifestyle      # cohort of 24h budgets + stat modifiers
npm run sim:agent-matrix   # GA evolution (see agent-matrix-evolution.md)
npm run sim:telemetry      # 7.83 Hz Schumann stream
npm run sim:quantum        # Quantum Reality Interface 5-phase protocol
```

## 1. Lifestyle hour-allocation simulation (`simulations/lifestyle/run.ts`)

- Seeds 256 random 24h allocations (default seed 2026).
- Validates every budget against the hard rules: sum = 24h, sleep ≥ 4h, no category > 8h.
- Computes stat modifiers per profile and reports cohort stat power (avg/max) plus the
  strongest profile.
- Writes `simulations/lifestyle/output/lifestyle-report.json`.

## 2. Agent matrix evolution simulation (`simulations/agent-matrix/run.ts`)

- Evolves a population of 48 character agents across 60 generations (override with
  `SIM_POPULATION`, `SIM_GENERATIONS`, `SIM_SEED`).
- Fitness: `characterGenomeFitness` (stat power + lifestyle balance).
- Prints a generation trajectory every 10 generations, the champion phenotype, its stat
  modifiers, and the final archetype distribution.
- Writes `simulations/agent-matrix/output/agent-matrix-report.json`.

## 3. Schumann telemetry simulation (`simulations/telemetry/run.ts`)

- Streams 240 deterministic samples of the 7.83 Hz resonance with noise, coherence decay
  toward a character harmony baseline, and entropy.
- Reports rolling coherence, first/last samples, and a coherence band histogram.
- Writes `telemetry-report.json` + `telemetry.csv`.

## Engine internals

### `cores/simulation`
- `mulberry32(seed)` — deterministic PRNG; `gaussian(rng)` — Box-Muller normal.
- `sampleOscillator(t, {frequency, amplitude, noise})` — sine + gaussian noise.
- `SimulationEngine` — tick loop with `dt`/`maxT`, time-series history, `step`/`run`/`reset`.
- `simulateLifestyleLifecycle(attributes, {days, volatility, statModifier})` — daily
  perturbation of the 24h allocation (renormalised each day), stat trajectory, best-day.

### `engines/telemetry`
- `createTelemetryEngine({dt, seed, bufferSize})` — Schumann wave + coherence/entropy/
  heartbeat channels; `run(steps, character)`; bounded buffer; `averageCoherence(engine)`.

## Determinism & verification

Every engine is seeded, so identical runs produce identical outputs (covered by tests).
All outputs carry a `SIMULATED` status field and are written under
`simulations/*/output/` (gitignored).
