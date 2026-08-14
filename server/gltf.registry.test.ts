import { describe, it, expect } from "vitest";
import { gltfRegistry, createGltfRegistry } from "@dt-engine/gltf-registry";

/**
 * Server-side GLTF registry suite (spec parity: server/gltf.registry.test.ts).
 */
describe("server GLTF registry", () => {
  it("exposes the three archive models", () => {
    const ids = gltfRegistry.list().map((m) => m.id);
    expect(ids).toEqual(["standing", "armor", "skull"]);
  });

  it("resolves archive paths", () => {
    expect(gltfRegistry.resolvePath("skull")).toContain("skull-commander");
    expect(gltfRegistry.resolvePath("armor")).toContain("armor-f-n7");
  });

  it("registers and filters custom models", () => {
    const registry = createGltfRegistry();
    registry.register({
      id: "server-import",
      label: "Server Import",
      path: "/assets/models/server-import.glb",
      category: "custom",
      tags: [],
    });
    expect(registry.list("custom")).toHaveLength(1);
    expect(registry.get("server-import")?.category).toBe("custom");
  });
});
