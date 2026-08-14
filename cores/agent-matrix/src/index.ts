/**
 * Aether Core — Agent Matrix Evolution Engine.
 *
 * A genetic algorithm that evolves a population ("matrix") of agents across
 * generations. Each agent carries a normalized gene vector; fitness is user
 * supplied; selection is tournament-based with elitism, crossover is uniform
 * blend, mutation is gaussian. Emits a generation report per round and tracks
 * convergence so simulations can stop early.
 */
import { mulberry32, gaussian, type Rng } from "@dt-core/simulation";

export interface AgentGenome {
  /** Normalized genes in [0, 1]. */
  genes: number[];
}

export interface AgentMatrixAgent {
  id: string;
  name: string;
  genome: AgentGenome;
  fitness: number;
  generation: number;
  /** Parent ids of this agent (lineage tracking for the matrix). */
  lineage: string[];
  /** Optional archetype label derived from the genome. */
  archetype?: string;
}

export interface GenerationReport {
  generation: number;
  best: AgentMatrixAgent;
  averageFitness: number;
  /** Standard deviation of gene values across the population (diversity). */
  diversity: number;
  converged: boolean;
  bestFitness: number;
  bestFitnessDelta: number;
}

export interface MatrixEvolutionOptions {
  populationSize: number;
  generations: number;
  geneCount: number;
  fitness: (genome: AgentGenome, index?: number) => number;
  mutationRate?: number; // per-gene probability, default 0.05
  mutationScale?: number; // gaussian sigma, default 0.12
  crossoverRate?: number; // probability two parents blend, default 0.8
  elitism?: number; // count of top agents carried over unchanged, default 2
  tournamentSize?: number; // default 3
  seed?: number;
  archetype?: (genome: AgentGenome) => string;
  onGeneration?: (report: GenerationReport) => void;
}

export interface MatrixEvolutionResult {
  agents: AgentMatrixAgent[];
  history: GenerationReport[];
  best: AgentMatrixAgent;
  converged: boolean;
  finalGeneration: number;
}

const clamp01 = (v: number) => Math.min(1, Math.max(0, v));

function makeAgent(
  genome: AgentGenome,
  generation: number,
  lineage: string[],
  fitness: (g: AgentGenome, i?: number) => number,
  archetype?: (g: AgentGenome) => string,
  index = 0,
): AgentMatrixAgent {
  return {
    id: `${generation}-${index}-${Math.random().toString(36).slice(2, 8)}`,
    name: `Agent_${String(generation).padStart(2, "0")}_${String(index).padStart(2, "0")}`,
    genome,
    fitness: fitness(genome, index),
    generation,
    lineage,
    archetype: archetype ? archetype(genome) : undefined,
  };
}

function randomGenome(geneCount: number, rng: Rng): AgentGenome {
  return { genes: Array.from({ length: geneCount }, () => rng()) };
}

function tournamentSelect(
  population: AgentMatrixAgent[],
  tournamentSize: number,
  rng: Rng,
): AgentMatrixAgent {
  let best: AgentMatrixAgent | null = null;
  for (let i = 0; i < tournamentSize; i += 1) {
    const candidate = population[Math.floor(rng() * population.length)];
    if (!candidate) continue;
    if (!best || candidate.fitness > best.fitness) best = candidate;
  }
  return best ?? population[0]!;
}

/** Uniform blend crossover: each gene randomly inherited or blended. */
function crossover(
  a: AgentGenome,
  b: AgentGenome,
  rate: number,
  rng: Rng,
): AgentGenome {
  if (rng() > rate) return { genes: [...a.genes] };
  const blend = 0.5 + (rng() - 0.5) * 0.5; // 0.25..0.75
  return {
    genes: a.genes.map((g, i) => {
      const other = b.genes[i] ?? g;
      return rng() < 0.5 ? g : g * (1 - blend) + other * blend;
    }),
  };
}

/** Gaussian mutation with clamp. */
function mutate(g: AgentGenome, rate: number, scale: number, rng: Rng): AgentGenome {
  return {
    genes: g.genes.map((gene) =>
      rng() < rate ? clamp01(gene + gaussian(rng) * scale) : gene,
    ),
  };
}

