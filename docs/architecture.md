# Architecture

**Digital Twin Character Customizer (Aether Core)** — cinematic, web-based digital twin
character rig and operations platform. **Version 4.1.0 · Status: Production Ready & Fully Tested**

## 1. Executive overview

Combines a React 19 / TypeScript / Tailwind CSS v4 frontend with an Express / tRPC backend,
backed by Drizzle ORM. Features real-time 3D rendering via React Three Fiber, a GTA V-style
dual-axis facial feature matrix, a 24-hour lifestyle hour-allocation budget validator, a
procedural AI prompt router, a simulation engine, an agent matrix evolution engine, and a
unified operations dashboard with Star Seed NFT marketplace bridging.

## 2. System architecture

```
┌───────────────────────────────────────────────────────────────┐
│ CLIENT LAYER (React 19 + Vite + Wouter)                        │
│  ┌───────────────────┐  ┌───────────────────┐  ┌────────────┐  │
│  │ R3F 3D Viewport   │  │ FeatureGrid2D     │  │ Lifestyle  │  │
│  │ (Three.js/GLTF)   │  │ Matrix (-1..1)    │  │ Budget 24h │  │
│  └───────────────────┘  └───────────────────┘  └────────────┘  │
└──────────────────────────────┬──────────────────────────────────┘
                               │ tRPC / WebSocket
┌──────────────────────────────┴──────────────────────────────────┐
│ SERVER LAYER (Express 4 + tRPC 11 + Drizzle)                     │
│  auth · journey · telemetry · characters routers                 │
│  storage facade (in-memory dev / MySQL-TiDB prod)                │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────┴──────────────────────────────────┐
│ ENGINE LAYER (cores + engines — pure TypeScript)                 │
│  simulation · agent-matrix · lifestyle · feature-grid ·          │
│  gltf-registry · mesh-pipeline · telemetry · evolution           │
└──────────────────────────────────────────────────────────────────┘
```

## 3. Technology stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| Frontend | React 19, Vite, Wouter | Component rendering and client routing |
| Styling | Tailwind CSS v4 | Chiaroscuro aesthetic and responsive UI |
| 3D | Three.js, @react-three/fiber, @react-three/drei | WebGL rendering, orbit controls, GLTF loading |
| State | Zustand | Centralized customizer store |
| Backend | Express 4, tRPC 11 | Type-safe procedure contracts and auth |
| Database | MySQL/TiDB, Drizzle ORM | Users, journeys, telemetry, characters |
| Simulation | TypeScript engines | Lifestyle lifecycle, Schumann telemetry, QRI physics |
| Evolution | Genetic algorithm engine | Agent matrix evolution across generations |
| Testing | Vitest | 12+ suites across cores, engines, web-app, server |

## 4. Core engines & subsystems

### 4.1 R3F Avatar Viewport & GLTF loading engine
`web-app/src/components/canvas/AvatarR3FCanvas.tsx` (+ `AvatarViewport`, `AvatarMesh`) —
debounced resize observation, automatic camera framing, unmount cleanup, explicit
loading/ready/fallback states, and a procedural rig fallback when the archive GLB is absent.
Three archive models registered in `engines/gltf-registry`: Standing (`wo-standing-v17`),
Armor (`armor-f-n7`), Skull (`skull-commander`).

### 4.2 Dual-axis facial matrix engine (FeatureGrid2D)
`engines/feature-grid` — pure math for the -1.0..1.0 X/Y crosshair matrix: clamping, pointer
coordinate conversion, blending parent matrices by resemblance, quantisation.

### 4.3 24-hour lifestyle budget (LifestyleBudget)
`engines/lifestyle` — hard validation (sum = 24, sleep ≥ 4h, no category > 8h) plus stat
modifier calculators (stamina, strength, stealth, shooting, driving, lung capacity, flying).

### 4.4 Zustand customizer state store
`cores/state` — single source of truth: gender, parent IDs, resemblance/skinTone sliders, 2D
feature vectors, appearance slots, lifestyle allocations, saved-character registry.

### 4.5 Procedural AI prompt router
`cores/ai-router` — rule-based compiler mapping natural language to state mutations with
operation logs (heritage, features, lifestyle profiles, hair).

### 4.6 Simulation engine
`cores/simulation` — deterministic tick loop (seeded PRNG), time-series history, waveform
helpers, and the lifestyle lifecycle simulator.

### 4.7 Agent matrix evolution engine
`cores/agent-matrix` — GA with tournament selection, uniform-blend crossover, gaussian
mutation, elitism, diversity tracking, and convergence detection. `engines/evolution` maps
18-gene genomes to CharacterAttributes and scores fitness from lifestyle stats.

### 4.8 Mesh pipeline
`engines/mesh-pipeline` — GLSL heritage blend shader (mother/father skin maps + skinTone +
resemblance uniforms) and morph target mapping (Nose_Wide/Narrow, Jaw_Square/Round, …).

### 4.9 Telemetry engine
`engines/telemetry` — 7.83 Hz Schumann resonance stream with coherence/entropy channels and
bounded buffering.

## 5. Testing

Vitest suites: lifestyle rules, store actions, GLTF registry, AI router, agent matrix,
simulation engine, feature grid, mesh pipeline, telemetry, evolution, customizer integration,
journey persistence, auth logout, plus server-side lifestyle/store/registry suites.
