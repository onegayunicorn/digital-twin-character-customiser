/**
 * Aether Core engine — Telemetry.
 *
 * Live telemetry stream built on the 7.83 Hz Schumann resonance (the Earth's
 * fundamental electromagnetic resonance). Emits samples with the resonance
 * wave, a coherence index, entropy, and optional character mood channels.
 * Deterministic when seeded; buffers the last N samples for dashboards.
 */
import { makeRng, sampleOscillator, mulberry32, type Rng } from "@dt-core/simulation";

export const SCHUMANN_HZ = 7.83;

export interface TelemetrySample {
  t: number;
  schumann: number; // 7.83 Hz resonance amplitude
  coherence: number; // 0..1 coherence index
  entropy: number; // 0..1 disorder metric
  harmonic: number; // 2nd harmonic contribution
  heartbeat?: number; // character vitality proxy (0..1)
}

export interface TelemetryEngineOptions {
  dt?: number;
  seed?: number;
  bufferSize?: number;
  coherenceDecay?: number; // how quickly coherence relaxes, default 0.02
}

export interface TelemetryEngine {
  readonly dt: number;
  readonly rng: Rng;
  buffer: TelemetrySample[];
  t: number;
  step(character?: { vitality?: number; harmony?: number }): TelemetrySample;
  sample(offset?: number): TelemetrySample | undefined;
  run(steps: number, character?: { vitality?: number; harmony?: number }): TelemetrySample[];
  reset(): void;
}

export function createTelemetryEngine(opts: TelemetryEngineOptions = {}): TelemetryEngine {
  const dt = opts.dt ?? 1;
  const seed = opts.seed ?? 1;
  const bufferSize = opts.bufferSize ?? 120;
  const rng = makeRng(seed);
  const coherenceRng = mulberry32((seed + 13) >>> 0);

  let t = 0;
  let coherence = 0.72 + rng() * 0.2;
  const buffer: TelemetrySample[] = [];

  function push(s: TelemetrySample): void {
    buffer.push(s);
    if (buffer.length > bufferSize) buffer.shift();
  }

  function step(character?: { vitality?: number; harmony?: number }): TelemetrySample {
    const wave = sampleOscillator(t, {
      frequency: SCHUMANN_HZ,
      amplitude: 1,
      noise: 0.12,
      rng,
    });
    const harmonic = sampleOscillator(t, {
      frequency: SCHUMANN_HZ * 2,
      amplitude: 0.35,
      phase: 0.6,
      noise: 0.05,
      rng,
    });
    // Coherence relaxes toward the character harmony baseline with noise
    const target = 0.5 + (character?.harmony ?? 0) * 0.5;
    coherence += (target - coherence) * (opts.coherenceDecay ?? 0.02);
    coherence += (coherenceRng() - 0.5) * 0.02;
    coherence = Math.min(1, Math.max(0, coherence));
    const entropy = 1 - coherence;
    const vitality = Math.min(1, Math.max(0, character?.vitality ?? 0.6));

    const sample: TelemetrySample = {
      t,
      schumann: wave,
      coherence,
      entropy,
      harmonic,
      heartbeat: vitality * (0.75 + 0.25 * Math.abs(wave)),
    };
    push(sample);
    t += dt;
    return sample;
  }

  return {
    dt,
    rng,
    buffer,
    get t() {
      return t;
    },
    step,
    sample(offset = -1) {
      if (offset === -1) return buffer[buffer.length - 1];
      return buffer[buffer.length - 1 - Math.abs(offset)];
    },
    run(steps, character) {
      for (let i = 0; i < steps; i += 1) step(character);
      return [...buffer];
    },
    reset() {
      t = 0;
      coherence = 0.72 + rng() * 0.2;
      buffer.length = 0;
    },
  };
}

/** Rolling average coherence over the current buffer. */
export function averageCoherence(engine: TelemetryEngine): number {
  if (engine.buffer.length === 0) return 0;
  const sum = engine.buffer.reduce((acc, s) => acc + s.coherence, 0);
  return sum / engine.buffer.length;
}