/** Population diversity: mean pairwise gene stddev across agents. */
function diversityOf(population: AgentMatrixAgent[], geneCount: number): number {
  const means = Array.from({ length: geneCount }, (_, i) => {
    let sum = 0;
    for (const a of population) sum += a.genome.genes[i] ?? 0;
    return sum / population.length;
  });
  let variance = 0;
  for (const a of population) {
    for (let i = 0; i < geneCount; i += 1) {
      variance += ((a.genome.genes[i] ?? 0) - means[i]!) ** 2;
    }
  }
  return Math.sqrt(variance / (population.length * geneCount));
}

export class MatrixEvolutionEngine {
  private readonly opts: MatrixEvolutionOptions;
  private readonly rng: Rng;

  constructor(opts: MatrixEvolutionOptions) {
    if (opts.populationSize < 4) throw new Error("populationSize must be >= 4");
    if (opts.generations < 1) throw new Error("generations must be >= 1");
    if (opts.geneCount < 1) throw new Error("geneCount must be >= 1");
    this.opts = {
      mutationRate: 0.05,
      mutationScale: 0.12,
      crossoverRate: 0.8,
      elitism: 2,
      tournamentSize: 3,
      seed: 1,
      ...opts,
    };
    this.rng = mulberry32(this.opts.seed ?? 1);
  }

  run(): MatrixEvolutionResult {
    const {
      populationSize,
      generations,
      geneCount,
      fitness,
      mutationRate = 0.05,
      mutationScale = 0.12,
      crossoverRate = 0.8,
      elitism = 2,
      tournamentSize = 3,
      archetype,
      onGeneration,
    } = this.opts;

    let population: AgentMatrixAgent[] = Array.from(
      { length: populationSize },
      (_, i) =>
        makeAgent(randomGenome(geneCount, this.rng), 0, [], fitness, archetype, i),
    ).sort((a, b) => b.fitness - a.fitness);

    const history: GenerationReport[] = [];
    let previousBest = population[0]?.fitness ?? 0;
    let converged = false;
    let finalGeneration = 0;

    for (let gen = 1; gen <= generations; gen += 1) {
      const next: AgentMatrixAgent[] = [];

      // Elitism: carry the best unchanged (preserves monotone improvement)
      for (let e = 0; e < Math.min(elitism, populationSize); e += 1) {
        const elite = population[e];
        if (elite) next.push({ ...elite, generation: gen });
      }

      // Breed until the population is refilled
      while (next.length < populationSize) {
        const parentA = tournamentSelect(population, tournamentSize, this.rng);
        const parentB = tournamentSelect(population, tournamentSize, this.rng);
        let child = crossover(parentA.genome, parentB.genome, crossoverRate, this.rng);
        child = mutate(child, mutationRate, mutationScale, this.rng);
        const idx = next.length;
        next.push(
          makeAgent(
            child,
            gen,
            [parentA.id, parentB.id],
            fitness,
            archetype,
            idx,
          ),
        );
      }

      population = next
        .sort((a, b) => b.fitness - a.fitness)
        .slice(0, populationSize);

      const best = population[0]!;
      const averageFitness =
        population.reduce((acc, a) => acc + a.fitness, 0) / population.length;
      const diversity = diversityOf(population, geneCount);
      const bestFitnessDelta = best.fitness - previousBest;
      converged = gen > 3 && bestFitnessDelta <= 1e-9 && history[history.length - 1]?.bestFitnessDelta! <= 1e-9;

      const report: GenerationReport = {
        generation: gen,
        best,
        averageFitness,
        diversity,
        converged,
        bestFitness: best.fitness,
        bestFitnessDelta,
      };
      history.push(report);
      onGeneration?.(report);
      previousBest = best.fitness;
      finalGeneration = gen;

      if (converged) break;
    }

    const best = population[0]!;
    return { agents: population, history, best, converged, finalGeneration };
  }
}

/** Label an agent by its dominant gene cluster (3 archetype bands). */
export function dominantBandArchetype(g: AgentGenome): string {
  const sum = g.genes.reduce((a, b) => a + b, 0);
  const mean = sum / g.genes.length;
  if (mean < 0.33) return "Stealth";
  if (mean < 0.66) return "Balanced";
  return "Combat";
}

/** Built-in fitness: higher gene values score higher (useful for demos). */
export function sumOfGenesFitness(g: AgentGenome): number {
  return g.genes.reduce((a, b) => a + b, 0) / g.genes.length;
}
