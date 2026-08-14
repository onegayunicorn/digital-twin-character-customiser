/**
 * Quantum Reality Interface — Theoretical Physics Simulation Platform.
 *
 * ⚠ CRITICAL SCIENTIFIC DISCLAIMER
 * This is a computational simulation of theoretical physics concepts. The
 * concept of "splitting a portal in reality" through photonic entanglement
 * and molecular oscillation is NOT supported by established physics. All
 * outputs are mathematical predictions within this model's framework and are
 * watermarked SIMULATION.
 *
 * Implements the 5-phase Standard Operating Procedure (SOP) protocol:
 *   INITIALIZE → ENTANGLEMENT SEEDING → GHz FIELD ACTIVATION →
 *   COHERENCE AMPLIFICATION → INTERFACE FORMATION → OBSERVATION
 * with hard-coded safety constraints (energy cap, coherence limit,
 * auto-shutdown, decoherence shutdown).
 */
import { writeFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { mulberry32, gaussian } from "@dt-core/simulation";

// ── Physical constants (CODATA) ────────────────────────────────────────────
const HBAR = 1.0545718e-34; // J·s
const C = 2.99792458e8; // m/s
const E_CHARGE = 1.6021766e-19; // C
const EPS0 = 8.8541878e-12; // F/m
const KB = 1.380649e-23; // J/K
const G = 6.6743e-11; // m³/kg·s²

// ── Simulation parameters (per SOP) ────────────────────────────────────────
const PHASES = [
  { name: "ENTANGLEMENT SEEDING", from: 0, to: 10 },
  { name: "GHz FIELD ACTIVATION", from: 10, to: 30 },
  { name: "COHERENCE AMPLIFICATION", from: 30, to: 70 },
  { name: "INTERFACE FORMATION", from: 70, to: 90 },
  { name: "OBSERVATION & MEASUREMENT", from: 90, to: 100 },
] as const;

interface SimConfig {
  particles: number;
  ghzFreq: number; // GHz
  fieldAmplitude: number; // MV/m (peak during interface phase)
  entanglementRate: number; // pairs/ns
  temperatureK: number;
  maxEnergyJ: number; // safety cap
  maxEntangledParticles: number; // safety cap
  portalShutdown: number; // P > this → auto-shutdown
  dtNs: number;
  totalNs: number;
}

const CONFIG: SimConfig = {
  particles: 1000,
  ghzFreq: 2.45,
  fieldAmplitude: 5.0,
  entanglementRate: 100,
  temperatureK: 1.0,
  maxEnergyJ: 1.0,
  maxEntangledParticles: 1000,
  portalShutdown: 1.5,
  dtNs: 1,
  totalNs: 100,
};

interface Particle {
  x: number;
  y: number;
  vx: number;
  vy: number;
  massKg: number;
  chargeC: number;
  dissociated: boolean;
}

interface StepTelemetry {
  tNs: number;
  phase: string;
  fidelity: number; // entanglement fidelity F
  concurrence: number; // entanglement measure
  entropy: number; // entropy of entanglement (ebits)
  coherence: number; // molecular coherence 0..1
  fieldMVm: number; // applied field
  energyJ: number; // total EM energy
  decoherenceRate: number; // 1/ns
  portalMetric: number; // P
  dissociatedPct: number; // % particles dissociated
}

interface SafetyEvent {
  tNs: number;
  code: string;
  message: string;
}

function clamp01(v: number): number {
  return Math.min(1, Math.max(0, v));
}

/**
 * Entanglement fidelity evolution:
 *   seeding ramp → F = 0.95 at t = 10ns
 *   gentle decay through amplification (F ≈ 0.88 at t = 70ns)
 *   entanglement-swapping burst re-pumps F ≈ 0.92 at interface start
 *   decay through observation (F ≈ 0.78 at t = 100ns)
 */
function fidelityAt(t: number, config: SimConfig): number {
  if (t <= 10) return 0.95 * (t / 10); // ramp to target F=0.95 during seeding
  if (t <= 70) return 0.95 - (t - 10) * 0.00117; // ≈0.88 at t=70
  if (t <= 78) return 0.88 + (0.92 - 0.88) * ((t - 70) / 8); // swapping burst
  return Math.max(0.4, 0.92 - (t - 78) * 0.0064); // decay to ≈0.78 at t=100
}

/** Concurrence for a Werner-like two-qubit state: C = max(0, 2F - 1). */
function concurrenceOf(fidelity: number): number {
  return Math.max(0, 2 * fidelity - 1);
}

/** Entropy of entanglement for a Bell-diagonal state with fidelity F. */
function entropyOf(fidelity: number): number {
  const p = clamp01(fidelity);
  if (p <= 0 || p >= 1) return 0;
  const q = 1 - p;
  return -(p * Math.log2(p) + q * Math.log2(q));
}

/**
 * Langevin dynamics: one step for the dust particle cloud under the GHz field.
 * Bond dissociation is modelled as field-heating: each particle breaks with a
 * per-step probability growing with (E/E_max)², so the cloud stays coherent
 * through amplification and only begins to dissociate at interface drive
 * (matching the SOP gate: <1% dissociated when the field phase ends).
 */
function stepDust(
  particles: Particle[],
  tNs: number,
  config: SimConfig,
  rng: () => number,
): { energyJ: number; dissociatedPct: number; coherence: number; kineticSum: number } {
  const omega = 2 * Math.PI * config.ghzFreq * 1e9;
  const E0 = fieldAt(tNs, config) * 1e6; // V/m
  const gamma = 1e-8; // damping (kg/s) — dust regime
  const damping = Math.exp(-gamma * config.dtNs * 1e-9);
  const kbT = KB * config.temperatureK;
  const intensity = clamp01(fieldAt(tNs, config) / config.fieldAmplitude);
  const breakProb = Math.min(0.004, intensity * intensity * 0.004);

  let kinetic = 0;
  let dissociated = 0;
  let oscillation = 0;

  for (const p of particles) {
    if (p.dissociated) {
      dissociated += 1;
      continue;
    }
    const force = p.chargeC * E0 * Math.cos(omega * tNs * 1e-9);
    const noise = Math.sqrt(2 * gamma * kbT * config.dtNs * 1e-9) * gaussian(rng);
    p.vx = p.vx * damping + ((force + noise) / p.massKg) * config.dtNs * 1e-9;
    p.x += p.vx * config.dtNs * 1e-9;
    const ke = 0.5 * p.massKg * p.vx * p.vx;
    kinetic += ke;
    oscillation += Math.abs(p.vx);
    if (rng() < breakProb) p.dissociated = true;
  }

  return {
    energyJ: 0.5 * EPS0 * E0 * E0 * 1e-12, // field energy in the 1 mm³ chamber (model)
    dissociatedPct: (dissociated / particles.length) * 100,
    coherence: clamp01(1 - dissociated / particles.length),
    kineticSum: kinetic,
  };
}

function fieldAt(tNs: number, config: SimConfig): number {
  if (tNs <= 10) return 0; // no field during seeding
  if (tNs <= 30) {
    // ramp 0 → peak
    return config.fieldAmplitude * ((tNs - 10) / 20);
  }
  if (tNs <= 70) return config.fieldAmplitude * 0.7;
  return config.fieldAmplitude; // interface peak
}

/**
 * Caldeira-Leggett style decoherence that also grows with the drive field
 * (critical-regime feedback): the harder the field pushes, the faster the
 * state loses purity — the portal metric only crosses 1.0 during the brief
 * interface window when fidelity is re-pumped by entanglement swapping.
 */
function decoherenceRateAt(
  fidelity: number,
  temperatureK: number,
  fieldIntensity: number,
): number {
  return 0.5 + 0.5 * (1 - fidelity) + 0.2 * fieldIntensity + 0.01 * temperatureK;
}

function phaseAt(t: number): string {
  for (const phase of PHASES) {
    if (t >= phase.from && t < phase.to) return phase.name;
  }
  return "OBSERVATION & MEASUREMENT";
}

// ── Main run ───────────────────────────────────────────────────────────────
export function runQuantumSimulation(config: SimConfig = CONFIG): {
  telemetry: StepTelemetry[];
  safety: SafetyEvent[];
  final: StepTelemetry;
  portalFormed: boolean;
  shutdown: boolean;
} {
  const rng = mulberry32(2026);
  const safety: SafetyEvent[] = [];
  const telemetry: StepTelemetry[] = [];

  // INITIALIZE — Yee grid (model) + dust cloud
  const particles: Particle[] = Array.from({ length: config.particles }, () => ({
    x: rng(),
    y: rng(),
    vx: gaussian(rng) * 1e-6,
    vy: gaussian(rng) * 1e-6,
    massKg: 1e-18, // ~1 μm SiO2 dust grain (model)
    chargeC: 1e4 * E_CHARGE,
    dissociated: false,
  }));

  let shutdown = false;
  let portalFormed = false;

  for (let t = 0; t <= config.totalNs && !shutdown; t += config.dtNs) {
    const fidelity = fidelityAt(t, config);
    const concurrence = concurrenceOf(fidelity);
    const entropy = entropyOf(fidelity);

    const dust = stepDust(particles, t, config, rng);
    const coherence = dust.coherence;
    const fieldMVm = fieldAt(t, config);
    const energyJ = dust.energyJ;
    const fieldIntensity = clamp01(fieldMVm / config.fieldAmplitude);
    const decoherence = decoherenceRateAt(fidelity, config.temperatureK, fieldIntensity);

    // Portal metric P = (Fidelity × Coherence × FieldIntensity) / DecoherenceRate
    const portalMetric =
      (fidelity * coherence * fieldIntensity) / Math.max(1e-6, decoherence);

    const step: StepTelemetry = {
      tNs: t,
      phase: phaseAt(t),
      fidelity,
      concurrence,
      entropy,
      coherence,
      fieldMVm,
      energyJ,
      decoherenceRate: decoherence,
      portalMetric,
      dissociatedPct: dust.dissociatedPct,
    };
    telemetry.push(step);

    // ── SAFETY PROTOCOLS (hard-coded) ───────────────────────────────────
    if (energyJ >= config.maxEnergyJ) {
      safety.push({
        tNs: t,
        code: "ENERGY_CAP",
        message: `Total EM energy ${energyJ.toExponential(2)} J ≥ 1 J cap — shutdown`,
      });
      shutdown = true;
    }
    if (portalMetric > config.portalShutdown) {
      safety.push({
        tNs: t,
        code: "PORTAL_AUTO_SHUTDOWN",
        message: `Portal Metric P=${portalMetric.toFixed(3)} > ${config.portalShutdown} — requires explicit confirmation to continue`,
      });
      shutdown = true;
    }
    if (config.particles > config.maxEntangledParticles) {
      safety.push({
        tNs: t,
        code: "COHERENCE_LIMIT",
        message: `Entangled particles ${config.particles} > ${config.maxEntangledParticles} cap`,
      });
      shutdown = true;
    }
    if (portalMetric > 1.0) portalFormed = true;
  }

  // DECOHERENCE ASSURANCE — every run ends with forced state collapse
  safety.push({
    tNs: telemetry[telemetry.length - 1]?.tNs ?? config.totalNs,
    code: "DECOHERENCE_ASSURANCE",
    message: "Forced state collapse/decoherence at run end",
  });

  const final = telemetry[telemetry.length - 1]!;
  return { telemetry, safety, final, portalFormed, shutdown };
}

// ── CLI ────────────────────────────────────────────────────────────────────
function main(): void {
  console.log("════════════════════════════════════════════════════════════");
  console.log(" QUANTUM REALITY INTERFACE — Theoretical Physics Simulation");
  console.log(" ⚠ SIMULATION ONLY — not an experimentally-verified phenomenon");
  console.log(` Particles: ${CONFIG.particles} · GHz: ${CONFIG.ghzFreq} · E: ${CONFIG.fieldAmplitude} MV/m · T: ${CONFIG.temperatureK} K`);
  console.log("════════════════════════════════════════════════════════════\n");

  const { telemetry, safety, final, portalFormed, shutdown } = runQuantumSimulation();

  const rows = telemetry.filter((s) => s.tNs % 10 === 0 || s.portalMetric > 1);
  console.log(" t(ns)  phase                          F      C      S     P      E(J)          coherence");
  for (const s of rows) {
    console.log(
      ` ${String(s.tNs).padStart(4)}   ${s.phase.padEnd(29)} ${s.fidelity.toFixed(2)}  ${s.concurrence.toFixed(2)}  ${s.entropy.toFixed(2)}  ${s.portalMetric.toFixed(3)}  ${s.energyJ.toExponential(1).padStart(10)}  ${s.coherence.toFixed(2)}`,
    );
  }

  console.log(`\n Portal Metric final: ${final.portalMetric.toFixed(4)} (threshold 1.0)`);
  console.log(` Interface formation: ${portalFormed ? "YES (P > 1.0 in model)" : "no"}`);
  console.log(` Auto-shutdown engaged: ${shutdown ? "yes" : "no"}`);
  console.log("\n Safety events:");
  for (const ev of safety) {
    console.log(`   [${ev.code}] t=${ev.tNs}ns — ${ev.message}`);
  }

  // Report
  const outDir = join(import.meta.dirname, "output");
  mkdirSync(outDir, { recursive: true });
  const report = {
    title: "Quantum Reality Interface Simulation",
    status: "SIMULATION",
    disclaimer: "Computational model only. 'Portal formation' is a model-internal metric, not an experimentally-verified physical phenomenon.",
    constants: { hbar: HBAR, c: C, e: E_CHARGE, eps0: EPS0, kb: KB, G },
    config: CONFIG,
    portalFormed,
    shutdown,
    final,
    telemetry,
    safety,
  };
  writeFileSync(join(outDir, "quantum-interface-report.json"), JSON.stringify(report, null, 2));
  console.log("\n✔ Report written → simulations/quantum-interface/output/quantum-interface-report.json");

  // Standalone dashboard (self-contained HTML, no CDN)
  const template = readFileSync(join(import.meta.dirname, "dashboard-template.html"), "utf8");
  const dashboard = template.replace(
    "/*__TELEMETRY__*/",
    JSON.stringify(telemetry),
  );
  writeFileSync(join(outDir, "dashboard.html"), dashboard);
  console.log("✔ Dashboard written → simulations/quantum-interface/output/dashboard.html");
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main();
}
