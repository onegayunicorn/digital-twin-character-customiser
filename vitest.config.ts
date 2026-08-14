import { defineConfig } from "vitest/config";
import { fileURLToPath } from "node:url";

const here = (p: string) => fileURLToPath(new URL(p, import.meta.url));

const alias = {
  "@": here("./web-app/src"),
  "@dt-core/types": here("./cores/types/src/index.ts"),
  "@dt-core/state": here("./cores/state/src/index.ts"),
  "@dt-core/ai-router": here("./cores/ai-router/src/index.ts"),
  "@dt-core/simulation": here("./cores/simulation/src/index.ts"),
  "@dt-core/agent-matrix": here("./cores/agent-matrix/src/index.ts"),
  "@dt-engine/lifestyle": here("./engines/lifestyle/src/index.ts"),
  "@dt-engine/feature-grid": here("./engines/feature-grid/src/index.ts"),
  "@dt-engine/gltf-registry": here("./engines/gltf-registry/src/index.ts"),
  "@dt-engine/mesh-pipeline": here("./engines/mesh-pipeline/src/index.ts"),
  "@dt-engine/telemetry": here("./engines/telemetry/src/index.ts"),
  "@dt-engine/evolution": here("./engines/evolution/src/index.ts"),
  "@dt/shared": here("./shared/src/index.ts"),
};

export default defineConfig({
  resolve: { alias },
  test: {
    globals: true,
    environment: "node",
    include: [
      "cores/**/*.test.ts",
      "engines/**/*.test.ts",
      "web-app/src/**/*.test.ts",
      "server/**/*.test.ts",
      "tests/**/*.test.ts",
    ],
    coverage: {
      provider: "v8",
      reporter: ["text", "html"],
    },
  },
});
