# R2 Bucket Data-Lake Layout

Canonical manifest: [`manifests/buckets.yaml`](../../manifests/buckets.yaml).

## 1. Bucket map

| Bucket | Contents | Access | Retention |
|---|---|---|---|
| `dev-ipp-docs` | Theory manuscripts, claims register, peer-review artifacts | Private + signed URLs (reviewers) | Versioned, 5 yr |
| `dev-ipp-sims` | Sim traces (JSON/CSV), figures, run logs | Private; public subpath for published figures | 90 d hot → cold |
| `dev-ipp-sensor` | Raw IPS telemetry (phase-shift, reclaim logs) | Private, Workers-only | Append-only, 400 d |
| `dev-ipp-vrmemories` | VR captures, voice/emotion models, scenes | Private, per-user signed URLs | User-owned; hard delete API |
| `dev-ipp-apps` | APK/EXE/DMG bundles, OTA, web assets | Public CDN | 30 d old versions pruned |
| `dev-ipp-models` | Embeddings, fine-tuned weights, checkpoints | Private | Versioned, immutable |
| `dev-ipp-archive` | Sealed milestones (Yggdrasil taxonomy) | Private, audit-gated | WORM, object lock |

## 2. Key conventions

- Keys: `<env>/<domain>/<kind>/<yyyymmdd>/<id>.<ext>` — e.g.
  `dev/sensor/telemetry/20260812/mod-ips-001.jsonl`.
- Partitions by day for telemetry; by version for models/artifacts.
- Lifecycle rules mandatory (cost control); 80% budget alerts via `BillingWrite` metrics.

## 3. Access paths

- Workers access via R2 bindings (no public keys ever).
- Reviewer/public access via signed URLs (`WorkersR2StorageWrite` workflow:
  Validate → Upload → Index → Set lifecycle → Purge cache).
- VRmemories: per-user scoped signed URLs; zero anonymous exposure.

## 4. Governance

- WORM archive (`dev-ipp-archive`) holds sealed theory versions — every peer-review
  milestone is sealed (immutable object lock) for provenance.
- PII/health-adjacent data client-side encrypted before upload (see `DLSWrite` +
  `ZeroTrustPIIRead`).

## 5. Cost model (planning)

- Sim/docs/telemetry scale with research volume (low); VR memories scale with users
  (medium); apps/models small. Re-estimate quarterly vs `BillingWrite` reports.
