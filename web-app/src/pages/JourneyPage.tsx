import React, { useState } from "react";
import { Badge, Button, Card } from "@/components/ui";

const JOURNEY_STEPS = [
  { id: 1, name: "Awakening", desc: "Acknowledge the resonance of the twin signal." },
  { id: 2, name: "Forge", desc: "Sculpt heritage, features, and lifestyle budget." },
  { id: 3, name: "Align", desc: "Tune the 7.83 Hz Schumann coherence band." },
  { id: 4, name: "Simulate", desc: "Run the lifestyle lifecycle simulation." },
  { id: 5, name: "Evolve", desc: "Seed the agent matrix and evolve generations." },
  { id: 6, name: "Deploy", desc: "Instantiate the twin into production pipelines." },
];

/**
 * JourneyPage — 12-step activation journey (compact 6-step staging for demo).
 */
export function JourneyPage() {
  const [step, setStep] = useState(1);

  return (
    <main className="mx-auto max-w-3xl px-6 py-12">
      <Badge tone="cyan">Activation Journey</Badge>
      <h1 className="mt-3 text-3xl font-black uppercase tracking-widest text-slate-200">
        The Path of the Twin
      </h1>
      <p className="mt-2 text-sm text-slate-500">
        Complete the staging steps to earn your twin certificate.
      </p>

      <div className="mt-8 space-y-3">
        {JOURNEY_STEPS.map((s) => {
          const done = step > s.id;
          const active = step === s.id;
          return (
            <Card
              key={s.id}
              className={`flex items-center gap-4 !p-4 transition-all ${
                active ? "border-cyan-600/60 bg-cyan-950/20" : ""
              } ${done ? "opacity-70" : ""}`}
            >
              <div
                className={`flex h-9 w-9 shrink-0 items-center justify-center rounded-full border font-mono text-xs font-bold ${
                  done
                    ? "border-emerald-600 bg-emerald-950/40 text-emerald-300"
                    : active
                      ? "border-cyan-500 bg-cyan-950/40 text-cyan-300"
                      : "border-slate-700 text-slate-500"
                }`}
              >
                {done ? "✓" : s.id}
              </div>
              <div className="flex-1">
                <p className="text-sm font-bold uppercase tracking-wider text-slate-200">
                  {s.name}
                </p>
                <p className="text-xs text-slate-500">{s.desc}</p>
              </div>
              {active && (
                <Button
                  variant="accent"
                  onClick={() => setStep(step + 1)}
                >
                  Complete
                </Button>
              )}
            </Card>
          );
        })}
      </div>

      {step > JOURNEY_STEPS.length && (
        <Card className="mt-8 border-cyan-700/50 text-center">
          <p className="text-lg font-black uppercase tracking-widest text-cyan-300">
            🏆 Twin Certificate Issued
          </p>
          <p className="mt-1 text-xs text-slate-500">
            The twin is aligned, simulated, and ready for deployment.
          </p>
        </Card>
      )}
    </main>
  );
}
