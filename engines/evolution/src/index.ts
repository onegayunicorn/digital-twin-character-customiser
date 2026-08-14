/**
 * Aether Core engine — Evolution.
 *
 * Bridges the Agent Matrix GA engine to the character domain:
 *   - decodes a normalized gene vector into a CharacterAttributes phenotype
 *   - evaluates character fitness from lifestyle stat modifiers
 *   - provides convenience helpers to evolve a character population
 *
 * SIMULATED: fitness values are model-internal scores, not verified biology.
 */
import {
  createDefaultAttributes,
  cloneAttributes,
  type CharacterAttributes,
} from "@dt-core/types";
import type { AgentGenome } from "@dt-core/agent-matrix";
import { calculateStatModifiers, statPower, rebalanceLifestyle } from "@dt-engine/lifestyle";

export const GENE_COUNT = 18;

/** Gene → phenotype mapping table (index → attribute path). */
const GENE_MAP: Array<{
  path: "resemblance" | "skinTone" | keyof CharacterAttributes["features"] | "lifestyle";
  axis?: "x" | "y";
  key?: "sleeping" | "friends" | "sports" | "legalWork" | "illegalWork";
}> = [
  { path: "resemblance" },
  { path: "skinTone" },
  { path: "brows", axis: "x" },
  { path: "brows", axis: "y" },
  { path: "eyes", axis: "x" },
  { path: "eyes", axis: "y" },
  { path: "nose", axis: "x" },
  { path: "nose", axis: "y" },
  { path: "jaw", axis: "x" },
  { path: "jaw", axis: "y" },
  { path: "cheekbones", axis: "x" },
  { path: "cheekbones", axis: "y" },
  { path: "chinProfile", axis: "x" },
  { path: "chinProfile", axis: "y" },
  { path: "lifestyle", key: "sleeping" },
  { path: "lifestyle", key: "friends" },
  { path: "lifestyle", key: "sports" },
  { path: "lifestyle", key: "illegalWork" },
];

const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const feature = (v: number) => clamp01(v) * 2 - 1; // [0,1] → [-1,1]

/** Decode a gene vector into a full CharacterAttributes phenotype. */
export function decodeGenomeToAttributes(genome: AgentGenome): CharacterAttributes {
  const attrs = createDefaultAttributes();
  const genes = genome.genes;

  GENE_MAP.forEach((slot, i) => {
    const gene = genes[i] ?? 0.5;
    if (slot.path === "resemblance") {
      attrs.resemblance = clamp01(gene);
      return;
    }
    if (slot.path === "skinTone") {
      attrs.skinTone = clamp01(gene);
      return;
    }
    if (slot.path === "lifestyle" && slot.key) {
      attrs.lifestyle[slot.key] = 2 + clamp01(gene) * 6; // 2..8h
      return;
    }
    if (slot.path !== "lifestyle") {
      const vec = attrs.features[slot.path] as unknown as { x: number; y: number };
      if (slot.axis === "x") vec.x = feature(gene);
      else vec.y = feature(gene);
    }
  });

  // Rebalance the lifestyle to exactly 24h with all hard rules satisfied
  attrs.lifestyle = rebalanceLifestyle(attrs.lifestyle);
  return attrs;
}

/** Fitness of a decoded character: normalized stat power + lifestyle balance. */
export function characterFitness(attributes: CharacterAttributes): number {
  const stats = calculateStatModifiers(attributes.lifestyle);
  const power = statPower(stats) / 7; // normalize 7 stats × 1.0 → 0..1
  // Balance bonus: closer to even spread wins slightly
  const b = attributes.lifestyle;
  const spread = Math.max(
    b.sleeping,
    b.friends,
    b.sports,
    b.legalWork,
    b.illegalWork,
  ) - Math.min(
    b.sleeping,
    b.friends,
    b.sports,
    b.legalWork,
    b.illegalWork,
  );
  const balance = 1 - spread / 10;
  return clamp01(power * 0.7 + balance * 0.3);
}

/** Fitness function for the GA engine (decodes then scores). */
export function characterGenomeFitness(genome: AgentGenome): number {
  return characterFitness(decodeGenomeToAttributes(genome));
}

/** Decode + score + attach archetype in one pass for reporting. */
export function evaluateGenome(genome: AgentGenome): {
  attributes: CharacterAttributes;
  fitness: number;
  stats: ReturnType<typeof calculateStatModifiers>;
} {
  const attributes = decodeGenomeToAttributes(genome);
  const stats = calculateStatModifiers(attributes.lifestyle);
  return { attributes, stats, fitness: characterFitness(attributes) };
}

/** Re-encode a character back into a gene vector (for visualization). */
export function encodeAttributesToGenome(attributes: CharacterAttributes): AgentGenome {
  const toUnit = (v: number) => clamp01((v + 1) / 2);
  const genes: number[] = [];
  genes.push(attributes.resemblance, attributes.skinTone);
  genes.push(toUnit(attributes.features.brows.x), toUnit(attributes.features.brows.y));
  genes.push(toUnit(attributes.features.eyes.x), toUnit(attributes.features.eyes.y));
  genes.push(toUnit(attributes.features.nose.x), toUnit(attributes.features.nose.y));
  genes.push(toUnit(attributes.features.jaw.x), toUnit(attributes.features.jaw.y));
  genes.push(
    toUnit(attributes.features.cheekbones.x),
    toUnit(attributes.features.cheekbones.y),
  );
  genes.push(
    toUnit(attributes.features.chinProfile.x),
    toUnit(attributes.features.chinProfile.y),
  );
  genes.push(
    clamp01((attributes.lifestyle.sleeping - 2) / 6),
    clamp01((attributes.lifestyle.friends - 2) / 6),
    clamp01((attributes.lifestyle.sports - 2) / 6),
    clamp01((attributes.lifestyle.illegalWork - 2) / 6),
  );
  while (genes.length < GENE_COUNT) genes.push(0.5);
  return { genes: genes.slice(0, GENE_COUNT) };
}

/** Produce a fresh random character genome (seeded). */
export function randomCharacterGenome(rng: () => number): AgentGenome {
  return { genes: Array.from({ length: GENE_COUNT }, () => rng()) };
}

export { cloneAttributes };
