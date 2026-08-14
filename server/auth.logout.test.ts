import { describe, it, expect, beforeEach } from "vitest";
import { appRouter } from "./routers";
import { createMemoryStorage, type Storage } from "./_core/storage";
import { createContext } from "./_core/trpc";

/**
 * Authentication logout suite — session lifecycle through the tRPC caller.
 */
describe("auth logout", () => {
  let storage: Storage;

  beforeEach(() => {
    storage = createMemoryStorage();
  });

  it("login issues a session token bound to a user", async () => {
    const caller = appRouter.createCaller(createContext(storage, null));
    const { token, user } = await caller.auth.login({});
    expect(token).toMatch(/^sess_/);
    expect(user.email).toBe("dev@aether.local");
    expect(storage.sessions.has(token)).toBe(true);
  });

  it("me returns the user while authenticated", async () => {
    const anon = appRouter.createCaller(createContext(storage, null));
    const { token } = await anon.auth.login({ email: "me@aether.local" });
    const caller = appRouter.createCaller(createContext(storage, token));
    const me = await caller.auth.me();
    expect(me?.email).toBe("me@aether.local");
  });

  it("logout destroys the session; subsequent me is unauthorized", async () => {
    const anon = appRouter.createCaller(createContext(storage, null));
    const { token } = await anon.auth.login({ email: "out@aether.local" });
    const caller = appRouter.createCaller(createContext(storage, token));

    const out = await caller.auth.logout();
    expect(out.ok).toBe(true);
    expect(storage.sessions.has(token)).toBe(false);

    // A fresh request context with the (now deleted) token is unauthorized
    const afterLogout = appRouter.createCaller(createContext(storage, token));
    await expect(afterLogout.auth.me()).rejects.toMatchObject({
      code: "UNAUTHORIZED",
    });
  });

  it("protected procedures reject anonymous callers", async () => {
    const anon = appRouter.createCaller(createContext(storage, null));
    await expect(anon.auth.me()).rejects.toMatchObject({ code: "UNAUTHORIZED" });
  });

  it("login is idempotent for the same email (reuses user)", async () => {
    const caller = appRouter.createCaller(createContext(storage, null));
    const a = await caller.auth.login({ email: "dup@aether.local" });
    const b = await caller.auth.login({ email: "dup@aether.local" });
    expect(a.user.id).toBe(b.user.id);
    expect(a.token).not.toBe(b.token);
  });
});
