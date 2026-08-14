/**
 * Pipeline: character manifest codegen.
 *
 * Generates a deployment manifest (characters.manifest.json) from a seed set
 * of characters — the artifact consumed by the saved-characters "Instantiate"
 * hot-deploy flow. Run: npm run pipeline:manifest
 */
import { writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import {
  createDefaultAttributes,
  cloneAttributes,
  type CharacterProfile,
} from "@dt-core/types";

function makeProfile(
  id: string,
  name: string,
  gender: "Male" | "Female",
  mutate: (attrs: ReturnType<typeof createDefaultAttributes>) => void,
): CharacterProfile {
  const attributes = cloneAttributes(createDefaultAttributes());
  mutate(attributes);
  return {
    id,
    name,
    gender,
    attributes,
    created: new Date().toISOString().split("T")[0] ?? "",
  };
}

const MANIFEST_VERSION = "4.1.0";

const characters: CharacterProfile[] = [
  makeProfile("Twin_Alpha_01", "Twin_Alpha_01", "Male", (a) => {
    a.resemblance = 0.85;
    a.features.jaw.x = 0.9;
    a.features.jaw.y = 0.8;
    a.lifestyle.illegalWork = 8;
    a.lifestyle.sleeping = 5;
  }),
  makeProfile("Cyber_Model_V2", "Cyber_Model_V2", "Female", (a) => {
    a.skinTone = 0.4;
    a.appearance.hairColor = 3;
    a.features.nose.x = -0.6;
    a.lifestyle.legalWork = 8;
    a.lifestyle.sports = 4;
  }),
  makeProfile("Noir_Specter", "Noir_Specter", "Female", (a) => {
    a.resemblance = 0.3;
    a.features.cheekbones.y = 0.8;
    a.features.lips = -0.4;
    a.lifestyle.friends = 8;
  }),
];

const outDir = join(import.meta.dirname, "output");
mkdirSync(outDir, { recursive: true });
const outPath = join(outDir, "characters.manifest.json");
writeFileSync(
  outPath,
  JSON.stringify(
    { manifestVersion: MANIFEST_VERSION, generatedAt: new Date().toISOString(), characters },
    null,
    2,
  ),
);

console.log(`manifest-generator: generated ${characters.length} character manifests`);
for (const c of characters) {
  console.log(`  - ${c.name} (${c.gender}) resemblance=${c.attributes.resemblance.toFixed(2)}`);
}
console.log(`✔ manifest → ${outPath}`);
