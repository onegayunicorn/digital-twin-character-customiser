import { clamp01 } from "./types";

export class VoidField {
  private pressureIndex = 0.28;
  private gradient = 0.44;
  private entropyIndex = 0.56;

  step(tick: number) {
    const drift = 0.5 + 0.5 * Math.cos(tick * 0.13);
    this.gradient = clamp01(this.gradient * 0.95 + drift * 0.035);
    this.pressureIndex = clamp01(this.pressureIndex * 0.97 + this.gradient * 0.03);
    this.entropyIndex = clamp01(this.entropyIndex * 0.985 + (1 - this.pressureIndex) * 0.018);
    return { pressureIndex: this.pressureIndex, gradient: this.gradient, entropyIndex: this.entropyIndex };
  }
}
