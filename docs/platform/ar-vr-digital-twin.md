# AR/VR & Digital Twins

## 1. Twin-State concept → engineering

The IPS dashboard's "entanglement twin" concept is implemented as an **event-sourced
digital twin**:

- Physical state (sphere charge, Ψ-sync, capacitor tension) → **state events** with
  monotonic sequence numbers.
- Twins (UI spheres, VR scenes, remote dashboards) replay/subscribe to the event stream;
  phase-sync = `apply(events) → same state` in every twin.
- Latency budget: <100 ms sync; UI "instant transitions" are pre-rendered state swaps
  (no loading screens), matching the zero-chrome design.

Spec refs: `RealtimeAdmin` (presence/rooms), `ConstellationWrite` (graph sync),
`WorkersObservabilityTelemetryWrite` (telemetry ingest).

## 2. Components

| Component | Tech | Purpose |
|---|---|---|
| `packages/ar-vr` | Three.js + WebXR | Energy-sphere visualization, VRmemories scenes |
| `packages/digital-twin` | TS event-sourcing lib | Twin state machine, replay, reconciliation |
| Unity export path | Unity 2022+ | High-fidelity VRmemories experiences (Quest/Pico) |
| Realtime worker | Durable Objects | Event fan-out, presence, conflict resolution |

## 3. VRmemories pipeline (consent-first)

```
Capture (voice/emotion/language) → Consent audit → Memory construct
  (embeddings + scene graph + emotion timeline) → Encrypt (client-side) → R2
  → VR replay (labeled "reconstruction") → User deletion (hard delete + audit)
```

Ethics rules (from `agents/vr-memories-agent.md`):
1. Documented informed consent at capture; consent of all depicted parties at replay.
2. In-experience labeling of AI reconstructions.
3. Real delete with audit trail; no retention beyond user choice.

## 4. Digital twin for IPS hardware

- Every deployed sensor module gets a twin: `twin_id`, config, live telemetry, predicted
  vs actual reclaim.
- Twins enable: remote calibration, anomaly detection (Ψ-sync instability), fleet dashboards.
- Sensor fleet data flows: `IOTWrite` (device registry) → ingest worker → R2 + D1 →
  twin store → dashboards/VR views.

## 5. Sandbox (AR/VR + sim)

- WebXR playground at `sim.invisiblepressure.com`: load any `theory-sim` output
  (rotation curves, resonance spectra) as interactive 3D scenes.
- Scene ↔ sim contract: sims emit JSON traces → twin renders them; one schema,
  two consumers (2D dashboard, VR scene).
