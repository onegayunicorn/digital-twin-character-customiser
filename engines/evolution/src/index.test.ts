import { describe, it, expect } from "vitest";
import {
  decodeGenomeToAttributes,
  encodeAttributesToGenome,
  characterFitness,
  characterGenomeFitness,
  GENE_COUNT,
} from "./index";
import {
  validateLifestyleBudget,
} from "@dt-engine/lifestyle";
import { createDefaultAttributes } from "@dt-core/types";

describe("genome → phenotype decoding", () => {
  it("produces a valid character with a 24h budget", () => {
    const genome = { genes: Array.from({ length: GENE_COUNT }, () => 0.5) };
    const attrs = decodeGenomeToAttributes(genome);
    expect(validateLifestyleBudget(attrs.lifestyle).valid).toBe(true);
    expect(attrs.features.nose.x).toBeCloseTo(0, 5);
    expect(attrs.resemblance).toBe(0.5);
  });

  it("extreme genes map to extreme features", () => {
    const genome = { genes: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0] };
    const attrs = decodeGenomeToAttributes(genome);
    expect(attrs.resemblance).toBe(0);
    expect(attrs.skinTone).toBe(1);
    expect(attrs.features.brows.x).toBe(-1);
    expect(attrs.features.brows.y).toBe(1);
  });

  it("round-trips through encode/decode", () => {
    const attrs = createDefaultAttributes();
    attrs.features.nose.x = 0.7;
    attrs.resemblance = 0.9;
    const genome = encodeAttributesToGenome(attrs);
    const back = decodeGenomeToAttributes(genome);
    expect(back.features.nose.x).toBeCloseTo(0.7, 5);
    expect(back.resemblance).toBeCloseTo(0.9, 5);
  });
});

describe("fitness", () => {
  it("characterFitness is bounded and monotone in stat power", () => {
    const weak = createDefaultAttributes();
    weak.lifestyle.sports = 2;
    weak.lifestyle.illegalWork = 2;
    weak.lifestyle.sleeping = 8;
    weak.lifestyle.friends = 6;
    weak.lifestyle.legalWork = 6;
    const strong = createDefaultAttributes();
    strong.lifestyle.sports = 8;
    strong.lifestyle.illegalWork = 8;
    strong.lifestyle.sleeping = 4;
    strong.lifestyle.friends = 2;
    strong.lifestyle.legalWork = 2;
    const fWeak = characterFitness(weak);
    const fStrong = characterFitness(strong);
    expect(fWeak).toBeGreaterThanOrEqual(0);
    expect(fWeak).toBeLessThanOrEqual(1.5);
    expect(fStrong).toBeGreaterThan(fWeak);
  });

  it("characterGenomeFitness is deterministic for the same genome", () => {
    const genome = { genes: Array.from({ length: GENE_COUNT }, (_, i) => (i % 5) / 5) };
    expect(characterGenomeFitness(genome)).toBe(characterGenomeFitness(genome));
  });
});
