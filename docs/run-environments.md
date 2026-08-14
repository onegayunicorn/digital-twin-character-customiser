# Run Environments

Three run environments ship with Aether Core: **dev** (local), **docker** (containers), and
**simulation/pipeline** (CLI). See `environments/README.md` for commands.

## Dev environment

| Service | Command | URL |
| :--- | :--- | :--- |
| Web app (Vite dev server) | `npm run dev` | http://localhost:5173 |
| API (Express + tRPC) | `npm run dev -w server` | http://localhost:3001 |
| Tests | `npm test` | — |
| Typecheck | `npm run typecheck` | — |

Workspaces: `npm install` at the root wires all packages (`cores/*`, `engines/*`,
`web-app`, `server`, `shared`, `simulations`, `pipelines`, `tests`).

## Docker environment (`environments/`)

`docker-compose.yml` runs three services:

| Service | Image | Port | Notes |
| :--- | :--- | :--- | :--- |
| web | nginx:1.27 (multi-stage build) | :8080 | Serves SPA, proxies `/api` → api |
| api | node:20-alpine (tsx) | :3001 | Express + tRPC + telemetry ingestion |
| db | mysql:8 | :3306 | Auto-applies `drizzle/migrations` on first boot |

```bash
make docker-build && make docker-up
```

## Environment variables

Copy `.env.example` → `.env`:

```
NODE_ENV=development
PORT=3001
DATABASE_URL=mysql://aether:aether_secret@localhost:3306/aether_core
JWT_SECRET=dev-only-secret-do-not-use-in-production
CORS_ORIGIN=*
```

## CI/CD

- `.github/workflows/ci.yml` — install → typecheck → test → build → simulation & pipeline
  smoke runs, on every push/PR to `main`.
- `.github/workflows/deploy.yml` — Vercel deploy of the web-app (on main), optional Docker
  compose build/push via `workflow_dispatch`.

## Git hooks

`hooks/` installs `pre-commit` (typecheck + tests), `commit-msg` (conventional commits),
`pre-push` (full test suite), `post-merge` (dependency refresh):

```bash
npm run hooks:install
```
