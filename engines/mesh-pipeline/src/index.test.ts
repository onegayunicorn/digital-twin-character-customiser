import { describe, it, expect } from "vitest";
import {
  HERITAGE_VERTEX_SHADER,
  HERITAGE_FRAGMENT_SHADER,
  buildUniformValues,
  defaultHeritageUniforms,
  applyMorphTargets,
  writeMorphInfluences,
  sculptIntensity,
  MORPH_KEYS,
} from "./index";
import { createDefaultAttributes } from "@dt-core/types";

describe("heritage shader", () => {
  it("provides vertex + fragment source referencing the parent skin uniforms", () => {
    expect(HERITAGE_VERTEX_SHADER).toContain("projectionMatrix * modelViewMatrix");
    expect(HERITAGE_FRAGMENT_SHADER).toContain("tMotherSkin");
    expect(HERITAGE_FRAGMENT_SHADER).toContain("tFatherSkin");
    expect(HERITAGE_FRAGMENT_SHADER).toContain("mix(motherTex, fatherTex, skinTone)");
  });

  it("defaults uniforms to neutral blend", () => {
    const u = defaultHeritageUniforms();
    expect(u.skinTone).toBe(0.5);
    expect(u.resemblance).toBe(0.5);
    expect(u.tMotherSkin).toBeNull();
  });

  it("builds uniforms from store attributes", () => {
    const attrs = createDefaultAttributes();
    attrs.skinTone = 0.85;
    const u = buildUniformValues(attrs, "mom-tex", "dad-tex");
    expect(u.skinTone).toBe(0.85);
    expect(u.tMotherSkin).toBe("mom-tex");
    expect(u.tFatherSkin).toBe("dad-tex");
  });
});

describe("morph target mapping", () => {
  it("splits positive/negative nose coordinates into wide/narrow + long/short", () => {
    const attrs = createDefaultAttributes();
    attrs.features.nose.x = 0.8;
    attrs.features.nose.y = -0.4;
    const map = applyMorphTargets(attrs.features);
    expect(map.Nose_Wide).toBe(0.8);
    expect(map.Nose_Narrow).toBe(0);
    expect(map.Nose_Long).toBe(0);
    expect(map.Nose_Short).toBe(0.4);
  });

  it("maps jaw square/round and other axes", () => {
    const attrs = createDefaultAttributes();
    attrs.features.jaw.x = -0.6;
    attrs.features.brows.y = 0.7;
    const map = applyMorphTargets(attrs.features);
    expect(map.Jaw_Round).toBe(0.6);
    expect(map.Jaw_Square).toBe(0);
    expect(map.Brow_Heavy).toBe(0.7);
  });

  it("writes influences into a dictionary-indexed array", () => {
    const dictionary: Record<string, number> = {};
    MORPH_KEYS.forEach((k, i) => {
      dictionary[k] = i;
    });
    const influences = new Array(MORPH_KEYS.length).fill(0);
    writeMorphInfluences(dictionary, influences, { Nose_Wide: 0.5, Jaw_Square: 1 });
    expect(influences[dictionary.Nose_Wide!]).toBe(0.5);
    expect(influences[dictionary.Jaw_Square!]).toBe(1);
    expect(influences[dictionary.Nose_Long!]).toBe(0);
  });

  it("is a no-op on missing rig data", () => {
    expect(() => writeMorphInfluences(undefined, undefined, { Nose_Wide: 0.5 })).not.toThrow();
  });

  it("sculptIntensity stays in 0..1", () => {
    const attrs = createDefaultAttributes();
    expect(sculptIntensity(attrs.features)).toBe(0);
    attrs.features.jaw.x = 0.9;
    attrs.features.nose.y = -0.8;
    const v = sculptIntensity(attrs.features);
    expect(v).toBeGreaterThan(0);
    expect(v).toBeLessThanOrEqual(1);
  });
});
