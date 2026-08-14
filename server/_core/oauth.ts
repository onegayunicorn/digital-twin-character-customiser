/**
 * Server plumbing — OAuth helper (stub).
 *
 * Production wiring would exchange an authorization code with the provider;
 * this stub mirrors the contract so routers stay testable.
 */
export interface OAuthProfile {
  provider: string;
  providerId: string;
  email: string;
  displayName: string;
}

export function stubOAuthExchange(_code: string): Promise<OAuthProfile | null> {
  // Stub: no real provider configured → return null (router falls back to
  // dev account). Replace with a real token exchange for production.
  return Promise.resolve(null);
}

export function devOAuthProfile(email = "dev@aether.local"): OAuthProfile {
  return {
    provider: "dev",
    providerId: `dev-${email}`,
    email,
    displayName: "Dev Operator",
  };
}
