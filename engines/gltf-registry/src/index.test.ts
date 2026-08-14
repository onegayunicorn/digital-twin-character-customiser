import { describe, it, expect } from "vitest";
import {
  createGltfRegistry,
  gltfRegistry,
  DEFAULT_MODEL_ID,
} from "./index";

describe("GLTF registry", () => {
  it("registers the three archive models by default", () => {
    expect(gltfRegistry.list()).toHaveLength(3);
    expect(gltfRegistry.get("standing")?.archiveKey).toBe("wo-standing-v17");
    expect(gltfRegistry.get("armor")?.archiveKey).toBe("armor-f-n7");
    expect(gltfRegistry.get("skull")?.archiveKey).toBe("skull-commander");
  });

  it("resolves model paths", () => {
    expect(gltfRegistry.resolvePath("standing")).toBe("/assets/models/wo-standing-v17.glb");
    expect(gltfRegistry.resolvePath("missing")).toBeUndefined();
  });

  it("filters by category", () => {
    const registry = createGltfRegistry();
    expect(registry.list("skull")).toHaveLength(1);
    expect(registry.list("armor")?.[0]?.id).toBe("armor");
  });

  it("supports runtime registration of custom models", () => {
    const registry = createGltfRegistry([]);
    registry.register({
      id: "imported-twin",
      label: "Imported Twin",
      path: "/assets/models/imported-twin.glb",
      category: "custom",
      tags: ["import"],
    });
    expect(registry.get("imported-twin")?.label).toBe("Imported Twin");
    expect(registry.list("custom")).toHaveLength(1);
  });

  it("exposes the default model id", () => {
    expect(DEFAULT_MODEL_ID).toBe("standing");
  });
});
