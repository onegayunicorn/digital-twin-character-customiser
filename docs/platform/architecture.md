# Platform Architecture

**Stack:** Cloudflare-first · **Contract:** [`platform/README.md`](../../platform/README.md)
(131 capabilities → protocols/triggers/workflows/tasks)

## 1. System overview

```
                     ┌──────────────────────────────────────────────┐
                     │                 CLIENTS                       │
                     │  Web (React) · Mobile (Flutter) · Desktop    │
                     │  (Tauri) · AR/VR (WebXR/Unity) · IPS HW      │
                     └───────────────┬──────────────────────────────┘
                                     │ HTTPS / WSS
                     ┌───────────────▼──────────────────────────────┐
                     │       CLOUDFLARE EDGE (Workers + D1 + KV)    │
                     │  AI Gateway · Vectorize · Queues · Realtime  │
                     │  R2 (buckets) · Turnstile · WAF · DNS        │
                     └───────┬───────────────┬──────────────┬───────┘
                             │               │              │
              ┌──────────────▼──┐   ┌────────▼───────┐   ┌───▼────────────┐
              │  THEORY-SIM     │   │  SENSOR/IPS    │   │  VR MEMORIES   │
              │  (DUP/resonance)│   │  telemetry     │   │  (twin data)   │
              └─────────────────┘   └────────────────┘   └────────────────┘
```

All cross-cutting behavior (auth, secrets, notifications, observability, rate limits)
is defined once in the platform contract and referenced, not re-implemented.

## 2. Service map (Workers)

| Worker | Path | Bindings | Spec refs |
|---|---|---|---|
| `api` | REST + WebSocket | D1, KV, R2, Queues, Vectorize | `AccountAPIGateway`, `MessagingRead`, `WorkersR2StorageWrite` |
| `ai-chat` | LLM chat + RAG | AI Gateway, Vectorize, KV (session) | `AIGatewayWrite`, `AutoRagWrite`, `VectorizeWrite` |
| `realtime` | Twin-state sync | Durable Objects / Realtime | `RealtimeAdmin` |
| `ingest` | Sensor telemetry intake | R2, Queues, D1 | `IOTWrite`, `WorkersObservabilityTelemetryWrite` |
| `web` | Static app hosting | R2 (assets) | `WorkersScriptsWrite` |
| `jobs` | Scheduled pipelines (sweeps, reports) | Queues, R2 | `PipelinesWrite`, `WorkersCITask` |

## 3. Data layer

| Store | Use | Spec ref |
|---|---|---|
| D1 | Relational: users, subscriptions, sensor configs, twin manifests | `D1Write` |
| KV | Session/cache/feature flags | `WorkersKVStorageWrite` |
| R2 | Object lake: sims, telemetry, VR assets, docs, artifacts | `WorkersR2StorageWrite` |
| Vectorize | Embeddings: theory docs, VR memory constructs, chat RAG | `VectorizeWrite` |
| Queues | Async: telemetry batches, notification fan-out, sim jobs | `QueuesWrite` |
| Hyperdrive | D1 connection pooling | `HyperdriveWrite` |

Layout per [`buckets.md`](buckets.md) and [`manifests/buckets.yaml`](../../manifests/buckets.yaml).

## 4. Security posture

- Zero-trust defaults (`ZeroTrustWrite`): every origin request authenticated; mTLS for
  device↔edge (`AccessMutualTLSCertificatesWrite`).
- Secrets via secrets store + Chamber (`ChamberSecretsProtocol`) — never in code.
- WAF managed rules + Turnstile on auth surfaces (`AccountWAFWrite`, `TurnstileSitesWrite`).
- PII paths (VRmemories, sensor data) client-side encrypted; DLP per `DLSWrite`.

## 5. Observability

- OpenTelemetry pipeline (`WorkersObservabilityTelemetryWrite`), metrics + alerts
  (`WorkersObservabilityWrite`), logpush to R2 (`LogsWrite`).
- DORA metrics tracked per release (throughput, stability, recovery).

## 6. Deployment

- Workers via wrangler (CI in `.github/workflows/ci.yml`); versioned deployments;
  staged rollouts via feature flags (`FlagshipWrite`).
- Reproducibility containers for sims; spec-integrity gate enforced in CI.
