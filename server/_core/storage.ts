/**
 * Server plumbing — storage abstraction.
 *
 * The server layer persists journeys, characters, telemetry, and sessions.
 * Production wiring would use Drizzle + MySQL/TiDB (see drizzle/schema.ts);
 * the default in-memory store keeps tests and local dev fully runnable.
 */
import type { CharacterProfile } from "@dt-core/types";

export interface Session {
  token: string;
  userId: string;
  createdAt: number;
  expiresAt: number;
}

export interface JourneyProgress {
  userId: string;
  step: number; // 1..12
  completedAt: string[];
  certificateIssued: boolean;
}

export interface TelemetryRecord {
  t: number;
  schumann: number;
  coherence: number;
}

export interface Storage {
  users: Map<string, { id: string; email: string; displayName: string }>;
  sessions: Map<string, Session>;
  journeys: Map<string, JourneyProgress>;
  characters: Map<string, CharacterProfile>;
  telemetry: TelemetryRecord[];
  flushTelemetry(): void;
}

export function createMemoryStorage(): Storage {
  return {
    users: new Map(),
    sessions: new Map(),
    journeys: new Map(),
    characters: new Map(),
    telemetry: [],
    flushTelemetry() {
      this.telemetry = [];
    },
  };
}
