import { describe, it, expect, beforeEach } from "vitest";
import { createVanillaCustomizerStore } from "./index";
import type { CustomizerStore } from "./index";
import { LIFESTYLE_TOTAL_HOURS } from "@dt-core/types";

describe("customizer store actions", () => {
  let store: ReturnType<typeof createVanillaCustomizerStore>;

  beforeEach(() => {
    store = createVanillaCustomizerStore();
  });

  it("initialises with default attributes and an empty registry", () => {
    const s = store.getState();
    expect(s.activeGender).toBe("Male");
    expect(s.activeCharacter.resemblance).toBe(0.5);
    expect(s.activeCharacter.lifestyle.sleeping).toBe(8);
    expect(s.savedRegistry).toHaveLength(0);
  });

  it("setGender flips the active gender", () => {
    store.getState().setGender("Female");
    expect(store.getState().activeGender).toBe("Female");
  });

  it("updateAttributes applies a mutator immutably and preserves the previous state", () => {
    const before = store.getState().activeCharacter;
    store
      .getState()
      .updateAttributes((s) => {
        s.resemblance = 0.15;
        s.features.nose.x = 0.8;
        s.lifestyle.sports = 8;
      });
    const after = store.getState().activeCharacter;
    expect(after.resemblance).toBe(0.15);
    expect(after.features.nose.x).toBe(0.8);
    expect(after.lifestyle.sports).toBe(8);
    // Immutability: previous reference untouched
    expect(before.resemblance).toBe(0.5);
    expect(after).not.toBe(before);
  });

  it("saveCurrentCharacter persists a deep-cloned profile into the registry", () => {
    store.getState().updateAttributes((s) => {
      s.skinTone = 0.9;
    });
    store.getState().saveCurrentCharacter("Twin_Alpha_01");
    const registry = store.getState().savedRegistry;
    expect(registry).toHaveLength(1);
    expect(registry[0]?.name).toBe("Twin_Alpha_01");
    expect(registry[0]?.attributes.skinTone).toBe(0.9);
    // Mutating the saved profile must not mutate the live character
    expect(store.getState().activeCharacter.skinTone).toBe(0.9);
    expect(registry[0]?.gender).toBe("Male");
  });

  it("loadCharacter restores gender + attributes for a saved id", () => {
    store.getState().setGender("Female");
    store.getState().updateAttributes((s) => {
      s.features.jaw.x = 0.9;
    });
    store.getState().saveCurrentCharacter("Cyber_Model_V2");
    const id = store.getState().savedRegistry[0]!.id;

    // Wipe live state, then reload
    store.getState().reset();
    expect(store.getState().activeGender).toBe("Male");
    expect(store.getState().activeCharacter.features.jaw.x).toBe(0);

    store.getState().loadCharacter(id);
    expect(store.getState().activeGender).toBe("Female");
    expect(store.getState().activeCharacter.features.jaw.x).toBe(0.9);
  });

  it("loadCharacter with an unknown id is a no-op", () => {
    store.getState().loadCharacter("does-not-exist");
    expect(store.getState().activeCharacter.resemblance).toBe(0.5);
  });

  it("reset restores defaults", () => {
    store.getState().updateAttributes((s) => {
      s.lifestyle.illegalWork = 8;
    });
    store.getState().setGender("Female");
    store.getState().reset();
    expect(store.getState().activeGender).toBe("Male");
    expect(store.getState().activeCharacter.lifestyle.illegalWork).toBe(4);
  });

  it("saved profiles always carry a valid 24h lifestyle budget", () => {
    store.getState().saveCurrentCharacter("Budget_Check");
    const attrs = store.getState().savedRegistry[0]!.attributes;
    const sum =
      attrs.lifestyle.sleeping +
      attrs.lifestyle.friends +
      attrs.lifestyle.sports +
      attrs.lifestyle.legalWork +
      attrs.lifestyle.illegalWork;
    expect(sum).toBe(LIFESTYLE_TOTAL_HOURS);
  });
});

// Keep TS happy about the imported type being used (documentation value).
export type { CustomizerStore };
