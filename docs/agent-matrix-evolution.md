# Agent Matrix Evolution

The **agent matrix** is a population of digital-twin agents whose genomes encode character
phenotypes. A genetic algorithm (GA) evolves the population across generations toward a
fitness objective. **Status: SIMULATED.**

## Genome → phenotype

Each agent carries an 18-gene normalized vector (`cores/agent-matrix`, `GENE_COUNT = 18` in
`engines/evolution`):

| Genes | Maps to |
| :--- | :--- |
| 0–1 | `resemblance`, `skinTone` (0..1) |
| 2–13 | dual-axis feature vectors: brows, eyes, nose, jaw, cheekbones, chinProfile (each x/y in -1..1) |
| 14–17 | lifestyle hours: sleeping, friends, sports, illegalWork (2..8h, renormalised to 24h) |

`decodeGenomeToAttributes(genome)` → `CharacterAttributes`; `encodeAttributesToGenome`
round-trips phenotypes back into gene space.

## Fitness

`characterGenomeFitness(genome)` = `characterFitness(attributes)`:

```
fitness = 0.7 × statPower(calculateStatModifiers(lifestyle))
        + 0.3 × lifestyleBalanceBonus
```

- `statPower` sums the seven stat modifiers (stamina, strength, stealth, shooting, driving,
  lung capacity, flying) produced by the lifestyle engine.
- The balance bonus rewards even hour distribution (spread over 24h, scaled to 0..1).

## Operators

| Operator | Implementation | Default |
| :--- | :--- | :--- |
| Selection | Tournament (k random candidates → best) | k = 3 |
| Crossover | Uniform blend (per-gene pick or 0.25–0.75 blend) | rate 0.8 |
| Mutation | Gaussian perturbation, clamped to [0,1] | rate 0.05, σ 0.12 |
| Elitism | Top-N carried unchanged into next generation | N = 2 |
| Initialisation | Seeded uniform random (`mulberry32`) | seed 2026 |

## Convergence

A run stops early when best fitness improvement is ≤ 1e-9 for 2 consecutive generations.
Each generation emits a `GenerationReport`: best agent, average fitness, population
diversity (stddev of genes), best fitness, delta.

## Archetypes

`dominantBandArchetype(genome)` labels agents by mean gene value:
`Stealth` (< 0.33) · `Balanced` (0.33–0.66) · `Combat` (> 0.66).

## Where it runs

- **Simulation:** `npm run sim:agent-matrix` — evolves 48 agents × 60 generations, prints the
  trajectory and champion phenotype, writes `simulations/agent-matrix/output/agent-matrix-report.json`.
- **In-browser:** the Operations Dashboard (`/dashboard`) runs the engine via
  `useAgentMatrix` and renders the fitness trajectory + champion stats.
- **Server:** `characters.evolve` tRPC procedure exposes evolution as an API query.
