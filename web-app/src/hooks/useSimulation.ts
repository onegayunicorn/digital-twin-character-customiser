import { useMemo, useState } from "react";
import {
  simulateLifestyleLifecycle,
  SimulationEngine,
  type LifestyleLifecycleResult,
} from "@dt-core/simulation";
import { calculateStatModifiers } from "@dt-engine/lifestyle";
import { useCustomizerStore } from "@dt-core/state";

export interface UseSimulationOptions {
  days?: number;
  seed?: number;
}

/**
 * useSimulation — runs the lifestyle lifecycle simulation against the current
 * character and exposes the trajectory + a generic engine for custom sims.
 */
export function useSimulation(opts: UseSimulationOptions = {}) {
  const activeCharacter = useCustomizerStore((s) => s.activeCharacter);
  const [result, setResult] = useState<LifestyleLifecycleResult | null>(null);
  const [running, setRunning] = useState(false);

  const engine = useMemo(
    () =>
      new SimulationEngine({
        dt: 1,
        maxT: opts.days ?? 30,
        seed: opts.seed ?? 2026,
      }),
    [opts.days, opts.seed],
  );

  const run = () => {
    setRunning(true);
    // Defer heavy compute out of the render/event critical path
    setTimeout(() => {
      const res = simulateLifestyleLifecycle(activeCharacter, {
        days: opts.days ?? 30,
        seed: opts.seed ?? 2026,
        statModifier: (l) => calculateStatModifiers(l),
      });
      setResult(res);
      setRunning(false);
    }, 0);
  };

  const currentStats = useMemo(
    () => calculateStatModifiers(activeCharacter.lifestyle),
    [activeCharacter.lifestyle],
  );

  return { engine, result, running, run, currentStats };
}
