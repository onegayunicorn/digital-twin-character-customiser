/**
 * Aether Core engine — Lifestyle Budget.
 *
 * Enforces the 24-hour hour-allocation matrix rules and calculates the active
 * attribute impact modifiers (SIMULATED) produced by a lifestyle allocation.
 *
 * Hard validation rules (from the Digital Twin spec):
 *   - the sum of all categories must equal 24 hours
 *   - sleep must be at least 4 hours
 *   - no single category may exceed 8 hours
 */
import {
  LIFESTYLE_MAX_PER_CATEGORY,
  LIFESTYLE_MIN_SLEEP,
  LIFESTYLE_TOTAL_HOURS,
  STAT_KEYS,
  type LifestyleAllocation,
  type LifestyleKey,
  type StatBlock,
} from "@dt-core/types";

export interface LifestyleValidationResult {
  valid: boolean;
  errors: string[];
  total: number;
}

export const LIFESTYLE_KEYS_LIST: readonly LifestyleKey[] = [
  "sleeping",
  "friends",
  "sports",
  "legalWork",
  "illegalWork",
];

export function lifestyleTotal(a: LifestyleAllocation): number {
  return LIFESTYLE_KEYS_LIST.reduce((acc, k) => acc + (a[k] ?? 0), 0);
}

/**
 * Validate a 24h lifestyle allocation against the hard rules.
 * Returns a list of human-readable errors; empty list = valid.
 */
export function validateLifestyleBudget(a: LifestyleAllocation): LifestyleValidationResult {
  const errors: string[] = [];
  const total = lifestyleTotal(a);

  if (Math.abs(total - LIFESTYLE_TOTAL_HOURS) > 1e-6) {
    errors.push(
      `Total allocation is ${total.toFixed(1)}h — must equal ${LIFESTYLE_TOTAL_HOURS}h.`,
    );
  }
  if (a.sleeping < LIFESTYLE_MIN_SLEEP) {
    errors.push(`Sleep is ${a.sleeping}h — must be at least ${LIFESTYLE_MIN_SLEEP}h.`);
  }
  for (const key of LIFESTYLE_KEYS_LIST) {
    const v = a[key];
    if (v > LIFESTYLE_MAX_PER_CATEGORY) {
      errors.push(
        `${key} is ${v.toFixed(1)}h — may not exceed ${LIFESTYLE_MAX_PER_CATEGORY}h.`,
      );
    }
    if (v < 0) {
      errors.push(`${key} is negative (${v.toFixed(1)}h).`);
    }
  }
  return { valid: errors.length === 0, errors, total };
}

/**
 * Calculate active attribute impact modifiers (range 0..1, SIMULATED).
 *
 * Weight model (documented, deterministic):
 *   stamina      ← sports (0.45) + sleeping (0.15)
 *   strength     ← sports (0.50) + illegalWork (0.10)
 *   stealth      ← illegalWork (0.50)
 *   shooting     ← illegalWork (0.45) + sports (0.15)
 *   driving      ← legalWork (0.50)
 *   lungCapacity ← sleeping (0.40) + sports (0.20)
 *   flying       ← illegalWork (0.40) + legalWork (0.20)
 * Each term is normalised by /8h and added to a 0.30 baseline, clamped to 1.
 */
export function calculateStatModifiers(a: LifestyleAllocation): StatBlock {
  const s = a.sports / 8;
  const sl = a.sleeping / 8;
  const il = a.illegalWork / 8;
  const lw = a.legalWork / 8;
  const fr = a.friends / 8;

  const clamp01 = (v: number) => Math.min(1, Math.max(0, v));

  return {
    stamina: clamp01(0.3 + 0.45 * s + 0.15 * sl + 0.05 * fr),
    strength: clamp01(0.3 + 0.5 * s + 0.1 * il),
    stealth: clamp01(0.3 + 0.5 * il),
    shooting: clamp01(0.3 + 0.45 * il + 0.15 * s),
    driving: clamp01(0.3 + 0.5 * lw + 0.05 * fr),
    lungCapacity: clamp01(0.3 + 0.4 * sl + 0.2 * s),
    flying: clamp01(0.3 + 0.4 * il + 0.2 * lw),
  };
}

/** Sum a stat block (used as an overall "power" metric). */
export function statPower(stats: StatBlock): number {
  return STAT_KEYS.reduce((acc, k) => acc + stats[k], 0);
}

/**
 * Rebalance an allocation so it satisfies all hard rules:
 *   - every category capped at 8h
 *   - sleep lifted to at least 4h
 *   - the sum restored to exactly 24h (redistributed across headroom)
 * Deterministic and idempotent.
 */
export function rebalanceLifestyle(a: LifestyleAllocation): LifestyleAllocation {
  const out: LifestyleAllocation = {
    sleeping: Math.min(LIFESTYLE_MAX_PER_CATEGORY, Math.max(0, a.sleeping)),
    friends: Math.min(LIFESTYLE_MAX_PER_CATEGORY, Math.max(0, a.friends)),
    sports: Math.min(LIFESTYLE_MAX_PER_CATEGORY, Math.max(0, a.sports)),
    legalWork: Math.min(LIFESTYLE_MAX_PER_CATEGORY, Math.max(0, a.legalWork)),
    illegalWork: Math.min(LIFESTYLE_MAX_PER_CATEGORY, Math.max(0, a.illegalWork)),
  };

  // Lift sleep to the 4h floor by borrowing from the largest other category
  if (out.sleeping < LIFESTYLE_MIN_SLEEP) {
    const need = LIFESTYLE_MIN_SLEEP - out.sleeping;
    const others: LifestyleKey[] = ["friends", "sports", "legalWork", "illegalWork"];
    for (const k of others) {
      const give = Math.min(need, out[k]);
      out.sleeping += give;
      out[k] -= give;
      if (out.sleeping >= LIFESTYLE_MIN_SLEEP) break;
    }
  }

  // Redistribute until the sum is exactly 24h with a per-category cap of 8h
  let iterations = 0;
  while (iterations < 200) {
    const sum = lifestyleTotal(out);
    if (Math.abs(sum - LIFESTYLE_TOTAL_HOURS) < 1e-6) break;
    const diff = LIFESTYLE_TOTAL_HOURS - sum;
    const headroom = LIFESTYLE_KEYS_LIST.filter((k) => out[k] < LIFESTYLE_MAX_PER_CATEGORY);
    if (headroom.length === 0) break;
    const totalHeadroom = headroom.reduce(
      (acc, k) => acc + (LIFESTYLE_MAX_PER_CATEGORY - out[k]),
      0,
    );
    if (totalHeadroom <= 0) break;
    for (const k of headroom) {
      const share = diff * ((LIFESTYLE_MAX_PER_CATEGORY - out[k]) / totalHeadroom);
      out[k] = Math.min(LIFESTYLE_MAX_PER_CATEGORY, Math.max(0, out[k] + share));
    }
    iterations += 1;
  }
  return out;
}

/** Alias for rebalanceLifestyle (legacy name). */
export function normaliseLifestyle(a: LifestyleAllocation): LifestyleAllocation {
  return rebalanceLifestyle(a);
}
