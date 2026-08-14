# Run Environments

Aether Core ships three run environments:

| Environment | What it runs | How |
| :--- | :--- | :--- |
| **Dev** | Vite dev server (`:5173`) + API (`:3001`) | `npm run dev` / `npm run dev -w server` |
| **Docker** | nginx static SPA (`:8080`) + API (`:3001`) + MySQL 8 (`:3306`) | `make docker-up` |
| **Simulation** | 4 CLI simulations + data pipelines | `npm run sim:all` / `npm run pipeline` |

## Quick start (dev)

```bash
npm install
npm run dev            # web-app at http://localhost:5173
```

## Docker

```bash
make docker-build      # build web + api images
make docker-up         # web :8080 · api :3001 · mysql :3306 (migrations auto-apply)
make docker-down
```

The `db` service mounts `drizzle/migrations` into `/docker-entrypoint-initdb.d`
so the schema (`0000_initial.sql`) applies on first boot.

## Env vars

Copy `environments/.env.example` → `.env` and set `DATABASE_URL`, `JWT_SECRET`,
`CORS_ORIGIN` before production deploys.

## Make targets

```bash
make help              # list all targets
make dev / build / test / typecheck
make sim / sim-quantum
make pipeline
make hooks
```
