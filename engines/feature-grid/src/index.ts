/**
 * Aether Core engine — FeatureGrid2D.
 *
 * Pure math for the GTA V-inspired dual-axis facial feature matrix. All
 * coordinates live in the -1.00..1.00 range; helpers convert pointer/UI
 * coordinates into matrix coordinates, clamp, measure distance, and blend
 * parent feature matrices by a resemblance weight.
 */
import {
  FEATURE_MAX,
  FEATURE_MIN,
  type FeatureMatrix,
  type Vector2D,
} from "@dt-core/types";

export function clampAxis(v: number): number {
  return Math.min(FEATURE_MAX, Math.max(FEATURE_MIN, v));
}

export function clampPoint(p: Vector2D): Vector2D {
  return { x: clampAxis(p.x), y: clampAxis(p.y) };
}

export function gridDistance(a: Vector2D, b: Vector2D): number {
  return Math.hypot(a.x - b.x, a.y - b.y);
}

export function midpoint(a: Vector2D, b: Vector2D): Vector2D {
  return { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
}

/** Normalized pixel → matrix coordinate for a square grid element. */
export function pixelToGrid(
  px: number,
  py: number,
  width: number,
  height: number,
): Vector2D {
  const nx = width > 0 ? px / width : 0;
  const ny = height > 0 ? py / height : 0;
  return {
    x: clampAxis(nx * 2 - 1),
    y: clampAxis(ny * 2 - 1),
  };
}

/** Matrix coordinate → pixel coordinate (inverse of pixelToGrid). */
export function gridToPixel(
  p: Vector2D,
  width: number,
  height: number,
): { px: number; py: number } {
  return {
    px: ((clampAxis(p.x) + 1) / 2) * width,
    py: ((clampAxis(p.y) + 1) / 2) * height,
  };
}

export function isOrigin(p: Vector2D, epsilon = 0.02): boolean {
  return gridDistance(p, { x: 0, y: 0 }) < epsilon;
}

/** Linearly interpolate two points by t (0 = a, 1 = b). */
export function lerpPoint(a: Vector2D, b: Vector2D, t: number): Vector2D {
  return { x: a.x + (b.x - a.x) * t, y: a.y + (b.y - a.y) * t };
}

export const EMPTY_POINT: Vector2D = { x: 0, y: 0 };

/**
 * Blend two parent feature matrices by resemblance (0 = mother, 1 = father).
 * Vectors lerp per-axis; scalars lerp linearly.
 */
export function blendFeatureMatrix(
  mother: FeatureMatrix,
  father: FeatureMatrix,
  resemblance: number,
): FeatureMatrix {
  const t = clampAxis(resemblance);
  const blend = (a: Vector2D, b: Vector2D): Vector2D => lerpPoint(a, b, t);
  const scalars = (a: number, b: number): number => a + (b - a) * t;
  return {
    brows: blend(mother.brows, father.brows),
    eyes: blend(mother.eyes, father.eyes),
    nose: blend(mother.nose, father.nose),
    noseProfile: blend(mother.noseProfile, father.noseProfile),
    noseTip: blend(mother.noseTip, father.noseTip),
    cheekbones: blend(mother.cheekbones, father.cheekbones),
    cheeks: scalars(mother.cheeks, father.cheeks),
    lips: scalars(mother.lips, father.lips),
    jaw: blend(mother.jaw, father.jaw),
    chinProfile: blend(mother.chinProfile, father.chinProfile),
    chinShape: blend(mother.chinShape, father.chinShape),
    neckWidth: scalars(mother.neckWidth, father.neckWidth),
  };
}

/** Random but deterministic matrix point from a uniform rng. */
export function randomGridPoint(
  rng: () => number,
  magnitude = 1,
): Vector2D {
  return clampPoint({
    x: (rng() * 2 - 1) * magnitude,
    y: (rng() * 2 - 1) * magnitude,
  });
}

/** Quantise a point to a coarse grid step (e.g. 0.05) for slider snapping. */
export function quantisePoint(p: Vector2D, step = 0.05): Vector2D {
  return {
    x: clampAxis(Math.round(p.x / step) * step),
    y: clampAxis(Math.round(p.y / step) * step),
  };
}
