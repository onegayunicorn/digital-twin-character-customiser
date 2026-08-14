import { describe, it, expect } from "vitest";
import { createVanillaCustomizerStore } from "@dt-core/state";
import { parseAIPrompt } from "@dt-core/ai-router";
import { validateLifestyleBudget, calculateStatModifiers, statPower } from "@dt-engine/lifestyle";
import { simulateLifestyleLifecycle } from "@dt-core/simulation";
import { MatrixEvolutionEngine } from "@dt-core/agent-matrix";
import { characterGenomeFitness, decodeGenomeToAttributes } from "@dt-engine/evolution";
import { createTelemetryEngine, averageCoherence } from "@dt-engine/telemetry";
import { blendFeatureMatrix, pixelToGrid } from "@dt-engine/feature-grid";
import { gltfRegistry } from "@dt-engine/gltf-registry";
import { applyMorphTargets, HERITAGE_FRAGMENT_SHADER } from "@dt-engine/mesh-pipeline";
import { createDefaultAttributes } from "@dt-core/types";

/**
 * Cross-package smoke — one test per package proves the whole monorepo
 * interconnects (imports resolve, engines interoperate).
 */
describe("cross-package integration", () => {
  it("state + ai-router + lifestyle work end to end", () => {
    const store = createVanillaCustomizerStore();
    const { mutator } = parseAIPrompt("criminal heist with square jaw");
    store.getState().updateAttributes(mutator);
    const attrs = store.getState().activeCharacter;
    expect(validateLifestyleBudget(attrs.lifestyle).valid).toBe(true);
    expect(attrs.features.jaw.x).toBe(0.9);
    expect(calculateStatModifiers(attrs.lifestyle).stealth).toBeGreaterThan(0.6);
  });

  it("simulation + lifestyle lifecycle keep budgets valid", () => {
    const result = simulateLifestyleLifecycle(createDefaultAttributes(), {
      days: 10,
      seed: 1,
      statModifier: (l) => calculateStatModifiers(l),
    });
    for (const day of result.days) {
      const sum = Object.values(day.lifestyle).reduce((a, b) => a + b, 0);
      expect(sum).toBeCloseTo(24, 5);
    }
  });

  it("agent-matrix + evolution produce a legal champion", () => {
    const engine = new MatrixEvolutionEngine({
      populationSize: 16,
      generations: 12,
      geneCount: 18,
      seed: 3,
      fitness: characterGenomeFitness,
    });
    const result = engine.run();
    const attrs = decodeGenomeToAttributes(result.best.genome);
    expect(validateLifestyleBudget(attrs.lifestyle).valid).toBe(true);
    expect(result.best.fitness).toBeGreaterThan(0);
  });

  it("telemetry + simulation oscillators stay bounded", () => {
    const engine = createTelemetryEngine({ seed: 7 });
    engine.run(50);
    expect(averageCoherence(engine)).toBeGreaterThanOrEqual(0);
    expect(averageCoherence(engine)).toBeLessThanOrEqual(1);
  });

  it("feature-grid + mesh-pipeline + gltf-registry interoperate", () => {
    const mother = createDefaultAttributes().features;
    const father = createDefaultAttributes().features;
    father.nose.x = 0.8;
    const blended = blendFeatureMatrix(mother, father, 0.5);
    const map = applyMorphTargets({ ...blended, jaw: blended.jaw, chinShape: blended.chinShape });
    expect(map.Nose_Wide).toBeCloseTo(0.4, 5);
    expect(gltfRegistry.resolvePath("standing")).toContain("wo-standing-v17");
    expect(HERITAGE_FRAGMENT_SHADER).toContain("tMotherSkin");
    expect(pixelToGrid(100, 100, 200, 200)).toEqual({ x: 0, y: 0 });
  });

  it("stat power orders a known strong profile above default", () => {
    const attrs = createDefaultAttributes();
    const strong = createDefaultAttributes();
    strong.lifestyle.sports = 8;
    strong.lifestyle.illegalWork = 8;
    strong.lifestyle.sleeping = 4;
    strong.lifestyle.friends = 2;
    strong.lifestyle.legalWork = 2;
    expect(statPower(calculateStatModifiers(strong.lifestyle))).toBeGreaterThan(
      statPower(calculateStatModifiers(attrs.lifestyle)),
    );
  });
});
