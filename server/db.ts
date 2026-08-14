/**
 * Server — database query helpers.
 *
 * Exposes a DbLike facade over the storage layer. Production would map these
 * calls onto Drizzle queries against MySQL/TiDB (see drizzle/schema.ts); the
 * in-memory facade keeps everything runnable offline and testable.
 */
import { createMemoryStorage, type Storage } from "./_core/storage";

export type Db = Storage;

export function createDb(): Db {
  return createMemoryStorage();
}

export function getJourney(storage: Db, userId: string) {
  return storage.journeys.get(userId);
}

export function upsertJourney(storage: Db, userId: string, progress: Storage["journeys"] extends Map<string, infer V> ? V : never) {
  storage.journeys.set(userId, progress);
  return progress;
}

export function listCharacters(storage: Db) {
  return [...storage.characters.values()];
}

export function saveCharacter(storage: Db, profile: Parameters<Storage["characters"]["set"]>[1]) {
  storage.characters.set(profile.id, profile);
  return profile;
}

export function pushTelemetry(storage: Db, record: Storage["telemetry"][number]) {
  storage.telemetry.push(record);
  return record;
}

export function latestTelemetry(storage: Db) {
  return storage.telemetry[storage.telemetry.length - 1] ?? null;
}
