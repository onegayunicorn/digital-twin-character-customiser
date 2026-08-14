import React, { useEffect, useState } from "react";
import { useTelemetry } from "@/hooks/useTelemetry";
import { Badge, Card, StatBar } from "@/components/ui";
import { SCHUMANN_HZ } from "@dt-engine/telemetry";

/**
 * TelemetryPage — live telemetry & 7.83 Hz Schumann resonance monitor.
 */
export function TelemetryPage() {
  const telemetry = useTelemetry({ live: true, intervalMs: 800, seed: 7 });
  const latest = telemetry.latest;
  const [avg, setAvg] = useState(0);

  useEffect(() => {
    if (telemetry.buffer.length > 0) {
      setAvg(telemetry.averageCoherence());
    }
  }, [telemetry.buffer.length, telemetry]);

  return (
    <main className="mx-auto max-w-5xl px-6 py-12">
      <div className="flex items-center justify-between">
        <div>
          <Badge tone="cyan">Live Telemetry</Badge>
          <h1 className="mt-3 text-3xl font-black uppercase tracking-widest text-slate-200">
            Schumann Resonance Monitor
          </h1>
          <p className="mt-1 text-sm text-slate-500">
            Earth's fundamental electromagnetic resonance — {SCHUMANN_HZ.toFixed(2)} Hz baseband.
          </p>
        </div>
        <span className="flex items-center gap-2 rounded-full border border-emerald-700/50 bg-emerald-950/40 px-3 py-1.5 font-mono text-[10px] uppercase tracking-widest text-emerald-300">
          <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-emerald-400" />
          Streaming
        </span>
      </div>

      <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <Card>
          <StatBar label="Schumann Amplitude" value={Math.abs(latest?.schumann ?? 0)} />
          <p className="mt-2 font-mono text-xs text-slate-600">t = {latest?.t.toFixed(0) ?? 0}s</p>
        </Card>
        <Card>
          <StatBar label="Coherence Index" value={latest?.coherence ?? 0} />
        </Card>
        <Card>
          <StatBar label="Entropy" value={latest?.entropy ?? 0} />
        </Card>
        <Card>
          <StatBar label="Twin Vitality" value={latest?.heartbeat ?? 0} />
        </Card>
      </div>

      {/* Waveform strip */}
      <Card className="mt-4">
        <p className="mb-3 text-[10px] font-bold uppercase tracking-widest text-slate-500">
          Resonance Waveform — recent buffer
        </p>
        <div className="flex h-24 items-end gap-[2px]">
          {telemetry.buffer.slice(-60).map((sample, i) => {
            const h = 8 + (Math.abs(sample.schumann) * 70);
            const coherent = sample.coherence > 0.6;
            return (
              <div
                key={i}
                className="flex-1 rounded-t transition-all duration-200"
                style={{
                  height: `${Math.max(4, h)}%`,
                  background: coherent
                    ? "linear-gradient(180deg, #06b6d4, #2563eb)"
                    : "linear-gradient(180deg, #64748b, #1e293b)",
                }}
              />
            );
          })}
        </div>
        <p className="mt-3 font-mono text-xs text-slate-600">
          Rolling coherence average: <span className="text-cyan-400">{avg.toFixed(3)}</span>
        </p>
      </Card>
    </main>
  );
}
