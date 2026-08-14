import { describe, it, expect, beforeEach } from "vitest";
import { appRouter } from "./routers";
import { createMemoryStorage, type Storage } from "./_core/storage";
import { createContext } from "./_core/trpc";
import { JOURNEY_STEP_COUNT } from "@dt/shared";

/**
 * Journey persistence suite — tRPC caller against the in-memory storage.
 */
describe("journey router", () => {
  let storage: Storage;
  let caller: ReturnType<typeof appRouter.createCaller>;
  let token: string;

  beforeEach(async () => {
    storage = createMemoryStorage();
    const anon = appRouter.createCaller(createContext(storage, null));
    const login = await anon.auth.login({ email: "journey@aether.local" });
    token = login.token;
    caller = appRouter.createCaller(createContext(storage, token));
  });

  it("starts a fresh journey at step 1", async () => {
    const progress = await caller.journey.progress();
    expect(progress.step).toBe(1);
    expect(progress.certificateIssued).toBe(false);
  });

  it("advances steps and tracks completions", async () => {
    await caller.journey.completeStep({ step: 1 });
    await caller.journey.completeStep({ step: 2 });
    const progress = await caller.journey.progress();
    expect(progress.step).toBe(3);
    expect(progress.completedAt).toContain("1");
    expect(progress.completedAt).toContain("2");
  });

  it("persists per-user (isolation)", async () => {
    await caller.journey.completeStep({ step: 1 });
    const anon = appRouter.createCaller(createContext(storage, null));
    const other = await anon.auth.login({ email: "other@aether.local" });
    const otherCaller = appRouter.createCaller(createContext(storage, other.token));
    const otherProgress = await otherCaller.journey.progress();
    expect(otherProgress.step).toBe(1);
  });

  it("issues a certificate after completing all steps", async () => {
    for (let step = 1; step <= JOURNEY_STEP_COUNT; step += 1) {
      await caller.journey.completeStep({ step });
    }
    const progress = await caller.journey.progress();
    expect(progress.certificateIssued).toBe(true);
    expect(progress.completedAt).toHaveLength(JOURNEY_STEP_COUNT);
  });

  it("rejects out-of-range steps", async () => {
    await expect(caller.journey.completeStep({ step: 99 })).rejects.toThrow();
  });
});
