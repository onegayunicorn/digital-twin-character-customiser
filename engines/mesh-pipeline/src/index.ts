/**
 * Aether Core engine — Mesh Pipeline.
 *
 * Bridges the Zustand state engine into the WebGL mesh pipeline:
 *   1. A custom GLSL vertex/fragment heritage shader that blends mother/father
 *      skin maps on the GPU using the skinTone + resemblance uniforms.
 *   2. A morph target map that translates dual-axis feature coordinates into
 *      named morph influences (Nose_Wide, Jaw_Square, …) on a SkinnedMesh.
 */
import {
  FEATURE_MAX,
  type CharacterAttributes,
  type FeatureMatrix,
  type Vector2D,
} from "@dt-core/types";

// ── Heritage GLSL shader (from the Digital Twin spec) ──────────────────────

export interface HeritageShaderUniforms {
  tMotherSkin: unknown | null;
  tFatherSkin: unknown | null;
  skinTone: number; // 0.0 = Mother texture, 1.0 = Father texture
  resemblance: number; // used for potential normal-map blending overrides
}

export const HERITAGE_VERTEX_SHADER = `
varying vec2 vUv;
varying vec3 vNormal;
void main() {
  vUv = uv;
  vNormal = normalize(normalMatrix * normal);
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
`;

export const HERITAGE_FRAGMENT_SHADER = `
uniform sampler2D tMotherSkin;
uniform sampler2D tFatherSkin;
uniform float skinTone;
uniform float resemblance;
varying vec2 vUv;
varying vec3 vNormal;
void main() {
  // Sample both parent textures maps simultaneously
  vec4 motherTex = texture2D(tMotherSkin, vUv);
  vec4 fatherTex = texture2D(tFatherSkin, vUv);
  // Calculate linear interpolation on the GPU
  vec4 finalColor = mix(motherTex, fatherTex, skinTone);
  // Resemblance modulates a subtle normal/detail blend
  finalColor.rgb = mix(finalColor.rgb, fatherTex.rgb, resemblance * 0.1);
  // Add very simple baseline lighting calculus to retain mesh curves definition
  float lighting = max(dot(vNormal, normalize(vec3(0.5, 1.0, 0.5))), 0.2);
  gl_FragColor = vec4(finalColor.rgb * (lighting + 0.3), finalColor.a);
}
`;

export function defaultHeritageUniforms(): HeritageShaderUniforms {
  return {
    tMotherSkin: null,
    tFatherSkin: null,
    skinTone: 0.5,
    resemblance: 0.5,
  };
}

/** Derive uniform values straight from the customizer store state. */
export function buildUniformValues(
  attributes: Pick<CharacterAttributes, "skinTone" | "resemblance">,
  motherTexture?: unknown,
  fatherTexture?: unknown,
): HeritageShaderUniforms {
  return {
    tMotherSkin: motherTexture ?? null,
    tFatherSkin: fatherTexture ?? null,
    skinTone: attributes.skinTone,
    resemblance: attributes.resemblance,
  };
}

// ── Morph target mapping ────────────────────────────────────────────────────

/** Morph key names the rig exposes (archive GLB naming convention). */
export const MORPH_KEYS = [
  "Nose_Wide",
  "Nose_Narrow",
  "Nose_Long",
  "Nose_Short",
  "Jaw_Square",
  "Jaw_Round",
  "Brow_Heavy",
  "Eye_Size",
  "Cheekbone_Height",
  "Chin_Strong",
  "Lip_Full",
  "Neck_Thick",
] as const;

export type MorphKey = (typeof MORPH_KEYS)[number];
export type MorphInfluenceMap = Partial<Record<MorphKey, number>>;

/**
 * Translate dual-axis feature coordinates into morph influences.
 * Positive axis values drive the positive morph key; negative values drive
 * the negative counterpart (clamped to 0..1 GPU metric).
 */
export function applyMorphTargets(
  features: Pick<
    FeatureMatrix,
    | "nose"
    | "jaw"
    | "brows"
    | "eyes"
    | "cheekbones"
    | "chinShape"
    | "lips"
    | "neckWidth"
  >,
): MorphInfluenceMap {
  const out: MorphInfluenceMap = {};
  const positive = (v: number) => Math.min(1, Math.max(0, v));
  const negative = (v: number) => Math.min(1, Math.max(0, -v));

  const nose: Vector2D = features.nose;
  out.Nose_Wide = positive(nose.x);
  out.Nose_Narrow = negative(nose.x);
  out.Nose_Long = positive(nose.y);
  out.Nose_Short = negative(nose.y);

  const jaw: Vector2D = features.jaw;
  out.Jaw_Square = positive(jaw.x);
  out.Jaw_Round = negative(jaw.x);

  out.Brow_Heavy = positive(features.brows.y);
  out.Eye_Size = positive(features.eyes.y);
  out.Cheekbone_Height = positive(features.cheekbones.y);
  out.Chin_Strong = positive(features.chinShape.x);
  out.Lip_Full = positive(features.lips);
  out.Neck_Thick = positive(features.neckWidth);

  return out;
}

/**
 * Apply the influences onto a THREE-like morph target dictionary object.
 * `dictionary` maps morph names → index; `influences` is the float array.
 */
export function writeMorphInfluences(
  dictionary: Record<string, number> | undefined,
  influences: number[] | undefined,
  map: MorphInfluenceMap,
): void {
  if (!dictionary || !influences) return;
  for (const [key, value] of Object.entries(map)) {
    const idx = dictionary[key];
    if (idx !== undefined && influences[idx] !== undefined) {
      influences[idx] = Math.min(1, Math.max(0, value ?? 0));
    }
  }
}

/** Feature magnitude metric (0..1) — "how sculpted" a character is. */
export function sculptIntensity(features: FeatureMatrix): number {
  const vectors = [
    features.brows,
    features.eyes,
    features.nose,
    features.noseProfile,
    features.noseTip,
    features.cheekbones,
    features.jaw,
    features.chinProfile,
    features.chinShape,
  ];
  const vectorSum = vectors.reduce(
    (acc, v) => acc + Math.abs(v.x) + Math.abs(v.y),
    0,
  );
  const scalarSum =
    Math.abs(features.cheeks) +
    Math.abs(features.lips) +
    Math.abs(features.neckWidth);
  const total = vectorSum + scalarSum;
  // 21 axes max (9 vectors × 2 + 3 scalars)
  return Math.min(1, total / 21 / FEATURE_MAX);
}
