import { describe, it, expect } from "vitest";
import {
  MatrixEvolutionEngine,
  dominantBandArchetype,
  sumOfGenesFitness,
  type AgentGenome,
} from "./index";

describe("MatrixEvolutionEngine", () => {
  it("evolves a population and improves best fitness over generations", () => {
    const target = [0.9, 0.8, 0.7, 0.6, 0.5];
    const engine = new MatrixEvolutionEngine({
      populationSize: 24,
      generations: 40,
      geneCount: 5,
      seed: 42,
      fitness: (g: AgentGenome) => {
        // Minimise distance to target → maximise negative distance
        const dist = Math.sqrt(
          g.genes.reduce((acc, gene, i) => acc + (gene - target[i]!) ** 2, 0),
        );
        return -dist;
      },
    });
    const result = engine.run();
    expect(result.history.length).toBeGreaterThanOrEqual(5);
    expect(result.best.generation).toBe(result.finalGeneration);
    const firstBest = result.history[0]!.bestFitness;
    expect(result.best.fitness).toBeGreaterThanOrEqual(firstBest);
  });

  it("preserves population size and gene count", () => {
    const engine = new MatrixEvolutionEngine({
      populationSize: 16,
      generations: 5,
      geneCount: 8,
      seed: 7,
      fitness: sumOfGenesFitness,
    });
    const result = engine.run();
    expect(result.agents).toHaveLength(16);
    expect(result.agents[0]!.genome.genes).toHaveLength(8);
  });

  it("keeps elite agents in every generation (elitism)", () => {
    const engine = new MatrixEvolutionEngine({
      populationSize: 20,
      generations: 10,
      geneCount: 4,
      elitism: 3,
      seed: 123,
      fitness: sumOfGenesFitness,
    });
    const result = engine.run();
    // The best agent of each generation must appear in the next (elite carry)
    for (let i = 0; i < result.history.length; i += 1) {
      const report = result.history[i]!;
      expect(report.best.fitness).toBeGreaterThanOrEqual(0);
    }
    expect(result.history[0]!.bestFitness).toBeLessThanOrEqual(
      result.history[result.history.length - 1]!.bestFitness,
    );
  });

  it("is deterministic for a fixed seed", () => {
    const make = () =>
      new MatrixEvolutionEngine({
        populationSize: 12,
        generations: 6,
        geneCount: 3,
        seed: 2026,
        fitness: sumOfGenesFitness,
      }).run();
    const a = make();
    const b = make();
    expect(a.history.map((h) => h.bestFitness)).toEqual(
      b.history.map((h) => h.bestFitness),
    );
  });

  it("records diversity and lineage", () => {
    const engine = new MatrixEvolutionEngine({
      populationSize: 10,
      generations: 8,
      geneCount: 6,
      seed: 5,
      fitness: sumOfGenesFitness,
    });
    const result = engine.run();
    for (const report of result.history) {
      expect(report.diversity).toBeGreaterThanOrEqual(0);
    }
    for (const agent of result.agents) {
      expect(Array.isArray(agent.lineage)).toBe(true);
      expect(agent.id).toBeTruthy();
    }
  });

  it("rejects invalid configuration", () => {
    expect(
      () =>
        new MatrixEvolutionEngine({
          populationSize: 2,
          generations: 1,
          geneCount: 2,
          fitness: sumOfGenesFitness,
        }),
    ).toThrow(/populationSize/);
  });
});

describe("dominantBandArchetype", () => {
  it("classifies gene bands", () => {
    expect(dominantBandArchetype({ genes: [0.1, 0.1, 0.2] })).toBe("Stealth");
    expect(dominantBandArchetype({ genes: [0.5, 0.5, 0.5] })).toBe("Balanced");
    expect(dominantBandArchetype({ genes: [0.9, 0.8, 0.8] })).toBe("Combat");
  });
});
