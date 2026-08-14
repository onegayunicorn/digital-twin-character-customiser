/**
 * HeritageShaderMaterial — factory for the custom GLSL shader that blends
 * mother/father skin maps on the GPU using skinTone + resemblance uniforms.
 * Shader sources live in @dt-engine/mesh-pipeline.
 */
import * as THREE from "three";
import {
  HERITAGE_FRAGMENT_SHADER,
  HERITAGE_VERTEX_SHADER,
  defaultHeritageUniforms,
  type HeritageShaderUniforms,
} from "@dt-engine/mesh-pipeline";

export function createHeritageMaterial(
  skinTone = 0.5,
  resemblance = 0.5,
): THREE.ShaderMaterial {
  const uniforms: Record<string, THREE.IUniform> = {
    tMotherSkin: { value: null },
    tFatherSkin: { value: null },
    skinTone: { value: skinTone },
    resemblance: { value: resemblance },
  };
  return new THREE.ShaderMaterial({
    uniforms,
    vertexShader: HERITAGE_VERTEX_SHADER,
    fragmentShader: HERITAGE_FRAGMENT_SHADER,
    side: THREE.DoubleSide,
  });
}

/** Update shader uniforms from customizer state (returns the uniform map). */
export function syncHeritageUniforms(
  material: THREE.ShaderMaterial | null,
  values: Partial<HeritageShaderUniforms>,
): void {
  if (!material) return;
  const u = material.uniforms;
  if (values.skinTone !== undefined) u.skinTone.value = values.skinTone;
  if (values.resemblance !== undefined) u.resemblance.value = values.resemblance;
  if (values.tMotherSkin !== undefined) u.tMotherSkin.value = values.tMotherSkin;
  if (values.tFatherSkin !== undefined) u.tFatherSkin.value = values.tFatherSkin;
  material.needsUpdate = true;
}

export { defaultHeritageUniforms };
export type { HeritageShaderUniforms };
