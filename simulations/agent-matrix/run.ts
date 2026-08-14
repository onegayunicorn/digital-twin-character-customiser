/**
 * Simulation: Agent Matrix Evolution.
 *
 * Evolves a population of character agents (18-gene genomes decoded into
 * CharacterAttributes) across generations using the GA engine, then reports
 * the best lineage, fitness trajectory, and archetype distribution.
 * Status: SIMULATED.
 */
import { writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { MatrixEvolutionEngine, dominantBandArchetype } from "@dt-core/agent-matrix";
import { characterGenomeFitness, decodeGenomeToAttributes, GENE_COUNT } from "@dt-engine/evolution";
import { calculateStatModifiers, statPower } from "@dt-engine/lifestyle";

const POPULATION = Number(process.env.SIM_POPULATION ?? 48);
const GENERATIONS = Number(process.env.SIM_GENERATIONS ?? 60);
const seed = Number(process.env.SIM_SEED ?? 2026);

console.log("══════════════════════════════════════════════════════");
console.log(" AGENT MATRIX EVOLUTION SIMULATION");
console.log(" Status: SIMULATED (genetic algorithm, deterministic)");
console.log(` Population: ${POPULATION} · Generations: ${GENERATIONS} · Genes: ${GENE_COUNT} · Seed: ${seed}`);
console.log("══════════════════════════════════════════════════════\n");

const engine = new MatrixEvolutionEngine({
  populationSize: POPULATION,
  generations: GENERATIONS,
  geneCount: GENE_COUNT,
  seed,
  fitness: characterGenomeFitness,
  archetype: dominantBandArchetype,
  onGeneration: (report) => {
    if (report.generation % 10 === 0 || report.generation === 1) {
      console.log(
        `  gen ${String(report.generation).padStart(3)}  best=${report.bestFitness.toFixed(4)}  avg=${report.averageFitness.toFixed(4)}  div=${report.diversity.toFixed(3)}${report.converged ? "  ✓ CONVERGED" : ""}`,
      );
    }
  },
});

const result = engine.run();

// Decode the champion
const champion = decodeGenomeToAttributes(result.best.genome);
const champStats = calculateStatModifiers(champion.lifestyle);

console.log(`\n Converged: ${result.converged ? "yes" : "no"} after ${result.finalGeneration} generations`);
console.log(` Best agent: ${result.best.name} (${result.best.archetype})`);
console.log(` Best fitness: ${result.best.fitness.toFixed(4)}`);
console.log("\n Champion phenotype:");
console.log(`   resemblance=${champion.resemblance.toFixed(2)} skinTone=${champion.skinTone.toFixed(2)}`);
console.log(
  `   nose=[${champion.features.nose.x.toFixed(2)}, ${champion.features.nose.y.toFixed(2)}]  jaw=[${champion.features.jaw.x.toFixed(2)}, ${champion.features.jaw.y.toFixed(2)}]`,
);
console.log(`   lifestyle=${JSON.stringify(champion.lifestyle)}`);
console.log(`   stat power=${statPower(champStats).toFixed(3)}  modifiers=${JSON.stringify(champStats)}`);

// Archetype distribution of the final population
const distribution = new Map<string, number>();
for (const agent of result.agents) {
  const archetype = agent.archetype ?? "Unknown";
  distribution.set(archetype, (distribution.get(archetype) ?? 0) + 1);
}
console.log("\n Final population archetypes:");
for (const [arch, count] of [...distribution.entries()].sort((a, b) => b[1] - a[1])) {
  console.log(`   ${arch.padEnd(10)} ${count}`);
}

// Report
const outDir = join(import.meta.dirname, "output");
mkdirSync(outDir, { recursive: true });
const report = {
  title: "Agent Matrix Evolution Simulation",
  status: "SIMULATED",
  seed,
  populationSize: POPULATION,
  generations: GENERATIONS,
  geneCount: GENE_COUNT,
  converged: result.converged,
  finalGeneration: result.finalGeneration,
  best: {
    id: result.best.id,
    name: result.best.name,
    fitness: result.best.fitness,
    archetype: result.best.archetype,
    lineage: result.best.lineage,
    phenotype: champion,
    statPower: statPower(champStats),
    modifiers: champStats,
  },
  trajectory: result.history.map((h) => ({
    generation: h.generation,
    bestFitness: h.bestFitness,
    averageFitness: h.averageFitness,
    diversity: h.diversity,
  })),
  archetypeDistribution: Object.fromEntries(distribution),
};
const outPath = join(outDir, "agent-matrix-report.json");
writeFileSync(outPath, JSON.stringify(report, null, 2));
console.log(`\n✔ Report written → ${outPath}`);
