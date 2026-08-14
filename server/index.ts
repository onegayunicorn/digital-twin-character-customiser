/**
 * Server — Express bootstrap.
 *
 * Mounts the tRPC HTTP handler plus telemetry ingestion (Schumann stream
 * written into storage so /api/telemetry has live data).
 */
import express from "express";
import { createExpressMiddleware } from "@trpc/server/adapters/express";
import { loadEnv } from "./_core/env";
import { createMemoryStorage } from "./_core/storage";
import { createContext } from "./_core/trpc";
import { appRouter } from "./routers";
import { createTelemetryEngine } from "@dt-engine/telemetry";
import { DEFAULT_TELEMETRY_SEED } from "@dt/shared";
import { pushTelemetry } from "./db";

const env = loadEnv();
const storage = createMemoryStorage();
const app = express();

app.use(express.json());

app.use(
  "/api/trpc",
  createExpressMiddleware({
    router: appRouter,
    createContext: ({ req }) => {
      const auth = req.headers.authorization;
      const token = auth?.startsWith("Bearer ") ? auth.slice(7) : null;
      return createContext(storage, token);
    },
  }),
);

app.get("/api/health", (_req, res) => {
  res.json({ ok: true, app: "aether-core", version: "4.1.0" });
});

// Telemetry ingestion: deterministic Schumann stream into storage
const telemetryEngine = createTelemetryEngine({ seed: DEFAULT_TELEMETRY_SEED, dt: 1 });
setInterval(() => {
  const s = telemetryEngine.step();
  pushTelemetry(storage, { t: s.t, schumann: s.schumann, coherence: s.coherence });
}, 1000);

if (env.NODE_ENV !== "test") {
  app.listen(env.PORT, () => {
    console.log(`[aether-core] API listening on :${env.PORT} (${env.NODE_ENV})`);
  });
}

export { app, storage, env };
