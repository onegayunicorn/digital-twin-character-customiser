import { useMemo, useState } from "react";
import {
  MatrixEvolutionEngine,
  type GenerationReport,
  type MatrixEvolutionResult,
} from "@dt-core/agent-matrix";
import { characterGenomeFitness, GENE_COUNT } from "@dt-engine/evolution";

export interface UseAgentMatrixOptions {
  populationSize?: number;
  generations?: number;
  seed?: number;
}

/**
 * useAgentMatrix — runs the agent matrix evolution (GA) in the browser and
 * exposes generation history for the operations dashboard.
 */
export function useAgentMatrix(opts: UseAgentMatrixOptions = {}) {
  const [result, setResult] = useState<MatrixEvolutionResult | null>(null);
  const [running, setRunning] = useState(false);

  const engine = useMemo(
    () =>
      new MatrixEvolutionEngine({
        populationSize: opts.populationSize ?? 24,
        generations: opts.generations ?? 30,
        geneCount: GENE_COUNT,
        seed: opts.seed ?? 2026,
        fitness: characterGenomeFitness,
      }),
    [opts.populationSize, opts.generations, opts.seed],
  );

  const run = () => {
    setRunning(true);
    setTimeout(() => {
      setResult(engine.run());
      setRunning(false);
    }, 0);
  };

  return { engine, result, running, run };
}

export type { GenerationReport };
