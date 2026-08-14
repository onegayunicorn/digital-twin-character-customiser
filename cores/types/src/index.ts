/**
 * Aether Core — shared domain types.
 *
 * Mirrors the Digital Twin Character Customizer spec payload layout
 * (GTA V-style dual-axis feature coordinates in the range -1.00..1.00).
 */

/** 2D vector with range -1.00 .. 1.00 per axis. */
export interface Vector2D {
  x: number; // Range: -1.00 to 1.00
  y: number; // Range: -1.00 to 1.00
}

/** Structural facial feature matrix (all vectors -1.00..1.00, scalars -1.00..1.00). */
export interface FeatureMatrix {
  brows: Vector2D;
  eyes: Vector2D;
  nose: Vector2D;
  noseProfile: Vector2D;
  noseTip: Vector2D;
  cheekbones: Vector2D;
  cheeks: number; // Single axis range: -1.00 to 1.00
  lips: number; // Single axis range: -1.00 to 1.00
  jaw: Vector2D;
  chinProfile: Vector2D;
  chinShape: Vector2D;
  neckWidth: number; // Single axis range: -1.00 to 1.00
}

/** Appearance slot configuration. */
export interface Appearance {
  hairId: number;
  hairColor: number;
  hairHighlight: number;
  eyebrowsId: number;
  eyebrowsOpacity: number;
  eyeColorId: number;
}

/** 24-hour lifestyle hour-allocation budget (sums to 24). */
export interface LifestyleAllocation {
  sleeping: number;
  friends: number;
  sports: number;
  legalWork: number;
  illegalWork: number;
}

/** Complete character attribute payload — single source of truth. */
export interface CharacterAttributes {
  motherId: number;
  fatherId: number;
  resemblance: number; // Range: 0.00 to 1.00
  skinTone: number; // Range: 0.00 to 1.00
  features: FeatureMatrix;
  appearance: Appearance;
  lifestyle: LifestyleAllocation;
}

export type Gender = "Male" | "Female";

/** Persisted character profile. */
export interface CharacterProfile {
  id: string;
  name: string;
  gender: Gender;
  attributes: CharacterAttributes;
  created: string;
}

/** Active attribute stat keys produced by the lifestyle budget. */
export type StatKey =
  | "stamina"
  | "strength"
  | "stealth"
  | "shooting"
  | "driving"
  | "lungCapacity"
  | "flying";

export type StatBlock = Record<StatKey, number>;

export const STAT_KEYS: readonly StatKey[] = [
  "stamina",
  "strength",
  "stealth",
  "shooting",
  "driving",
  "lungCapacity",
  "flying",
] as const;

export const LIFESTYLE_KEYS = [
  "sleeping",
  "friends",
  "sports",
  "legalWork",
  "illegalWork",
] as const;

export type LifestyleKey = (typeof LIFESTYLE_KEYS)[number];

/** Hard budget rules (enforced by the LifestyleBudget engine). */
export const LIFESTYLE_TOTAL_HOURS = 24;
export const LIFESTYLE_MIN_SLEEP = 4;
export const LIFESTYLE_MAX_PER_CATEGORY = 8;

/** Dual-axis matrix bounds. */
export const FEATURE_MIN = -1.0;
export const FEATURE_MAX = 1.0;

export const FEATURE_VECTOR_KEYS = [
  "brows",
  "eyes",
  "nose",
  "noseProfile",
  "noseTip",
  "cheekbones",
  "jaw",
  "chinProfile",
  "chinShape",
] as const;

export const FEATURE_SCALAR_KEYS = ["cheeks", "lips", "neckWidth"] as const;

/** Factory producing a fresh default attribute payload. */
export function createDefaultAttributes(): CharacterAttributes {
  return {
    motherId: 0,
    fatherId: 0,
    resemblance: 0.5,
    skinTone: 0.5,
    features: {
      brows: { x: 0, y: 0 },
      eyes: { x: 0, y: 0 },
      nose: { x: 0, y: 0 },
      noseProfile: { x: 0, y: 0 },
      noseTip: { x: 0, y: 0 },
      cheekbones: { x: 0, y: 0 },
      cheeks: 0,
      lips: 0,
      jaw: { x: 0, y: 0 },
      chinProfile: { x: 0, y: 0 },
      chinShape: { x: 0, y: 0 },
      neckWidth: 0,
    },
    appearance: {
      hairId: 0,
      hairColor: 0,
      hairHighlight: 0,
      eyebrowsId: 0,
      eyebrowsOpacity: 1.0,
      eyeColorId: 0,
    },
    lifestyle: {
      sleeping: 8,
      friends: 4,
      sports: 4,
      legalWork: 4,
      illegalWork: 4,
    },
  };
}

/** Default attribute payload (immutable by convention — copy before mutating). */
export const DEFAULT_ATTRIBUTES: CharacterAttributes = createDefaultAttributes();

/** Deep clone helper used by the state store for immutable updates. */
export function cloneAttributes(a: CharacterAttributes): CharacterAttributes {
  return JSON.parse(JSON.stringify(a)) as CharacterAttributes;
}
