/**
 * Aether Core — Zustand customizer state store.
 *
 * Centralized reactive state managing gender, maternal/paternal parent IDs,
 * resemblance and skin-tone sliders, the 2D feature vectors, appearance
 * properties, lifestyle allocations, and the saved-character registry.
 */
import { create } from "zustand";
import { createStore, type StoreApi } from "zustand/vanilla";
import {
  cloneAttributes,
  createDefaultAttributes,
  type CharacterAttributes,
  type CharacterProfile,
  type Gender,
} from "@dt-core/types";

export interface CustomizerStore {
  activeGender: Gender;
  activeCharacter: CharacterAttributes;
  savedRegistry: CharacterProfile[];
  setGender: (gender: Gender) => void;
  updateAttributes: (updater: (state: CharacterAttributes) => void) => void;
  saveCurrentCharacter: (name: string) => void;
  loadCharacter: (id: string) => void;
  reset: () => void;
}

type SetFn = (
  partial:
    | Partial<CustomizerStore>
    | ((state: CustomizerStore) => Partial<CustomizerStore>),
) => void;

export function customizerStoreInitializer(set: SetFn): CustomizerStore {
  return {
    activeGender: "Male",
    activeCharacter: createDefaultAttributes(),
    savedRegistry: [],
    setGender: (gender) => set({ activeGender: gender }),
    updateAttributes: (updater) =>
      set((state) => {
        // Structural deep clone for immutable state handling
        const next = cloneAttributes(state.activeCharacter);
        updater(next);
        return { activeCharacter: next };
      }),
    saveCurrentCharacter: (name) =>
      set((state) => {
        const profile: CharacterProfile = {
          id: crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random()}`,
          name,
          gender: state.activeGender,
          attributes: cloneAttributes(state.activeCharacter),
          created: new Date().toISOString().split("T")[0] ?? "",
        };
        return { savedRegistry: [...state.savedRegistry, profile] };
      }),
    loadCharacter: (id) =>
      set((state) => {
        const profile = state.savedRegistry.find((c) => c.id === id);
        if (!profile) return {};
        return {
          activeGender: profile.gender,
          activeCharacter: cloneAttributes(profile.attributes),
        };
      }),
    reset: () =>
      set({
        activeGender: "Male",
        activeCharacter: createDefaultAttributes(),
      }),
  };
}

/** React hook store (default export used by the web-app). */
export const useCustomizerStore = create<CustomizerStore>(
  customizerStoreInitializer,
);

/** Vanilla store factory — usable in node (tests, simulations) without React. */
export function createVanillaCustomizerStore(): StoreApi<CustomizerStore> {
  return createStore<CustomizerStore>(customizerStoreInitializer);
}

export { DEFAULT_ATTRIBUTES, createDefaultAttributes } from "@dt-core/types";
