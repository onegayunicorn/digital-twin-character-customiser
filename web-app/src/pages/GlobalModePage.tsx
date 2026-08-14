import React, { useState } from "react";
import { useTelemetry } from "@/hooks/useTelemetry";
import { Badge, Button, Card } from "@/components/ui";

/**
 * GlobalModePage — collective coherence monitor. Aggregates the twin telemetry
 * stream into a global coherence index (SIMULATED aggregate).
 */
export function GlobalModePage() {
  const telemetry = useTelemetry({ live: true, intervalMs: 1200, seed: 21 });
  const [nodes, setNodes] = useState(128);

  const latest = telemetry.latest;
  const coherence = latest?.coherence ?? 0.5;
  const globalIndex = Math.min(1, coherence * (0.85 + 0.15 * Math.sin(nodes / 10)));

  return (
    <main className="mx-auto max-w-5xl px-6 py-12">
      <div className="flex items-center justify-between">
        <div>
          <Badge tone="emerald">Collective Monitor</Badge>
          <h1 className="mt-3 text-3xl font-black uppercase tracking-widest text-slate-200">
            Global Mode — Coherence Field
          </h1>
          <p className="mt-1 text-sm text-slate-500">
            Aggregated resonance coherence across the twin network (SIMULATED).
          </p>
        </div>
        <div className="flex items-center gap-3">
          <label className="text-xs font-bold uppercase tracking-wider text-slate-500">
            Nodes
          </label>
          <input
            type="number"
            min={8}
            max={4096}
            step={8}
            value={nodes}
            onChange={(e) => setNodes(Number(e.target.value))}
            className="w-24 rounded-lg border border-slate-700 bg-slate-900 px-2 py-1.5 font-mono text-xs text-slate-200 outline-none focus:border-cyan-500"
          />
        </div>
      </div>

      {/* Coherence dial */}
      <Card className="mt-8 flex flex-col items-center border-cyan-800/40">
        <div
          className="relative flex h-48 w-48 items-center justify-center rounded-full border-8 border-slate-800"
          style={{
            background: `conic-gradient(#06b6d4 ${globalIndex * 360}deg, #1e293b 0deg)`,
          }}
        >
          <div className="flex h-36 w-36 flex-col items-center justify-center rounded-full bg-slate-950">
            <span className="font-mono text-4xl font-black text-cyan-300">
              {(globalIndex * 100).toFixed(1)}
            </span>
            <span className="text-[10px] uppercase tracking-widest text-slate-500">
              Global Index
            </span>
          </div>
        </div>
        <p className="mt-4 text-center text-xs text-slate-500">
          {globalIndex > 0.8
            ? "Field coherent — collective resonance maintained."
            : globalIndex > 0.5
              ? "Field partially coherent — aligning nodes."
              : "Field scattered — re-tuning node band."}
        </p>
      </Card>

      <div className="mt-4 grid gap-4 sm:grid-cols-3">
        <Card>
          <p className="text-[10px] font-bold uppercase tracking-widest text-slate-500">Nodes Online</p>
          <p className="mt-1 font-mono text-2xl font-bold text-slate-200">{nodes}</p>
        </Card>
        <Card>
          <p className="text-[10px] font-bold uppercase tracking-widest text-slate-500">Base Coherence</p>
          <p className="mt-1 font-mono text-2xl font-bold text-cyan-400">{coherence.toFixed(3)}</p>
        </Card>
        <Card>
          <p className="text-[10px] font-bold uppercase tracking-widest text-slate-500">Stream Time</p>
          <p className="mt-1 font-mono text-2xl font-bold text-slate-200">
            {latest?.t.toFixed(0) ?? 0}s
          </p>
        </Card>
      </div>

      <div className="mt-6 flex gap-3">
        <Button variant="accent" onClick={() => setNodes((n) => Math.min(4096, n * 2))}>
          Double Network
        </Button>
        <Button variant="default" onClick={() => setNodes(128)}>
          Reset
        </Button>
      </div>
    </main>
  );
}
