import { describe, it, expect } from "vitest";
import {
  clampAxis,
  clampPoint,
  gridDistance,
  pixelToGrid,
  gridToPixel,
  lerpPoint,
  blendFeatureMatrix,
  quantisePoint,
} from "./index";
import { createDefaultAttributes, FEATURE_MAX, FEATURE_MIN } from "@dt-core/types";

describe("clamping", () => {
  it("clamps into -1..1", () => {
    expect(clampAxis(1.7)).toBe(1);
    expect(clampAxis(-2)).toBe(-1);
    expect(clampAxis(0.4)).toBe(0.4);
    expect(clampPoint({ x: 5, y: -9 })).toEqual({ x: FEATURE_MAX, y: FEATURE_MIN });
  });
});

describe("coordinate conversion", () => {
  it("pixelToGrid maps corners to the matrix corners", () => {
    expect(pixelToGrid(0, 0, 200, 200)).toEqual({ x: -1, y: -1 });
    expect(pixelToGrid(200, 200, 200, 200)).toEqual({ x: 1, y: 1 });
    expect(pixelToGrid(100, 100, 200, 200)).toEqual({ x: 0, y: 0 });
  });

  it("gridToPixel inverts pixelToGrid", () => {
    const p = pixelToGrid(150, 60, 300, 300);
    const back = gridToPixel(p, 300, 300);
    expect(back.px).toBeCloseTo(150, 1);
    expect(back.py).toBeCloseTo(60, 1);
  });
});

describe("distance and blending", () => {
  it("computes grid distance", () => {
    expect(gridDistance({ x: 0, y: 0 }, { x: 1, y: 0 })).toBe(1);
  });

  it("lerpPoint interpolates", () => {
    expect(lerpPoint({ x: 0, y: 0 }, { x: 1, y: 2 }, 0.5)).toEqual({ x: 0.5, y: 1 });
  });

  it("blendFeatureMatrix at resemblance 0 is mother, at 1 is father", () => {
    const mother = createDefaultAttributes().features;
    const father = createDefaultAttributes().features;
    father.nose.x = 0.8;
    father.jaw.x = -0.6;
    father.lips = 0.5;
    expect(blendFeatureMatrix(mother, father, 0).nose.x).toBe(0);
    expect(blendFeatureMatrix(mother, father, 1).nose.x).toBe(0.8);
    expect(blendFeatureMatrix(mother, father, 1).lips).toBe(0.5);
    const mid = blendFeatureMatrix(mother, father, 0.5);
    expect(mid.nose.x).toBeCloseTo(0.4, 5);
    expect(mid.jaw.x).toBeCloseTo(-0.3, 5);
  });

  it("quantisePoint snaps to the nearest step", () => {
    expect(quantisePoint({ x: 0.63, y: -0.12 })).toEqual({ x: 0.65, y: -0.1 });
  });
});
