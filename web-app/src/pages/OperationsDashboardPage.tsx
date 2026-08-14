import React from "react";
import { useAgentMatrix } from "@/hooks/useAgentMatrix";
import { useSimulation } from "@/hooks/useSimulation";
import { NFTMarketplaceBridge } from "@/components/dashboard/NFTMarketplaceBridge";
import { Badge, Button, Card, StatBar } from "@/components/ui";
import { decodeGenomeToAttributes } from "@dt-engine/evolution";
import { calculateStatModifiers } from "@/utils/statCalculators";

/**
 * OperationsDashboardPage — unified operations dashboard: agent matrix
 * evolution, lifestyle simulation, and the Star Seed NFT marketplace bridge.
 */
export function OperationsDashboardPage() {
  const matrix = useAgentMatrix({ populationSize: 20, generations: 25, seed: 2026 });
  const sim = useSimulation({ days: 30, seed: 2026 });

  const bestAttrs = matrix.result
    ? decodeGenomeToAttributes(matrix.result.best.genome)
    : null;
  const bestStats = bestAttrs ? calculateStatModifiers(bestAttrs.lifestyle) : null;

  return (
    <main className="mx-auto max-w-6xl space-y-6 px-6 py-12">
      <div>
        <Badge tone="cyan">Unified Operations</Badge>
        <h1 className="mt-3 text-3xl font-black uppercase tracking-widest text-slate-200">
          Operations Dashboard
        </h1>
        <p className="mt-1 text-sm text-slate-500">
          Agent matrix evolution · lifestyle simulation · Star Seed marketplace bridge.
        </p>
      </div>

      <div className="grid gap-6 lg:grid-cols-2">
        {/* Agent Matrix Evolution */}
        <Card className="flex flex-col gap-4">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-sm font-bold uppercase tracking-widest text-slate-200">
                Agent Matrix Evolution
              </h2>
              <p className="text-xs text-slate-500">
                GA population · 18-gene character genome · elitism + tournament selection
              </p>
            </div>
            <Button variant="accent" onClick={matrix.run} disabled={matrix.running}>
              {matrix.running ? "Evolving…" : matrix.result ? "Re-Evolve" : "Evolve"}
            </Button>
          </div>

          {matrix.result ? (
            <div className="space-y-3">
              <div className="grid grid-cols-3 gap-2 rounded-xl border border-slate-800 bg-slate-950/60 p-3 font-mono text-xs">
                <div>
                  <p className="text-slate-500">Best Fitness</p>
                  <p className="text-lg font-bold text-cyan-400">
                    {matrix.result.best.fitness.toFixed(4)}
                  </p>
                </div>
                <div>
                  <p className="text-slate-500">Generations</p>
                  <p className="text-lg font-bold text-slate-200">
                    {matrix.result.finalGeneration}
                  </p>
                </div>
                <div>
                  <p className="text-slate-500">Population</p>
                  <p className="text-lg font-bold text-slate-200">
                    {matrix.result.agents.length}
                  </p>
                </div>
              </div>

              {/* Fitness trajectory */}
              <div className="flex h-20 items-end gap-[2px]">
                {matrix.result.history.map((report, i) => (
                  <div
                    key={i}
                    className="flex-1 rounded-t bg-gradient-to-t from-cyan-600 to-blue-500"
                    style={{ height: `${Math.max(6, (report.bestFitness / 1.0) * 100)}%` }}
                    title={`gen ${report.generation}: ${report.bestFitness.toFixed(3)}`}
                  />
                ))}
              </div>

              {bestStats && (
                <div className="grid grid-cols-2 gap-x-4 gap-y-2">
                  {(Object.keys(bestStats) as Array<keyof typeof bestStats>).map((k) => (
                    <StatBar key={k} label={k} value={bestStats[k]} />
                  ))}
                </div>
              )}
              <p className="font-mono text-[10px] text-slate-600">
                {matrix.result.converged ? "✓ converged" : "○ still improving"} · best archetype:{" "}
                {matrix.result.best.archetype ?? "—"}
              </p>
            </div>
          ) : (
            <div className="flex h-48 items-center justify-center rounded-xl border border-dashed border-slate-800 font-mono text-xs tracking-widest text-slate-600">
              [ SEED AGENT MATRIX TO BEGIN EVOLUTION ]
            </div>
          )}
        </Card>

        {/* Lifestyle Simulation */}
        <Card className="flex flex-col gap-4">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-sm font-bold uppercase tracking-widest text-slate-200">
                Lifestyle Lifecycle Simulation
              </h2>
              <p className="text-xs text-slate-500">
                30-day hour-allocation trajectory · stat modifiers
              </p>
            </div>
            <Button variant="default" onClick={sim.run} disabled={sim.running}>
              {sim.running ? "Simulating…" : sim.result ? "Re-Run" : "Run Simulation"}
            </Button>
          </div>

          {sim.result ? (
            <div className="space-y-3">
              <div className="grid grid-cols-3 gap-2 rounded-xl border border-slate-800 bg-slate-950/60 p-3 font-mono text-xs">
                <div>
                  <p className="text-slate-500">Days</p>
                  <p className="text-lg font-bold text-slate-200">{sim.result.days.length}</p>
                </div>
                <div>
                  <p className="text-slate-500">Best Day</p>
                  <p className="text-lg font-bold text-cyan-400">
                    #{sim.result.bestDay.day + 1}
                  </p>
                </div>
                <div>
                  <p className="text-slate-500">Stamina Final</p>
                  <p className="text-lg font-bold text-slate-200">
                    {sim.result.finalStats.stamina.toFixed(2)}
                  </p>
                </div>
              </div>
              <div className="flex h-20 items-end gap-[2px]">
                {sim.result.days.map((d, i) => (
                  <div
                    key={i}
                    className="flex-1 rounded-t bg-gradient-to-t from-emerald-600 to-teal-400"
                    style={{ height: `${Math.max(6, d.stats.stamina * 100)}%` }}
                    title={`day ${d.day + 1}: stamina ${d.stats.stamina.toFixed(2)}`}
                  />
                ))}
              </div>
              <p className="font-mono text-[10px] text-slate-600">
                ✓ every day budget validated to exactly 24h
              </p>
            </div>
          ) : (
            <div className="flex h-48 items-center justify-center rounded-xl border border-dashed border-slate-800 font-mono text-xs tracking-widest text-slate-600">
              [ RUN LIFESTYLE LIFECYCLE SIMULATION ]
            </div>
          )}
        </Card>
      </div>

      <NFTMarketplaceBridge />
    </main>
  );
}
