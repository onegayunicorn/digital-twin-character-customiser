/**
 * Server plumbing — tRPC context + procedure builders.
 */
import { initTRPC, TRPCError } from "@trpc/server";
import type { Storage, Session } from "./storage";

export interface ServerContext {
  storage: Storage;
  session: Session | null;
}

export function createContext(
  storage: Storage,
  token?: string | null,
): ServerContext {
  const session = token ? (storage.sessions.get(token) ?? null) : null;
  return { storage, session };
}

const t = initTRPC.context<ServerContext>().create();

/** Public procedures (auth, telemetry reads). */
export const publicProcedure = t.procedure;

/** Protected procedures — require a valid session. */
export const protectedProcedure = t.procedure.use(({ ctx, next }) => {
  if (!ctx.session) {
    throw new TRPCError({ code: "UNAUTHORIZED", message: "No active session" });
  }
  return next({ ctx: { ...ctx, session: ctx.session } });
});

export const router = t.router;
