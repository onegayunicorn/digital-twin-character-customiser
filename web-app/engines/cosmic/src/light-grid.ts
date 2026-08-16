import { clamp01 } from "./types";

export class LightGrid {
  private illumination = 0.66;
  private shadowAlignment = 0.31;
  private photonDensity = 0.58;

  step(tick: number) {
    const wave = 0.5 + 0.5 * Math.sin(tick * 0.21);
    this.illumination = clamp01(this.illumination * 0.96 + wave * 0.035);
    this.shadowAlignment = clamp01(this.shadowAlignment * 0.97 + (1 - wave) * 0.025);
    this.photonDensity = clamp01(this.illumination * 0.72 + (1 - this.shadowAlignment) * 0.19);
    return this.snapshot();
  }

  snapshot() {
    return { illumination: this.illumination, shadowAlignment: this.shadowAlignment, photonDensity: this.photonDensity };
  }
}
