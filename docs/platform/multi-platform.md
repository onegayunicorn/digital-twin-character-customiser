# Multi-Platform Applications & Native Scalability

## 1. Target platforms

| Platform | Stack | Entry |
|---|---|---|
| Web | React 18 + Vite (SPA) | `apps/web` |
| Mobile (iOS/Android) | Flutter (single codebase; native compile) | `apps/mobile` |
| Desktop (Win/macOS/Linux) | Tauri (Rust shell + webview) | `apps/desktop` |
| AR/VR | WebXR (browser) + Unity export path | `packages/ar-vr` |
| Hardware edge | ESP32/RP2040 firmware (telemetry) | `packages/sensor` firmware branch |

Shared logic lives in `packages/core` (types, config, validation against
`platform/schemas/base-types.md`); each client is a thin adapter.

## 2. Architecture pattern

- **Monorepo:** pnpm workspaces (`apps/*`, `packages/*`) with shared packages.
- **API-first:** all clients consume the Workers API (REST + WebSocket). No client-side
  business logic duplication.
- **State sync:** Twin-State dashboard + VRmemories scenes use the event-sourced sync
  defined in [`ar-vr-digital-twin.md`](ar-vr-digital-twin.md).
- **Offline:** local-first cache (SQLite via drift on mobile; IndexedDB on web) with
  conflict-free merging for VR memory constructs.

## 3. Native scalability path

| Stage | Action |
|---|---|
| 1 | Flutter compiles to native (no webview for mobile); Tauri for desktop |
| 2 | Platform channels for hardware access (Bluetooth LE to IPS modules) |
| 3 | Edge compute: heavy sims offloaded to Workers/Queues, never the client |
| 4 | Per-platform release trains (Firebase App Distribution / TestFlight / winget) |
| 5 | Performance budgets: 60 fps Twin-State UI, <100 ms sync latency, offline-first |

## 4. App → platform contract

Every client action maps to a spec artifact (e.g., "send chat message" →
`MessagingRead`/`QueuesWrite`; "upload VR capture" → `WorkersR2StorageWrite` +
`RealtimeAdmin`). Adding a new client capability = add spec entry first, then implement.

## 5. Distribution

- OTA/updates via R2 bucket (`dev-ipp-apps`): APK/EXE/DMG bundles + web assets;
  versioned, signed (`ArtifactsWrite`).
