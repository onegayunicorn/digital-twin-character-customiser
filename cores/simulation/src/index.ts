/**
 * Aether Core — Simulation Engine core.
 *
 * A deterministic tick loop with seeded PRNG, time-series history capture,
 * waveform helpers (sine oscillator with noise), and a lifestyle lifecycle
 * simulator that evolves a character's stats day over day.
 */
import {
  cloneAttributes,
  LIFESTYLE_TOTAL_HOURS,
  type CharacterAttributes,
  type StatBlock,
  type StatKey,
} from "@dt-core/types";

// ── Deterministic PRNG (mulberry32) ────────────────────────────────────────

export type Rng = () => number;

export function mulberry32(seed: number): Rng {
  let a = seed >>> 0;
  return () => {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/** Standard normal via Box-Muller on a seeded uniform rng. */
export function gaussian(rng: Rng): number {
  const u = Math.max(rng(), 1e-12);
  const v = rng();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}

export function makeRng(seed?: number): Rng {
  return mulberry32(seed ?? (Date.now() & 0xffffffff));
}

// ── Waveform helpers ───────────────────────────────────────────────────────

export interface OscillatorOptions {
  frequency: number; // Hz
  amplitude?: number;
  phase?: number;
  noise?: number; // 0..1 noise injection
  rng?: Rng;
}

/** Sine oscillator with optional gaussian noise (e.g. Schumann 7.83 Hz). */
export function sampleOscillator(t: number, opts: OscillatorOptions): number {
  const amp = opts.amplitude ?? 1;
  const phase = opts.phase ?? 0;
  const noise = opts.noise ?? 0;
  const rng = opts.rng ?? makeRng(1);
  const clean = amp * Math.sin(2 * Math.PI * opts.frequency * t + phase);
  if (noise <= 0) return clean;
  return clean + noise * amp * gaussian(rng);
}

// ── Engine ─────────────────────────────────────────────────────────────────

/** One recorded time-series sample. */
export interface SimulationSample {
  t: number;
  [key: string]: number;
}

export interface SimulationEngineOptions {
  dt?: number; // seconds per tick
  maxT?: number; // total simulated seconds
  seed?: number;
}

export class SimulationEngine {
  readonly dt: number;
  readonly maxT: number;
  readonly rng: Rng;
  t = 0;
  history: SimulationSample[] = [];

  constructor(opts: SimulationEngineOptions = {}) {
    this.dt = opts.dt ?? 1;
    this.maxT = opts.maxT ?? 100;
    this.rng = makeRng(opts.seed);
  }

  /** Advance one tick, record the sample, return it. */
  step(sample: Omit<SimulationSample, "t">): SimulationSample {
    const record: SimulationSample = { t: this.t, ...sample };
    this.history.push(record);
    this.t += this.dt;
    return record;
  }

  /**
   * Run a simulation loop for `steps` ticks (or until maxT reached).
   * The tickFn receives (t, dt, rng) and returns numeric channels.
   */
  run(
    tickFn: (t: number, dt: number, rng: Rng) => Omit<SimulationSample, "t">,
    steps?: number,
  ): SimulationSample[] {
    const limit = Math.floor((steps ?? this.maxT) / this.dt);
    for (let i = 0; i < limit && this.t < this.maxT; i += 1) {
      this.step(tickFn(this.t, this.dt, this.rng));
    }
    return this.history;
  }

  reset(): void {
    this.t = 0;
    this.history = [];
  }
}

// ── Lifestyle lifecycle simulation ─────────────────────────────────────────

export interface LifestyleLifecycleOptions {
  days?: number;
  seed?: number;
  /** Optional daily noise applied to each category before renormalisation. */
  volatility?: number;
  /** Optional stat modifier function (e.g. from @dt-engine/lifestyle). */
  statModifier?: (lifestyle: CharacterAttributes["lifestyle"]) => StatBlock;
}

export interface LifestyleDayResult {
  day: number;
  lifestyle: CharacterAttributes["lifestyle"];
  stats: StatBlock;
}

export interface LifestyleLifecycleResult {
  days: LifestyleDayResult[];
  finalStats: StatBlock;
  bestDay: LifestyleDayResult;
}

function emptyStats(): StatBlock {
  return {
    stamina: 0,
    strength: 0,
    stealth: 0,
    shooting: 0,
    driving: 0,
    lungCapacity: 0,
    flying: 0,
  };
}

/**
 * Simulate `days` days of a character's lifestyle: each day a small
 * perturbation is applied to the 24h allocation (renormalised to exactly 24h)
 * and stat modifiers are recomputed, producing a stat trajectory.
 */
export function simulateLifestyleLifecycle(
  attributes: CharacterAttributes,
  opts: LifestyleLifecycleOptions = {},
): LifestyleLifecycleResult {
  const days = opts.days ?? 30;
  const volatility = opts.volatility ?? 0.15;
  const rng = makeRng(opts.seed);
  const modifier =
    opts.statModifier ??
    (() => {
      const s = emptyStats();
      // Identity fallback: hours directly drive a scaled stat proxy
      s.stamina = attributes.lifestyle.sports / 8;
      s.strength = attributes.lifestyle.sports / 8;
      s.stealth = attributes.lifestyle.illegalWork / 8;
      return s;
    });

  const current = cloneAttributes(attributes);
  const results: LifestyleDayResult[] = [];

  for (let day = 0; day < days; day += 1) {
    const b = current.lifestyle;
    // Perturb each category, then renormalise to exactly 24h
    b.sleeping += (rng() - 0.5) * 2 * volatility * b.sleeping;
    b.friends += (rng() - 0.5) * 2 * volatility * b.friends;
    b.sports += (rng() - 0.5) * 2 * volatility * b.sports;
    b.legalWork += (rng() - 0.5) * 2 * volatility * b.legalWork;
    b.illegalWork += (rng() - 0.5) * 2 * volatility * b.illegalWork;

    let sum = b.sleeping + b.friends + b.sports + b.legalWork + b.illegalWork;
    if (sum <= 0) sum = LIFESTYLE_TOTAL_HOURS;
    const scale = LIFESTYLE_TOTAL_HOURS / sum;
    b.sleeping *= scale;
    b.friends *= scale;
    b.sports *= scale;
    b.legalWork *= scale;
    b.illegalWork *= scale;
    // Clamp per-category to [1, 10] and renormalise once more
    b.sleeping = Math.min(10, Math.max(1, b.sleeping));
    b.friends = Math.min(10, Math.max(1, b.friends));
    b.sports = Math.min(10, Math.max(1, b.sports));
    b.legalWork = Math.min(10, Math.max(1, b.legalWork));
    b.illegalWork = Math.min(10, Math.max(1, b.illegalWork));
    sum = b.sleeping + b.friends + b.sports + b.legalWork + b.illegalWork;
    const s2 = LIFESTYLE_TOTAL_HOURS / sum;
    b.sleeping *= s2;
    b.friends *= s2;
    b.sports *= s2;
    b.legalWork *= s2;
    b.illegalWork *= s2;

    const stats = modifier(b);
    results.push({ day, lifestyle: { ...b }, stats: { ...stats } });
  }

  const finalStats = results[results.length - 1]?.stats ?? emptyStats();
  const bestDay = results.reduce<LifestyleDayResult>(
    (best, r) =>
      statSum(r.stats) > statSum(best.stats) ? r : best,
    results[0] ?? { day: 0, lifestyle: current.lifestyle, stats: emptyStats() },
  );

  return { days: results, finalStats, bestDay };
}

function statSum(s: StatBlock): number {
  return (Object.keys(s) as StatKey[]).reduce((acc, k) => acc + s[k], 0);
}
