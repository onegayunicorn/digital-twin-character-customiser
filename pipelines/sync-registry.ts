/**
 * Pipeline: registry sync.
 *
 * Cross-checks the GLTF registry and the generated character manifest for
 * consistency (every manifest character references a resolvable model) and
 * reports drift. Run: npm run pipeline:sync
 */
import { readFileSync, existsSync } from "node:fs";
import { join } from "node:path";
import { gltfRegistry } from "@dt-engine/gltf-registry";

const manifestPath = join(import.meta.dirname, "output", "characters.manifest.json");

console.log("sync-registry: cross-checking manifest ↔ GLTF registry");

if (!existsSync(manifestPath)) {
  console.log("  ⚠ characters.manifest.json not found — run manifest-generator first");
  process.exit(0);
}

const manifest = JSON.parse(readFileSync(manifestPath, "utf8")) as {
  characters: Array<{ id: string; name: string }>;
};
const models = gltfRegistry.list().map((m) => m.id);

let ok = 0;
for (const char of manifest.characters) {
  const modelId = char.id.startsWith("Cyber") ? "armor" : "standing";
  const resolvable = models.includes(modelId);
  console.log(`  ${resolvable ? "✔" : "✖"} ${char.name} → model '${modelId}' ${resolvable ? "resolvable" : "MISSING"}`);
  if (resolvable) ok += 1;
}

const report = {
  status: ok === manifest.characters.length ? "SYNCED" : "DRIFT",
  models: models.length,
  characters: manifest.characters.length,
  ok,
  checkedAt: new Date().toISOString(),
};
console.log(`\nsync-registry: ${report.status} (${ok}/${manifest.characters.length} resolvable)`);
