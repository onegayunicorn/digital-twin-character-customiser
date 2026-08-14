/**
 * Aether Core — Drizzle ORM database schema (MySQL / TiDB).
 *
 * Tables: users, journeys (12-step activation), telemetry (Schumann stream),
 * characters (deployed twin profiles).
 */
import {
  mysqlTable,
  varchar,
  int,
  boolean,
  timestamp,
  float,
  json,
  index,
} from "drizzle-orm/mysql-core";

export const users = mysqlTable(
  "users",
  {
    id: varchar("id", { length: 64 }).primaryKey(),
    email: varchar("email", { length: 255 }).notNull().unique(),
    displayName: varchar("display_name", { length: 128 }),
    createdAt: timestamp("created_at").defaultNow().notNull(),
  },
  (t) => [index("idx_users_email").on(t.email)],
);

export const journeys = mysqlTable(
  "journeys",
  {
    userId: varchar("user_id", { length: 64 }).primaryKey(),
    step: int("step").notNull().default(1),
    completedAt: json("completed_at").$type<string[]>().notNull().default([]),
    certificateIssued: boolean("certificate_issued").notNull().default(false),
    updatedAt: timestamp("updated_at").defaultNow().notNull(),
  },
  (t) => [index("idx_journeys_user").on(t.userId)],
);

export const telemetry = mysqlTable(
  "telemetry",
  {
    id: int("id").autoincrement().primaryKey(),
    t: float("t").notNull(),
    schumann: float("schumann").notNull(),
    coherence: float("coherence").notNull(),
    entropy: float("entropy").notNull(),
    createdAt: timestamp("created_at").defaultNow().notNull(),
  },
  (t) => [index("idx_telemetry_time").on(t.t)],
);

export const characters = mysqlTable(
  "characters",
  {
    id: varchar("id", { length: 64 }).primaryKey(),
    name: varchar("name", { length: 64 }).notNull(),
    gender: varchar("gender", { length: 8 }).notNull(),
    attributes: json("attributes").notNull(),
    created: varchar("created", { length: 16 }).notNull(),
    createdAt: timestamp("created_at").defaultNow().notNull(),
  },
  (t) => [index("idx_characters_name").on(t.name)],
);

export type UserRow = typeof users.$inferSelect;
export type JourneyRow = typeof journeys.$inferSelect;
export type TelemetryRow = typeof telemetry.$inferSelect;
export type CharacterRow = typeof characters.$inferSelect;
