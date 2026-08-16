import { clamp01 } from "./types";

export class EquilibriumLattice {
  private density = 0.52;
  private displacement = 0.18;
  private restoringForce = 0.42;
  private readonly seed: number;

  constructor(seed = 441) {
    this.seed = seed;
  }

  step(tick: number): { density: number; displacement: number; restoringForce: number } {
    const drive = 0.025 * (0.5 + 0.5 * Math.sin((tick + this.seed) * 0.17));
    this.displacement = clamp01(this.displacement * 0.94 + drive);
    this.restoringForce = clamp01(this.displacement * 0.82 + this.density * 0.08);
    this.density = clamp01(this.density * 0.992 + this.restoringForce * 0.012 - this.displacement * 0.008);
    return this.snapshot();
  }

  snapshot() {
    return { density: this.density, displacement: this.displacement, restoringForce: this.restoringForce };
  }
}
