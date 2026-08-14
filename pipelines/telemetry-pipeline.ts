/**
 * Pipeline: telemetry ingest → aggregate → report.
 *
 * Consumes the Schumann telemetry engine, aggregates windows into summaries,
 * and writes a JSON report. Run: npm run pipeline:telemetry
 */
import { writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { createTelemetryEngine } from "@dt-engine/telemetry";

const WINDOW = 60; // samples per window

const engine = createTelemetryEngine({ dt: 1, seed: 7, bufferSize: 100000 });
engine.run(600, { harmony: 0.6 });

interface WindowSummary {
  window: number;
  samples: number;
  avgSchumann: number;
  avgCoherence: number;
  peakPortal: number;
}

const windows: WindowSummary[] = [];
for (let w = 0; w * WINDOW < engine.buffer.length; w += 1) {
  const slice = engine.buffer.slice(w * WINDOW, (w + 1) * WINDOW);
  const avgSchumann = slice.reduce((a, s) => a + Math.abs(s.schumann), 0) / slice.length;
  const avgCoherence = slice.reduce((a, s) => a + s.coherence, 0) / slice.length;
  windows.push({
    window: w + 1,
    samples: slice.length,
    avgSchumann: Number(avgSchumann.toFixed(4)),
    avgCoherence: Number(avgCoherence.toFixed(4)),
    peakPortal: Number((avgCoherence * avgSchumann).toFixed(4)),
  });
}

const overall = {
  windows: windows.length,
  meanCoherence: Number(
    (windows.reduce((a, w) => a + w.avgCoherence, 0) / windows.length).toFixed(4),
  ),
  bestWindow: windows.reduce((a, b) => (b.avgCoherence > a.avgCoherence ? b : a)),
};

const outDir = join(import.meta.dirname, "output");
mkdirSync(outDir, { recursive: true });
const outPath = join(outDir, "telemetry-pipeline-report.json");
writeFileSync(
  outPath,
  JSON.stringify({ status: "SIMULATED", overall, windows }, null, 2),
);

console.log("telemetry-pipeline: ingest 600 samples → aggregated windows");
console.log(`  windows: ${overall.windows} · mean coherence: ${overall.meanCoherence}`);
console.log(`  best window: #${overall.bestWindow.window} (coherence ${overall.bestWindow.avgCoherence})`);
console.log(`✔ report → ${outPath}`);
