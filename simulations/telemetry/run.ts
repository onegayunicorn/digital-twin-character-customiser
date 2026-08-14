/**
 * Simulation: 7.83 Hz Schumann resonance telemetry stream.
 *
 * Streams deterministic telemetry samples, computes the rolling coherence,
 * and writes a telemetry report + CSV of the buffer.
 * Status: SIMULATED.
 */
import { writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import {
  createTelemetryEngine,
  averageCoherence,
  SCHUMANN_HZ,
} from "@dt-engine/telemetry";

const STEPS = Number(process.env.SIM_STEPS ?? 240);
const seed = Number(process.env.SIM_SEED ?? 7);

console.log("══════════════════════════════════════════════════════");
console.log(" SCHUMANN RESONANCE TELEMETRY SIMULATION");
console.log(" Status: SIMULATED (deterministic, seeded)");
console.log(` Frequency: ${SCHUMANN_HZ.toFixed(2)} Hz · Steps: ${STEPS} · Seed: ${seed}`);
console.log("══════════════════════════════════════════════════════\n");

const engine = createTelemetryEngine({ dt: 1, seed, bufferSize: STEPS });
engine.run(STEPS, { harmony: 0.6, vitality: 0.75 });

const samples = engine.buffer;
console.log(` Streamed ${samples.length} samples`);
console.log(` Rolling coherence (avg): ${averageCoherence(engine).toFixed(4)}`);

const first = samples[0];
const last = samples[samples.length - 1];
console.log(` First: t=${first?.t}s schumann=${first?.schumann.toFixed(4)} coherence=${first?.coherence.toFixed(4)}`);
console.log(` Last:  t=${last?.t}s schumann=${last?.schumann.toFixed(4)} coherence=${last?.coherence.toFixed(4)}`);

// Coherence band histogram
const bands = [0, 0, 0, 0, 0]; // 0.0-0.2 ... 0.8-1.0
for (const s of samples) {
  const idx = Math.min(4, Math.floor(s.coherence * 5));
  bands[idx] = (bands[idx] ?? 0) + 1;
}
console.log("\n Coherence distribution:");
for (let i = 0; i < 5; i += 1) {
  const lo = i * 0.2;
  const hi = lo + 0.2;
  console.log(`   [${lo.toFixed(1)}–${hi.toFixed(1)}]  ${"█".repeat(bands[i] ?? 0)} ${bands[i] ?? 0}`);
}

// Report + CSV
const outDir = join(import.meta.dirname, "output");
mkdirSync(outDir, { recursive: true });
const report = {
  title: "Schumann Telemetry Stream Simulation",
  status: "SIMULATED",
  seed,
  frequencyHz: SCHUMANN_HZ,
  steps: STEPS,
  rollingCoherence: averageCoherence(engine),
  samples: samples.map((s) => ({
    t: s.t,
    schumann: Number(s.schumann.toFixed(4)),
    coherence: Number(s.coherence.toFixed(4)),
    entropy: Number(s.entropy.toFixed(4)),
  })),
};
writeFileSync(join(outDir, "telemetry-report.json"), JSON.stringify(report, null, 2));

const csv = ["t,schumann,coherence,entropy", ...samples.map((s) => `${s.t},${s.schumann.toFixed(4)},${s.coherence.toFixed(4)},${s.entropy.toFixed(4)}`)].join("\n");
writeFileSync(join(outDir, "telemetry.csv"), csv);
console.log("\n✔ Report written → simulations/telemetry/output/telemetry-report.json (+ .csv)");
