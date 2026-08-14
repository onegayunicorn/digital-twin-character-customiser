/**
 * Server — tRPC procedure routers.
 *
 * Auth / Journey / Telemetry / Characters, wired against the storage facade.
 */
import { z } from "zod";
import { TRPCError } from "@trpc/server";
import { router, publicProcedure, protectedProcedure } from "./_core/trpc";
import { devOAuthProfile } from "./_core/oauth";
import {
  getJourney,
  upsertJourney,
  listCharacters,
  saveCharacter,
  latestTelemetry,
} from "./db";
import type { Storage } from "./_core/storage";
import { JOURNEY_STEP_COUNT, TELEMETRY_BUFFER } from "@dt/shared";
import {
  calculateStatModifiers,
  validateLifestyleBudget,
} from "@dt-engine/lifestyle";
import { MatrixEvolutionEngine } from "@dt-core/agent-matrix";
import { characterGenomeFitness, GENE_COUNT } from "@dt-engine/evolution";
import { createDefaultAttributes, type CharacterProfile } from "@dt-core/types";

const SESSION_TTL_MS = 1000 * 60 * 60 * 24 * 7; // 7 days

const authRouter = router({
  /** Dev sign-in: creates or reuses a session token. */
  login: publicProcedure
    .input(z.object({ email: z.string().email().optional() }))
    .mutation(({ ctx, input }) => {
      const profile = devOAuthProfile(input.email);
      let user = [...ctx.storage.users.values()].find(
        (u) => u.email === profile.email,
      );
      if (!user) {
        user = {
          id: `user-${ctx.storage.users.size + 1}`,
          email: profile.email,
          displayName: profile.displayName,
        };
        ctx.storage.users.set(user.id, user);
      }
      const token = `sess_${Date.now()}_${Math.random().toString(36).slice(2, 10)}`;
      const now = Date.now();
      ctx.storage.sessions.set(token, {
        token,
        userId: user.id,
        createdAt: now,
        expiresAt: now + SESSION_TTL_MS,
      });
      return { token, user };
    }),

  /** Logout: destroys the session token. */
  logout: protectedProcedure.mutation(({ ctx }) => {
    const token = ctx.session?.token;
    if (token) ctx.storage.sessions.delete(token);
    return { ok: true };
  }),

  /** Current session user. */
  me: protectedProcedure.query(({ ctx }) => {
    const user = ctx.storage.users.get(ctx.session!.userId);
    return user ?? null;
  }),
});

const journeyRouter = router({
  progress: protectedProcedure.query(({ ctx }) => {
    const userId = ctx.session!.userId;
    const existing = getJourney(ctx.storage, userId);
    if (existing) return existing;
    const fresh = {
      userId,
      step: 1,
      completedAt: [] as string[],
      certificateIssued: false,
    };
    upsertJourney(ctx.storage, userId, fresh);
    return fresh;
  }),

  completeStep: protectedProcedure
    .input(z.object({ step: z.number().int().min(1).max(JOURNEY_STEP_COUNT) }))
    .mutation(({ ctx, input }) => {
      const userId = ctx.session!.userId;
      const current = getJourney(ctx.storage, userId) ?? {
        userId,
        step: 1,
        completedAt: [] as string[],
        certificateIssued: false,
      };
      const completed = new Set(current.completedAt);
      completed.add(String(input.step));
      const nextStep = Math.min(JOURNEY_STEP_COUNT, Math.max(1, input.step + 1));
      const next = {
        ...current,
        step: nextStep,
        completedAt: [...completed],
        certificateIssued: completed.size >= JOURNEY_STEP_COUNT,
      };
      return upsertJourney(ctx.storage, userId, next);
    }),
});

const telemetryRouter = router({
  latest: publicProcedure.query(({ ctx }) => latestTelemetry(ctx.storage)),
  stream: publicProcedure
    .input(z.object({ count: z.number().int().min(1).max(TELEMETRY_BUFFER).optional() }))
    .query(({ ctx, input }) => {
      const count = input.count ?? 30;
      return ctx.storage.telemetry.slice(-count);
    }),
});

const characterRouter = router({
  list: protectedProcedure.query(({ ctx }) => listCharacters(ctx.storage)),

  save: protectedProcedure
    .input(
      z.object({
        name: z.string().min(1).max(64),
        gender: z.enum(["Male", "Female"]),
        attributes: z.record(z.unknown()),
      }),
    )
    .mutation(({ ctx, input }) => {
      // Re-validate the 24h budget before persisting
      const attributes = input.attributes as unknown as CharacterProfile["attributes"];
      const validation = validateLifestyleBudget(attributes.lifestyle);
      if (!validation.valid) {
        throw new TRPCError({
          code: "BAD_REQUEST",
          message: `Invalid lifestyle budget: ${validation.errors.join(" ")}`,
        });
      }
      const profile: CharacterProfile = {
        id: `char_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`,
        name: input.name,
        gender: input.gender,
        attributes,
        created: new Date().toISOString().split("T")[0] ?? "",
      };
      return saveCharacter(ctx.storage, profile);
    }),

  /** Evaluate a character's stat modifiers server-side. */
  evaluate: protectedProcedure
    .input(z.object({ lifestyle: z.record(z.number()) }))
    .query(({ ctx, input }) => {
      const lifestyle = input.lifestyle as unknown as CharacterProfile["attributes"]["lifestyle"];
      return calculateStatModifiers(lifestyle);
    }),

  /** Run the agent matrix evolution for N generations and return the best. */
  evolve: protectedProcedure
    .input(
      z.object({
        generations: z.number().int().min(1).max(200).default(25),
        populationSize: z.number().int().min(4).max(200).default(20),
      }),
    )
    .query(({ ctx, input }) => {
      const engine = new MatrixEvolutionEngine({
        populationSize: input.populationSize,
        generations: input.generations,
        geneCount: GENE_COUNT,
        fitness: characterGenomeFitness,
      });
      const result = engine.run();
      return {
        best: result.best,
        generations: result.finalGeneration,
        converged: result.converged,
        history: result.history.map((h) => ({
          generation: h.generation,
          bestFitness: h.bestFitness,
          averageFitness: h.averageFitness,
          diversity: h.diversity,
        })),
      };
    }),
});

export const appRouter = router({
  auth: authRouter,
  journey: journeyRouter,
  telemetry: telemetryRouter,
  characters: characterRouter,
});

export type AppRouter = typeof appRouter;

/** Bootstrap a fresh storage + router pair (used by index.ts and tests). */
export function createServerApi(storage: Storage) {
  return { appRouter, storage };
}

export { createDefaultAttributes };
