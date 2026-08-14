# Digital Twin Character Customizer (Aether Core)

A cinematic, web-based **digital twin character rig and operations platform**. Combines a
React 19 / TypeScript / Tailwind CSS v4 frontend with an Express / tRPC backend, backed by
Drizzle ORM. Features real-time 3D rendering via React Three Fiber, a GTA V-style dual-axis
facial feature matrix, a 24-hour lifestyle hour-allocation budget validator, a procedural AI
prompt router, a **simulation engine**, an **agent matrix evolution** engine, and a unified
operations dashboard with Star Seed NFT marketplace bridging.

**Version:** 4.1.0 · **Status:** Production Ready & Fully Tested

---

## What's inside

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | React 19, Vite, Wouter | Component rendering and client routing |
| **Styling** | Tailwind CSS v4, Lucide | Chiaroscuro aesthetic and responsive UI |
| **3D Rendering** | Three.js, @react-three/fiber, @react-three/drei | Real-time WebGL rendering, orbit controls, GLTF asset loading |
| **State** | Zustand | Centralized reactive store for heritage, features, lifestyle |
| **Backend** | Express 4, tRPC 11 | Type-safe procedure contracts and authentication |
| **Database** | MySQL/TiDB, Drizzle ORM | Users, journeys, telemetry persistence |
| **Simulation** | TypeScript engines | Lifestyle lifecycle, telemetry streams, Quantum Reality Interface |
| **Evolution** | Genetic algorithm engine | Agent matrix evolution across generations |
| **Testing** | Vitest | 12+ suites: lifestyle rules, store actions, GLTF registry, AI router, agent matrix, auth |

## Repository layout

```
├── cores/              # Shared core libraries (pure TS)
│   ├── types/          #   CharacterAttributes, Vector2D, CharacterProfile
│   ├── state/          #   Zustand customizer store (single source of truth)
│   ├── ai-router/      #   Procedural AI prompt router (parseAIPrompt)
│   ├── simulation/     #   Simulation engine core (tick, time-series, lifecycle)
│   └── agent-matrix/   #   Agent matrix evolution engine (GA)
├── engines/            # Domain engines
│   ├── lifestyle/      #   LifestyleBudget validation + stat modifiers
│   ├── feature-grid/   #   Dual-axis facial feature matrix math (-1.0..1.0)
│   ├── gltf-registry/  #   GLTF model registry (standing / armor / skull)
│   ├── mesh-pipeline/  #   GLSL heritage shader + morph target mapping
│   ├── telemetry/      #   7.83 Hz Schumann resonance telemetry stream
│   └── evolution/      #   Genome→phenotype mapping + fitness functions
├── web-app/            # React 19 + Vite + R3F + Tailwind v4 frontend
│   └── src/app/customizer/   #   4-page customizer: builder / ai-chat / showcase / saved
├── server/             # Express 4 + tRPC 11 + Drizzle (auth, journey, telemetry, characters)
├── shared/             # Shared constants
├── drizzle/            # Drizzle schema + SQL migrations
├── simulations/        # Runnable simulations (lifestyle, agent-matrix, telemetry, quantum)
├── hooks/              # Git hooks (pre-commit, commit-msg, pre-push, post-merge)
├── pipelines/          # Data pipelines + codegen (telemetry, manifest, registry sync)
├── environments/       # Docker, docker-compose, Makefile, env templates
├── .github/workflows/  # CI/CD pipelines
├── docs/               # Architecture, inventory, agent matrix, simulation docs
└── tests/              # Cross-package tests
```

## Quick start

```bash
npm install                # install all workspaces
npm run dev                # start the web app (Vite dev server)
npm test                   # run all Vitest suites
npm run typecheck          # TypeScript check across all packages
npm run build              # production build of web-app
```

### Simulations

```bash
npm run sim:lifestyle      # 24h lifestyle hour-allocation simulation
npm run sim:agent-matrix   # agent matrix evolution (GA) simulation
npm run sim:telemetry      # 7.83 Hz Schumann resonance telemetry stream
npm run sim:quantum        # Quantum Reality Interface physics protocol (5 phases)
npm run sim:all            # run all four
```

### Pipelines & hooks

```bash
npm run pipeline:telemetry # ingest → aggregate → report telemetry pipeline
npm run pipeline:manifest  # generate character manifest codegen
npm run pipeline:sync      # sync registry manifests
npm run hooks:install      # install git hooks (typecheck+tests on commit)
```

### Run environments

```bash
make dev                   # dev server
make build                 # production build
make test                  # run tests
make docker-build          # build web + api images
make docker-up             # compose up (web + api + mysql)
```

## Verification policy

- Every claim in the docs carries a status: `VERIFIED` / `SIMULATED` / `HYPOTHESIS`.
- All simulation outputs are computational predictions within their model's mathematical
  framework and are watermarked `SIMULATION`.
- Releases gate on CI (typecheck → test → build).

## Repository heritage

This monorepo grew out of the *Invisible Pressure Platform (IPP)* scaffold. The legacy IPP
theory, hardware, and platform-contract content remains under `packages/`, `platform/`,
`docs/theory`, and `apps/`; the Digital Twin platform lives in the directories above.
