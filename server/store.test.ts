import { describe, it, expect } from "vitest";
import { createVanillaCustomizerStore } from "@dt-core/state";
import { parseAIPrompt } from "@dt-core/ai-router";
import { validateLifestyleBudget } from "@dt-engine/lifestyle";

/**
 * Server-side store suite — exercises the customizer state engine through the
 * server package (spec parity: server/store.test.ts).
 */
describe("server store actions", () => {
  it("defaults to a Male character with a valid budget", () => {
    const store = createVanillaCustomizerStore();
    const s = store.getState();
    expect(s.activeGender).toBe("Male");
    expect(validateLifestyleBudget(s.activeCharacter.lifestyle).valid).toBe(true);
  });

  it("updateAttributes mutates immutably", () => {
    const store = createVanillaCustomizerStore();
    const before = store.getState().activeCharacter;
    store.getState().updateAttributes((s) => {
      s.resemblance = 0.85;
      s.features.jaw.x = 0.9;
    });
    const after = store.getState().activeCharacter;
    expect(after.resemblance).toBe(0.85);
    expect(after.features.jaw.x).toBe(0.9);
    expect(before.resemblance).toBe(0.5);
    expect(after).not.toBe(before);
  });

  it("AI router output flows through the store cleanly", () => {
    const store = createVanillaCustomizerStore();
    const { mutator } = parseAIPrompt("criminal heist with wide nose");
    store.getState().updateAttributes(mutator);
    const attrs = store.getState().activeCharacter;
    expect(attrs.lifestyle.illegalWork).toBe(8);
    expect(attrs.features.nose.x).toBe(0.8);
    expect(validateLifestyleBudget(attrs.lifestyle).valid).toBe(true);
  });

  it("save/load round-trips profiles", () => {
    const store = createVanillaCustomizerStore();
    store.getState().saveCurrentCharacter("Server_Twin");
    const id = store.getState().savedRegistry[0]!.id;
    store.getState().updateAttributes((s) => {
      s.skinTone = 0.4;
    });
    store.getState().loadCharacter(id);
    expect(store.getState().activeCharacter.skinTone).toBe(0.5);
  });
});
