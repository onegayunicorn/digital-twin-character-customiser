/**
 * Server plumbing — environment configuration.
 */
import { DEFAULT_PORT } from "@dt/shared";

export interface ServerEnv {
  NODE_ENV: "development" | "production" | "test";
  PORT: number;
  DATABASE_URL?: string;
  JWT_SECRET: string;
  OAUTH_CLIENT_ID?: string;
  OAUTH_CLIENT_SECRET?: string;
  CORS_ORIGIN: string;
}

export function loadEnv(overrides: Partial<ServerEnv> = {}): ServerEnv {
  const env = process.env;
  return {
    NODE_ENV:
      (env.NODE_ENV as ServerEnv["NODE_ENV"] | undefined) ??
      overrides.NODE_ENV ??
      "development",
    PORT: Number(env.PORT ?? overrides.PORT ?? DEFAULT_PORT),
    DATABASE_URL: env.DATABASE_URL ?? overrides.DATABASE_URL,
    JWT_SECRET:
      env.JWT_SECRET ??
      overrides.JWT_SECRET ??
      "dev-only-secret-do-not-use-in-production",
    OAUTH_CLIENT_ID: env.OAUTH_CLIENT_ID ?? overrides.OAUTH_CLIENT_ID,
    OAUTH_CLIENT_SECRET:
      env.OAUTH_CLIENT_SECRET ?? overrides.OAUTH_CLIENT_SECRET,
    CORS_ORIGIN: env.CORS_ORIGIN ?? overrides.CORS_ORIGIN ?? "*",
  };
}
