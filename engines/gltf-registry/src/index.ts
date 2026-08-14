/**
 * Aether Core engine — GLTF Model Registry.
 *
 * Registers the archive-sourced GLB models available to the 3D viewport:
 *   Standing — wo-standing-v17 (default hero pose)
 *   Armor    — armor-f-n7    (armored rig)
 *   Skull    — skull-commander (cinematic prop)
 * The registry resolves model paths and supports runtime registration of
 * additional models (e.g. user-imported characters).
 */
export type GltfModelCategory = "standing" | "armor" | "skull" | "custom";

export interface GltfModelEntry {
  id: string;
  label: string;
  path: string;
  category: GltfModelCategory;
  /** Optional archive source key (matches extracted/ asset naming). */
  archiveKey?: string;
  tags: string[];
}

export interface GltfRegistry {
  models: Map<string, GltfModelEntry>;
  register(entry: GltfModelEntry): void;
  get(id: string): GltfModelEntry | undefined;
  list(category?: GltfModelCategory): GltfModelEntry[];
  resolvePath(id: string): string | undefined;
}

const DEFAULT_MODELS: GltfModelEntry[] = [
  {
    id: "standing",
    label: "Standing",
    path: "/assets/models/wo-standing-v17.glb",
    category: "standing",
    archiveKey: "wo-standing-v17",
    tags: ["hero", "idle", "base"],
  },
  {
    id: "armor",
    label: "Armor",
    path: "/assets/models/armor-f-n7.glb",
    category: "armor",
    archiveKey: "armor-f-n7",
    tags: ["armor", "combat"],
  },
  {
    id: "skull",
    label: "Skull Commander",
    path: "/assets/models/skull-commander.glb",
    category: "skull",
    archiveKey: "skull-commander",
    tags: ["skull", "cinematic"],
  },
];

export function createGltfRegistry(initial: GltfModelEntry[] = DEFAULT_MODELS): GltfRegistry {
  const models = new Map<string, GltfModelEntry>();
  for (const entry of initial) models.set(entry.id, entry);
  return {
    models,
    register(entry: GltfModelEntry) {
      models.set(entry.id, entry);
    },
    get(id: string) {
      return models.get(id);
    },
    list(category?: GltfModelCategory) {
      const all = [...models.values()];
      return category ? all.filter((m) => m.category === category) : all;
    },
    resolvePath(id: string) {
      return models.get(id)?.path;
    },
  };
}

/** Singleton registry used across the web-app viewport. */
export const gltfRegistry = createGltfRegistry();

export const DEFAULT_MODEL_ID = "standing";
