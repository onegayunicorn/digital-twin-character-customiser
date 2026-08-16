import { clamp01 } from "./types";

export class ResonanceMesh {
  private readonly nodeCount: number;
  private pulses: number[];

  constructor(nodeCount = 12) {
    this.nodeCount = Math.min(64, Math.max(1, Math.floor(nodeCount)));
    this.pulses = Array.from({ length: this.nodeCount }, (_, index) => 0.24 + (index % 5) * 0.07);
  }

  step(tick: number) {
    this.pulses = this.pulses.map((pulse, index) => clamp01(pulse * 0.91 + Math.abs(Math.sin(tick * 0.16 + index * 0.43)) * 0.045));
    const averagePulse = this.pulses.reduce((sum, value) => sum + value, 0) / this.nodeCount;
    const activeNodes = this.pulses.filter((pulse) => pulse > 0.28).length;
    return { activeNodes, averagePulse, propagation: clamp01(averagePulse * 1.24) };
  }
}
