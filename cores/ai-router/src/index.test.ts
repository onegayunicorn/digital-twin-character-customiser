import { describe, it, expect } from "vitest";
import { parseAIPrompt, clampFeature } from "./index";
import { createDefaultAttributes, LIFESTYLE_TOTAL_HOURS } from "@dt-core/types";

function apply(prompt: string) {
  const { mutator, logs } = parseAIPrompt(prompt);
  const state = createDefaultAttributes();
  mutator(state);
  return { state, logs };
}

describe("parseAIPrompt — heritage heuristics", () => {
  it("weights resemblance toward the mother when asked to look like mom", () => {
    const { state, logs } = apply("make them look like their mother");
    expect(state.resemblance).toBe(0.15);
    expect(logs.some((l) => l.includes("Maternal"))).toBe(true);
  });

  it("weights resemblance toward the father", () => {
    const { state } = apply("resemblance dad");
    expect(state.resemblance).toBe(0.85);
  });

  it("shifts skin tone for pale and dark requests", () => {
    expect(apply("make skin paler").state.skinTone).toBe(0.2);
    expect(apply("darker skin").state.skinTone).toBe(0.85);
  });
});

describe("parseAIPrompt — feature vector parsing", () => {
  it("maps wide nose to +0.80 on the x axis", () => {
    const { state } = apply("give them a wide nose");
    expect(state.features.nose.x).toBe(0.8);
  });

  it("maps narrow nose to -0.80", () => {
    const { state } = apply("narrow nose");
    expect(state.features.nose.x).toBe(-0.8);
  });

  it("maps long nose to +0.75 on the y axis", () => {
    const { state } = apply("long nose");
    expect(state.features.nose.y).toBe(0.75);
  });

  it("maps square alpha jaw to 0.90 both axes", () => {
    const { state } = apply("square jaw alpha");
    expect(state.features.jaw.x).toBe(0.9);
    expect(state.features.jaw.y).toBe(0.9);
  });

  it("handles combined prompts: criminal + jaw + nose", () => {
    const { state, logs } = apply("make character an alpha criminal with a square jaw and wide nose");
    expect(state.features.jaw.x).toBe(0.9);
    expect(state.features.nose.x).toBe(0.8);
    expect(state.lifestyle.illegalWork).toBe(8);
    expect(logs.length).toBeGreaterThanOrEqual(3);
  });
});

describe("parseAIPrompt — lifestyle budgets", () => {
  it("injects the athletic profile and keeps the 24h invariant", () => {
    const { state } = apply("athletic fighter strong");
    expect(state.lifestyle.sports).toBe(8);
    expect(state.lifestyle.sleeping).toBe(6);
    const sum =
      state.lifestyle.sleeping +
      state.lifestyle.friends +
      state.lifestyle.sports +
      state.lifestyle.legalWork +
      state.lifestyle.illegalWork;
    expect(sum).toBe(LIFESTYLE_TOTAL_HOURS);
  });

  it("injects the criminal profile", () => {
    const { state } = apply("criminal heist hustler");
    expect(state.lifestyle.illegalWork).toBe(8);
    expect(state.lifestyle.sleeping).toBe(5);
  });

  it("injects the business profile", () => {
    const { state } = apply("business executive");
    expect(state.lifestyle.legalWork).toBe(8);
  });
});

describe("parseAIPrompt — fallbacks and bounds", () => {
  it("returns a warning log when no rules match", () => {
    const { logs } = apply("zorp the florbinator");
    expect(logs.some((l) => l.includes("no matching parameters"))).toBe(true);
  });

  it("clamps mutated feature coordinates into -1..1", () => {
    const { state } = apply("extremely wide nose and extremely square jaw");
    expect(state.features.nose.x).toBeLessThanOrEqual(1);
    expect(state.features.jaw.x).toBeLessThanOrEqual(1);
    expect(clampFeature(1.7)).toBe(1);
    expect(clampFeature(-2.3)).toBe(-1);
  });

  it("never leaves a broken 24h budget after mutation", () => {
    const prompts = [
      "sleepy tired",
      "social party",
      "balanced",
      "square jaw thick brows big eyes high cheekbones full lips thick neck",
    ];
    for (const p of prompts) {
      const { state } = apply(p);
      const sum =
        state.lifestyle.sleeping +
        state.lifestyle.friends +
        state.lifestyle.sports +
        state.lifestyle.legalWork +
        state.lifestyle.illegalWork;
      expect(sum, `budget broken for prompt: ${p}`).toBe(LIFESTYLE_TOTAL_HOURS);
    }
  });

  it("maps hair color words to slots", () => {
    expect(apply("neon green hair").state.appearance.hairColor).toBe(3);
    expect(apply("black hair").state.appearance.hairColor).toBe(1);
    expect(apply("blonde hair").state.appearance.hairColor).toBe(2);
  });
});
