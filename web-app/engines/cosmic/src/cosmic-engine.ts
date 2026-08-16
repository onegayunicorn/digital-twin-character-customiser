import { EquilibriumLattice } from "./lattice";
import { LightGrid } from "./light-grid";
import { ResonanceMesh } from "./resonance-mesh";
import { VoidField } from "./void-field";
import { COSMIC_BOUNDARY, clamp01, type CosmicConfig, type CosmicSnapshot } from "./types";

export class CosmicEngine {
  private readonly lattice: EquilibriumLattice;
  private readonly lightGrid: LightGrid;
  private readonly mesh: ResonanceMesh;
  private readonly voidField: VoidField;
  private readonly energyCap = 0.86;
  private tick = 0;

  constructor(config: CosmicConfig = {}) {
    const seed = config.seed ?? 441;
    this.lattice = new EquilibriumLattice(seed);
    this.lightGrid = new LightGrid();
    this.mesh = new ResonanceMesh(config.nodeCount ?? 12);
    this.voidField = new VoidField();
  }

  step(): CosmicSnapshot {
    this.tick += 1;
    const lattice = this.lattice.step(this.tick);
    const lightGrid = this.lightGrid.step(this.tick);
    const resonanceMesh = this.mesh.step(this.tick);
    const voidField = this.voidField.step(this.tick);
    const normalizedEnergy = clamp01((lattice.displacement + lightGrid.photonDensity + resonanceMesh.propagation + voidField.pressureIndex) / 4);
    const safety = normalizedEnergy > this.energyCap ? "reset-after-cap" : "within-cap";
    return { status: "SIMULATED", tick: this.tick, lattice, lightGrid, resonanceMesh, voidField, safety, boundary: COSMIC_BOUNDARY };
  }
}
