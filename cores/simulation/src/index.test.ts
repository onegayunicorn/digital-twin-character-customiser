import { describe, it, expect } from "vitest";
import {
  SimulationEngine,
  mulberry32,
  gaussian,
  sampleOscillator,
  simulateLifestyleLifecycle,
} from "./index";
import { createDefaultAttributes, LIFESTYLE_TOTAL_HOURS } from "@dt-core/types";

describe("mulberry32 PRNG", () => {
  it("is deterministic for a fixed seed", () => {
    const a = mulberry32(42);
    const b = mulberry32(42);
    const seqA = Array.from({ length: 10 }, () => a());
    const seqB = Array.from({ length: 10 }, () => b());
    expect(seqA).toEqual(seqB);
  });

  it("produces values in [0, 1)", () => {
    const rng = mulberry32(7);
    for (let i = 0; i < 100; i += 1) {
      const v = rng();
      expect(v).toBeGreaterThanOrEqual(0);
      expect(v).toBeLessThan(1);
    }
  });

  it("gaussian is approximately standard normal", () => {
    const rng = mulberry32(1);
    let sum = 0;
    const n = 2000;
    for (let i = 0; i < n; i += 1) sum += gaussian(rng);
    const mean = sum / n;
    expect(Math.abs(mean)).toBeLessThan(0.15);
  });
});

describe("SimulationEngine", () => {
  it("runs N ticks and records time series", () => {
    const engine = new SimulationEngine({ dt: 1, maxT: 100, seed: 5 });
    const out = engine.run((t) => ({ value: Math.sin(t) }));
    expect(out).toHaveLength(100);
    expect(out[0]?.t).toBe(0);
    expect(out[99]?.t).toBe(99);
    expect(out[50]?.value).toBeCloseTo(Math.sin(50), 5);
  });

  it("respects maxT when steps would exceed it", () => {
    const engine = new SimulationEngine({ dt: 2, maxT: 10, seed: 1 });
    engine.run((t) => ({ v: t }), 1000);
    expect(engine.history).toHaveLength(5); // t = 0,2,4,6,8
  });

  it("step() records samples with monotonic time", () => {
    const engine = new SimulationEngine({ dt: 0.5 });
    engine.step({ a: 1 });
    engine.step({ a: 2 });
    expect(engine.history.map((h) => h.t)).toEqual([0, 0.5]);
  });

  it("reset clears history and time", () => {
    const engine = new SimulationEngine({ seed: 9 });
    engine.run(() => ({ v: 1 }));
    engine.reset();
    expect(engine.history).toHaveLength(0);
    expect(engine.t).toBe(0);
  });
});

describe("sampleOscillator", () => {
  it("produces a clean sine at frequency f", () => {
    const f = 7.83; // Schumann
    expect(sampleOscillator(0, { frequency: f, amplitude: 1 })).toBeCloseTo(0, 5);
    expect(sampleOscillator(1 / (4 * f), { frequency: f, amplitude: 1 })).toBeCloseTo(1, 3);
  });

  it("injects noise when requested", () => {
    const noisy = sampleOscillator(0.5, { frequency: 1, noise: 0.5, rng: mulberry32(3) });
    expect(noisy).not.toBeCloseTo(Math.sin(Math.PI), 2);
  });
});

describe("simulateLifestyleLifecycle", () => {
  it("keeps every day budget at exactly 24h", () => {
    const result = simulateLifestyleLifecycle(createDefaultAttributes(), {
      days: 20,
      seed: 11,
    });
    expect(result.days).toHaveLength(20);
    for (const day of result.days) {
      const sum =
        day.lifestyle.sleeping +
        day.lifestyle.friends +
        day.lifestyle.sports +
        day.lifestyle.legalWork +
        day.lifestyle.illegalWork;
      expect(sum).toBeCloseTo(LIFESTYLE_TOTAL_HOURS, 5);
    }
  });

  it("returns deterministic results for a fixed seed", () => {
    const a = simulateLifestyleLifecycle(createDefaultAttributes(), { days: 5, seed: 99 });
    const b = simulateLifestyleLifecycle(createDefaultAttributes(), { days: 5, seed: 99 });
    expect(a.days).toEqual(b.days);
  });

  it("computes final and best-day stats", () => {
    const result = simulateLifestyleLifecycle(createDefaultAttributes(), {
      days: 7,
      seed: 3,
      statModifier: (l) => ({
        stamina: l.sports / 8,
        strength: l.sports / 8,
        stealth: l.illegalWork / 8,
        shooting: l.legalWork / 8,
        driving: l.friends / 8,
        lungCapacity: l.sleeping / 8,
        flying: 0,
      }),
    });
    expect(result.finalStats.stamina).toBeGreaterThanOrEqual(0);
    expect(result.bestDay.day).toBeGreaterThanOrEqual(0);
  });
});
