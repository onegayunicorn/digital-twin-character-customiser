# Agent Roster — Invisible Pressure Platform

Named agents operating over the platform contract ([`platform/`](../platform/README.md)),
simulation stack, and business plan. Each definition is deployable as an LLM agent
(Cloudflare Workers AI / AI Gateway) or a deterministic pipeline, per the agent protocols
in `platform/protocols/AgentMemoryWriteProtocol.md`, `CFAgentsWriteProtocol.md`, and
`WorkersAIWriteProtocol.md`.

| Agent | Mission | Primary artifacts |
|---|---|---|
| [**IpAI**](ipai.md) | Invisible Pressure AI — theory reasoning core; owns the claims register and falsification discipline | `docs/theory/*`, `packages/theory-sim` |
| [**Physics-Sim**](physics-sim-agent.md) | Runs and extends DUP/resonance simulations; comparative tests | `packages/theory-sim`, `tests/unit/test_dup_physics.py` |
| [**Sensor-Design**](sensor-design-agent.md) | IPS hardware/software co-design; DEC + Twin-State UI | `packages/sensor`, `docs/theory/03-ips-spec.md`, `docs/hardware/*` |
| [**Peer-Review**](peer-review-agent.md) | Preprint packaging, reproducibility checks, review-board facilitation | `docs/testing/peer-review-protocol.md` |
| [**VR-Memories**](vr-memories-agent.md) | VR essence-preservation product; ethics, consent, privacy | `docs/business/*`, `packages/ar-vr` |
| [**Business**](business-agent.md) | Go-to-market, revenue, roadmap, domain, fundraising | `docs/business/*` |

## Operating rules (all agents)

1. **Claims discipline:** never present `HYPOTHESIS`/`UNVERIFIED-CLAIM` as fact
   (`docs/theory/04-claims-register.md`).
2. **Contract-first:** cross-platform behavior maps to `platform/` protocol/trigger/
   workflow/task files; agents register new capabilities by adding spec entries.
3. **Deterministic gates:** CI + tests gate every change; scientific claims additionally
   gate on the peer-review protocol.
4. **Consent & privacy:** VRmemories and sensor data paths enforce consent-first design
   (see `manifests/buckets.yaml`).
