# Invisible Pressure Platform (IPP)

Monorepo for the **Invisible Pressure / DUP (Dimensional Unifying Pressure)** technology ecosystem.

**Author / IP owner:** Tyrone John Power (tpower86@live.com)
**Status:** Monorepo scaffold — v0.1.0 (pre-alpha)
**License:** MIT (software) — theory manuscript under separate IP terms

> **Honesty clause.** This repository formalizes an original physical hypothesis
> (Invisible Pressure / DUP) and its engineering, simulation, hardware, and business
> plan. Hypothesis ≠ established science: every scientific claim lives in
> [`docs/theory/04-claims-register.md`](docs/theory/04-claims-register.md) with a
> verification status, and nothing ships to market without the peer-review gates in
> [`docs/testing/peer-review-protocol.md`](docs/testing/peer-review-protocol.md).

---

## 1. What this is

A complete, platform-first build package covering:

| Domain | Deliverable |
|---|---|
| **Theory** | Consolidated Invisible Pressure / DUP theory, equations, IPS sensor spec, claims register |
| **Agents** | Agent roster (IpAI, physics-sim, sensor-design, peer-review, vr-memories, business) |
| **Simulation sandbox** | Runnable NumPy sims: DUP pressure-vs-gravity, resonance, IPS detection model |
| **Platform contract** | 131 Cloudflare capabilities → `platform/protocols|triggers|workflows|tasks` (525 files) |
| **Multi-platform apps** | Web (React), Mobile (Flutter), Desktop (Tauri) architecture |
| **AR/VR & Digital Twins** | VRmemories, energy-sphere visualization, twin sync architecture |
| **AI chat module** | Cloudflare AI Gateway + Workers AI + Vectorize RAG + memory |
| **Hardware** | IPS prototype BOM + sourcing plan (nanophotonics, DEC, supercaps, BCI) |
| **Business** | Business plan, GTM, revenue model, roadmap, domain strategy |
| **Quality** | Test plan, CI gates, arXiv-grade peer-review protocol |

## 2. Repository layout

```
├── apps/                     # Multi-platform frontends
│   ├── commerce-portal/      #   Sovereign Commerce portal + payments kiosk
│   ├── web/                  #   IPP portal console (Vite scaffold) + dashboard
├── cpp/                      # Compiled native modules
│   └── mutation_kernel/      #   C++ stop-codon/frameshift analysis kernel (g++ build)
│   ├── mobile/               #   Flutter app (iOS/Android)
│   └── desktop/              #   Tauri desktop shell
├── packages/                 # Shared libraries & services
│   ├── core/                 #   Types, config, constants
│   ├── theory-sim/           #   DUP physics + resonance + galaxy rotation (Python/NumPy/SciPy)
│   ├── earth-sim/            #   Pangaea Proxima: climate + tectonics models
│   ├── sensor/               #   IPS nanophotonic detection models (Python/NumPy)
│   ├── cpf-sim/              #   Crystal Planet Formation (nucleation/accretion)
│   ├── pero/                 #   Photonic analysis: classical metrics + Bell/SPDC quantum models
│   ├── ipai-cli/             #   IpAI MT Communion CLI (sentiment + resonance routing + engrams)
│   ├── sovereign/            #   Orchestrator core: agents, queue, scheduler, memory, tools, audit, HTTP API
│   ├── digital-twin/         #   Twin engine: event bus, state store, interpolation, heartbeat
│   ├── medgen/               #   Medical-genetics sims: DMD nonsense mutations, repair mechanisms, tumor dynamics (SIMULATED)
│   ├── genesis/              #   Genesis Engine: GA + SPSA optimizer (cleaned, numpy-only)
│   ├── medagents/            #   Healthcare agency agents: hospital triage, doctor case review, researcher match (decision-support only)
│   ├── sonar-5d/             #   Crystal-mesh geometry + 5D sonar sweep (OBJ export)
│   ├── bridge/               #   Software bridge: capability routing registry + handshake
│   ├── sovereign-commerce/   #   Commerce kernel: 14 domains, compliance OS, jurisdiction, ledger, procurement, NFC escrow, off-grid
│   ├── ai-chat/              #   LLM chat module (AI Gateway + Vectorize RAG)
│   ├── ar-vr/                #   WebXR scenes, sphere visualization
│   └── api/                  #   Cloudflare Workers API (REST/WebSocket)
├── platform/                 # Platform contract (generated, do not hand-edit)
│   ├── protocols/            #   131 protocol definitions
│   ├── triggers/             #   131 trigger definitions
│   ├── workflows/            #   131 workflow definitions
│   ├── tasks/                #   131 task definitions
│   ├── extensions/           #   6 app-layer capabilities (twin sync, orchestration, CLI, CPF, PERO, sphere)
│   ├── manifests/            #   Declarative configs (buckets, wrangler, CI)
│   └── schemas/              #   Base types & validation schemas
├── dashboard/                # Platform command dashboard (static HTML + status.json)
├── agents/                   # Agent definitions (YAML/MD)
├── docs/
│   ├── theory/               # Theory consolidation + claims register
│   ├── research/             # New-document analyses (diamond qubits, NAVT, FUTUREMAP, Earth-250M, RIPE)
│   ├── business/             # Business plan, GTM, revenue, roadmap, domain
│   ├── hardware/             # IPS BOM + sourcing plan
│   ├── platform/             # Architecture, multi-platform, AR/VR, AI chat, buckets
│   └── testing/              # Test plan + peer-review protocol
├── tests/                    # Cross-package tests
├── scripts/                  # Codegen & ops scripts
└── .github/workflows/        # CI/CD
```

## 3. Quick start

```bash
# Platform spec regeneration (after editing scripts/generate_platform_spec.py)
python3 scripts/generate_platform_spec.py

# Simulations
python3 -m pip install -r packages/theory-sim/requirements.txt
python3 -m theory_sim --mode dup --bodies 9          # DUP pressure-vs-gravity comparison
python3 -m theory_sim --mode resonance --freq 7.83    # resonance wave sim
python3 -m sensor --mode detect                       # IPS phase-shift / reclaim sim

# Tests
python3 -m pytest tests -v
```

## 4. Platform contract

The 131-item Cloudflare Permissions & Capabilities list is fully formalized under
[`platform/`](platform/) — every capability maps to a Protocol (interface contract),
Trigger(s) (event sources), Task(s) (atomic units), and Workflow(s) (end-to-end process).
Base types in [`platform/schemas/base-types.md`](platform/schemas/base-types.md).

## 5. Product lines

1. **IPS Sensor & Energy-Sphere** — nanophotonic invisible pressure sensing, entropy-waste
   recovery, twin-state dashboard (hardware + software).
2. **VRmemories** — VR preservation of personal essence: emotion, voice, language patterns,
   consent-first (privacy & ethics core).
3. **Theory-as-Service (DUP)** — licensed simulation toolkit, peer-reviewed data products,
   and research-grade sensor data pipelines.

See [`docs/business/business-plan.md`](docs/business/business-plan.md) for the full package.

## 6. Verification policy

- All claims carry a status: `VERIFIED` / `SIMULATED` / `HYPOTHESIS` / `UNVERIFIED-CLAIM`.
- Nothing labeled `UNVERIFIED-CLAIM` is presented as fact (see claims register).
- Releases gate on CI (lint → test → build) and, for scientific artifacts, the peer-review
  protocol.
