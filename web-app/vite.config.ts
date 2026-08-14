import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import { fileURLToPath } from "node:url";

const alias = {
  "@": fileURLToPath(new URL("./src", import.meta.url)),
  "@dt-core/types": fileURLToPath(new URL("../cores/types/src/index.ts", import.meta.url)),
  "@dt-core/state": fileURLToPath(new URL("../cores/state/src/index.ts", import.meta.url)),
  "@dt-core/ai-router": fileURLToPath(new URL("../cores/ai-router/src/index.ts", import.meta.url)),
  "@dt-core/simulation": fileURLToPath(new URL("../cores/simulation/src/index.ts", import.meta.url)),
  "@dt-core/agent-matrix": fileURLToPath(new URL("../cores/agent-matrix/src/index.ts", import.meta.url)),
  "@dt-engine/lifestyle": fileURLToPath(new URL("../engines/lifestyle/src/index.ts", import.meta.url)),
  "@dt-engine/feature-grid": fileURLToPath(new URL("../engines/feature-grid/src/index.ts", import.meta.url)),
  "@dt-engine/gltf-registry": fileURLToPath(new URL("../engines/gltf-registry/src/index.ts", import.meta.url)),
  "@dt-engine/mesh-pipeline": fileURLToPath(new URL("../engines/mesh-pipeline/src/index.ts", import.meta.url)),
  "@dt-engine/telemetry": fileURLToPath(new URL("../engines/telemetry/src/index.ts", import.meta.url)),
  "@dt-engine/evolution": fileURLToPath(new URL("../engines/evolution/src/index.ts", import.meta.url)),
};

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: { alias },
  server: {
    port: 5173,
    host: true,
  },
  build: {
    outDir: "dist",
    sourcemap: false,
  },
});
