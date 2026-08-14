# File & Folder Inventory

Complete directory tree of the Digital Twin Character Customizer monorepo
(generated from the built artifact; legacy IPP content omitted).

```
.
├── package.json                  # Workspaces: cores/*, engines/*, web-app, server, shared, …
├── pnpm-workspace.yaml           # Workspace globs (incl. legacy apps/*, packages/*)
├── tsconfig.base.json            # Shared compiler options
├── tsconfig.json                 # Cross-package typecheck with @dt-* path aliases
├── vitest.config.ts              # Single vitest config for all packages
├── README.md                     # Project overview + quick start
├── LICENSE                       # MIT
│
├── cores/                        # Shared core libraries (pure TS)
│   ├── types/                    #   Vector2D, FeatureMatrix, CharacterAttributes, stats
│   │   └── src/index.ts
│   ├── state/                    #   Zustand store (useCustomizerStore, vanilla factory)
│   │   └── src/{index.ts, index.test.ts}
│   ├── ai-router/                #   parseAIPrompt procedural compiler
│   │   └── src/{index.ts, index.test.ts}
│   ├── simulation/               #   SimulationEngine, PRNG, oscillator, lifecycle sim
│   │   └── src/{index.ts, index.test.ts}
│   └── agent-matrix/             #   MatrixEvolutionEngine (GA)
│       └── src/{index.ts, index.test.ts}
│
├── engines/                      # Domain engines
│   ├── lifestyle/                #   Budget validation + stat modifiers
│   │   └── src/{index.ts, index.test.ts}
│   ├── feature-grid/             #   Dual-axis matrix math
│   │   └── src/{index.ts, index.test.ts}
│   ├── gltf-registry/            #   3 archive GLB models
│   │   └── src/{index.ts, index.test.ts}
│   ├── mesh-pipeline/            #   GLSL heritage shader + morph targets
│   │   └── src/{index.ts, index.test.ts}
│   ├── telemetry/                #   7.83 Hz Schumann stream
│   │   └── src/{index.ts, index.test.ts}
│   └── evolution/                #   Genome ↔ phenotype + fitness
│       └── src/{index.ts, index.test.ts}
│
├── web-app/                      # React 19 + Vite + R3F + Tailwind v4
│   ├── index.html · vite.config.ts · tsconfig.json
│   ├── public/{favicon.svg, robots.txt}
│   └── src/
│       ├── main.tsx · App.tsx · index.css
│       ├── app/customizer/
│       │   ├── layout.tsx                        # 4-page sidebar shell
│       │   ├── builder/page.tsx                  # Character Builder
│       │   ├── ai-chat/page.tsx                  # Procedural Matrix Assistant
│       │   ├── showcase/page.tsx                 # Studio/pose viewer
│       │   ├── saved/page.tsx                    # Deployment Registry
│       │   └── customizer.integration.test.ts
│       ├── components/
│       │   ├── canvas/{AvatarR3FCanvas, AvatarMesh, AvatarViewport}.tsx
│       │   ├── canvas/shaders/HeritageShaderMaterial.ts
│       │   ├── customizer/{FeatureGrid2D, LifestyleBudget}.tsx
│       │   ├── dashboard/NFTMarketplaceBridge.tsx
│       │   ├── Navbar.tsx · ui.tsx
│       ├── contexts/ThemeContext.tsx
│       ├── hooks/{useCustomizerState, useAvatarMesh, useTelemetry, useSimulation, useAgentMatrix}.ts
│       ├── pages/{Home, JourneyPage, TelemetryPage, GlobalModePage, CustomizerPage, OperationsDashboardPage, NotFound}.tsx
│       ├── stores/useCustomizerStore.ts
│       └── utils/{statCalculators, aiPromptRouter}.ts
│
├── server/                       # Express 4 + tRPC 11 + Drizzle
│   ├── index.ts                  #   Express bootstrap + telemetry ingestion
│   ├── routers.ts                #   auth / journey / telemetry / characters routers
│   ├── db.ts                     #   Storage facade query helpers
│   ├── _core/{trpc, env, oauth, storage}.ts
│   └── {lifestyle, store, gltf.registry, journey, auth.logout}.test.ts
│
├── shared/src/index.ts           # Shared constants
├── drizzle/
│   ├── schema.ts                 # users, journeys, telemetry, characters (MySQL)
│   ├── drizzle.config.ts
│   └── migrations/0000_initial.sql
│
├── simulations/                  # Runnable simulations (tsx)
│   ├── lifestyle/run.ts          #   24h budget cohort sim
│   ├── agent-matrix/run.ts       #   GA evolution sim
│   ├── telemetry/run.ts          #   Schumann stream sim
│   └── quantum-interface/
│       ├── run.ts                #   5-phase QRI physics protocol
│       └── dashboard-template.html
│
├── hooks/                        # Git hooks (pre-commit, commit-msg, pre-push, post-merge)
│   ├── install-hooks.sh · chmod-hooks.sh
├── pipelines/                    # Data pipelines
│   ├── telemetry-pipeline.ts     #   ingest → aggregate → report
│   ├── manifest-generator.ts     #   character manifest codegen
│   └── sync-registry.ts          #   manifest ↔ GLTF registry cross-check
│
├── environments/                 # Run environments
│   ├── Dockerfile · nginx.conf · docker-compose.yml · .env.example · Makefile · README.md
│
├── .github/workflows/            # CI/CD
│   ├── ci.yml · deploy.yml
│
├── docs/                         # This documentation set
│   ├── README.md · architecture.md · file-inventory.md · agent-matrix-evolution.md
│   ├── simulation-engines.md · quantum-reality-interface.md · run-environments.md
│
└── tests/                        # Cross-package tests
    └── cross-package.test.ts
```

## Test inventory

| Suite | Location |
| :--- | :--- |
| Store actions | `cores/state`, `server/store.test.ts`, web-app integration |
| Lifestyle rules | `engines/lifestyle`, `server/lifestyle.test.ts` |
| AI prompt router | `cores/ai-router` |
| Agent matrix GA | `cores/agent-matrix` |
| Simulation engine | `cores/simulation` |
| Feature grid | `engines/feature-grid` |
| GLTF registry | `engines/gltf-registry`, `server/gltf.registry.test.ts` |
| Mesh pipeline | `engines/mesh-pipeline` |
| Telemetry | `engines/telemetry` |
| Evolution | `engines/evolution` |
| Journey persistence | `server/journey.test.ts` |
| Auth logout | `server/auth.logout.test.ts` |
| Cross-package | `tests/cross-package.test.ts` |
