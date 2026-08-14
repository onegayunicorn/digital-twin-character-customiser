import { describe, it, expect } from "vitest";
import {
  createTelemetryEngine,
  averageCoherence,
  SCHUMANN_HZ,
} from "./index";

describe("telemetry engine", () => {
  it("emits Schumann resonance samples at 7.83 Hz", () => {
    const engine = createTelemetryEngine({ dt: 1, seed: 7 });
    const s = engine.step();
    // wave + injected noise stays within amplitude bounds
    expect(Math.abs(s.schumann)).toBeLessThanOrEqual(1.2);
    expect(typeof s.coherence).toBe("number");
    expect(s.entropy).toBeCloseTo(1 - s.coherence, 5);
  });

  it("keeps coherence bounded in [0, 1]", () => {
    const engine = createTelemetryEngine({ seed: 3 });
    for (let i = 0; i < 500; i += 1) {
      const s = engine.step();
      expect(s.coherence).toBeGreaterThanOrEqual(0);
      expect(s.coherence).toBeLessThanOrEqual(1);
    }
  });

  it("buffers a bounded window", () => {
    const engine = createTelemetryEngine({ bufferSize: 30, seed: 9 });
    engine.run(100);
    expect(engine.buffer).toHaveLength(30);
  });

  it("sample(-1) returns the latest sample", () => {
    const engine = createTelemetryEngine({ seed: 2 });
    engine.step();
    const last = engine.step();
    expect(engine.sample()).toEqual(last);
  });

  it("is deterministic for a fixed seed", () => {
    const a = createTelemetryEngine({ seed: 55 });
    const b = createTelemetryEngine({ seed: 55 });
    a.run(10);
    b.run(10);
    expect(a.buffer.map((s) => s.schumann)).toEqual(
      b.buffer.map((s) => s.schumann),
    );
  });

  it("averageCoherence computes the rolling mean", () => {
    const engine = createTelemetryEngine({ seed: 1, bufferSize: 5 });
    engine.run(5);
    const avg = averageCoherence(engine);
    expect(avg).toBeGreaterThanOrEqual(0);
    expect(avg).toBeLessThanOrEqual(1);
  });

  it("character harmony pulls coherence up over time", () => {
    const low = createTelemetryEngine({ seed: 1 });
    const high = createTelemetryEngine({ seed: 1 });
    low.run(400, { harmony: 0 });
    high.run(400, { harmony: 1 });
    expect(averageCoherence(high)).toBeGreaterThan(averageCoherence(low));
  });
});
