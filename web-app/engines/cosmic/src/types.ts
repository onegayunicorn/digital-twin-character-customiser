export type CosmicConfig = {
  seed?: number;
  latticeSize?: number;
  nodeCount?: number;
};

export type CosmicSnapshot = {
  status: "SIMULATED";
  tick: number;
  lattice: { density: number; displacement: number; restoringForce: number };
  lightGrid: { illumination: number; shadowAlignment: number; photonDensity: number };
  resonanceMesh: { activeNodes: number; averagePulse: number; propagation: number };
  voidField: { pressureIndex: number; gradient: number; entropyIndex: number };
  safety: "within-cap" | "reset-after-cap";
  boundary: string;
};

export const COSMIC_BOUNDARY = "Dimensionless visual systems only; no physical field, gravity, photon, quantum, portal, financial, or hardware claim.";

export const clamp01 = (value: number) => Math.min(1, Math.max(0, value));
