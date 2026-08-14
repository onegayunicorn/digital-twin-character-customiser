import { describe, it, expect } from "vitest";
import { createVanillaCustomizerStore } from "@/stores/useCustomizerStore";
import { parseAIPrompt } from "@/utils/aiPromptRouter";
import {
  calculateStatModifiers,
  validateLifestyleBudget,
} from "@/utils/statCalculators";
import { LIFESTYLE_TOTAL_HOURS } from "@dt-core/types";

/**
 * Integration test — the AI chat pipeline: prompt → router → store → stats.
 */
describe("customizer integration (prompt → store → stats)", () => {
  it("applies an AI prompt through the store and yields valid, boosted stats", () => {
    const store = createVanillaCustomizerStore();

    const { mutator, logs } = parseAIPrompt(
      "make character an alpha criminal with a square jaw and wide nose",
    );
    expect(logs.length).toBeGreaterThanOrEqual(3);

    store.getState().updateAttributes(mutator);
    const attrs = store.getState().activeCharacter;

    // Router mutations landed
    expect(attrs.features.jaw.x).toBe(0.9);
    expect(attrs.features.nose.x).toBe(0.8);
    expect(attrs.lifestyle.illegalWork).toBe(8);

    // Budget remains valid after mutation
    const validation = validateLifestyleBudget(attrs.lifestyle);
    expect(validation.valid).toBe(true);

    // Criminal lifestyle produces strong stealth/shooting modifiers
    const stats = calculateStatModifiers(attrs.lifestyle);
    expect(stats.stealth).toBeGreaterThan(0.6);
    expect(stats.shooting).toBeGreaterThan(0.6);
  });

  it("keeps the 24h invariant across every router profile", () => {
    const store = createVanillaCustomizerStore();
    const prompts = ["athletic fighter", "criminal heist", "business executive", "social party"];
    for (const p of prompts) {
      const { mutator } = parseAIPrompt(p);
      store.getState().updateAttributes(mutator);
      const b = store.getState().activeCharacter.lifestyle;
      const sum = b.sleeping + b.friends + b.sports + b.legalWork + b.illegalWork;
      expect(sum).toBeCloseTo(LIFESTYLE_TOTAL_HOURS, 5);
    }
  });

  it("saved characters round-trip through loadCharacter with stats intact", () => {
    const store = createVanillaCustomizerStore();
    store.getState().updateAttributes((s) => {
      s.resemblance = 0.85;
      s.features.nose.x = 0.7;
    });
    store.getState().saveCurrentCharacter("RoundTrip_Test");
    const id = store.getState().savedRegistry[0]!.id;

    store.getState().reset();
    store.getState().loadCharacter(id);

    const attrs = store.getState().activeCharacter;
    expect(attrs.resemblance).toBe(0.85);
    expect(attrs.features.nose.x).toBe(0.7);
    const stats = calculateStatModifiers(attrs.lifestyle);
    expect(Object.keys(stats)).toHaveLength(7);
  });
});
