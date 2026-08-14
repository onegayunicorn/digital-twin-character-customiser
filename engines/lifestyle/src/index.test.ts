import { describe, it, expect } from "vitest";
import {
  validateLifestyleBudget,
  calculateStatModifiers,
  statPower,
  normaliseLifestyle,
} from "./index";
import {
  createDefaultAttributes,
  LIFESTYLE_TOTAL_HOURS,
  type LifestyleAllocation,
} from "@dt-core/types";

const base = (): LifestyleAllocation => ({
  sleeping: 8,
  friends: 4,
  sports: 4,
  legalWork: 4,
  illegalWork: 4,
});

describe("validateLifestyleBudget — hard rules", () => {
  it("accepts the default balanced budget", () => {
    const r = validateLifestyleBudget(base());
    expect(r.valid).toBe(true);
    expect(r.errors).toHaveLength(0);
  });

  it("rejects budgets that do not sum to 24", () => {
    const bad = { ...base(), sports: 9 };
    const r = validateLifestyleBudget(bad);
    expect(r.valid).toBe(false);
    expect(r.errors.some((e) => e.includes("must equal 24"))).toBe(true);
  });

  it("rejects sleep below 4 hours", () => {
    const bad = { ...base(), sleeping: 3, sports: 5 };
    const r = validateLifestyleBudget(bad);
    expect(r.errors.some((e) => e.includes("Sleep"))).toBe(true);
  });

  it("rejects any single category above 8 hours", () => {
    const bad = { ...base(), illegalWork: 9, sleeping: 7 };
    const r = validateLifestyleBudget(bad);
    expect(r.errors.some((e) => e.includes("may not exceed 8"))).toBe(true);
  });

  it("reports total in the result", () => {
    const r = validateLifestyleBudget(base());
    expect(r.total).toBe(LIFESTYLE_TOTAL_HOURS);
  });

  it("accepts a legal edge case: sleep exactly 4, one category at 8", () => {
    const edge: LifestyleAllocation = {
      sleeping: 4,
      friends: 4,
      sports: 8,
      legalWork: 4,
      illegalWork: 4,
    };
    expect(validateLifestyleBudget(edge).valid).toBe(true);
  });
});

describe("calculateStatModifiers", () => {
  it("produces all seven stats in range 0..1", () => {
    const stats = calculateStatModifiers(base());
    expect(Object.keys(stats)).toHaveLength(7);
    for (const v of Object.values(stats)) {
      expect(v).toBeGreaterThanOrEqual(0);
      expect(v).toBeLessThanOrEqual(1);
    }
  });

  it("sports-heavy allocation boosts stamina and strength", () => {
    const athletic: LifestyleAllocation = {
      sleeping: 6,
      friends: 4,
      sports: 8,
      legalWork: 4,
      illegalWork: 2,
    };
    const stats = calculateStatModifiers(athletic);
    const balanced = calculateStatModifiers(base());
    expect(stats.stamina).toBeGreaterThan(balanced.stamina);
    expect(stats.strength).toBeGreaterThan(balanced.strength);
  });

  it("criminal allocation boosts stealth and shooting", () => {
    const criminal: LifestyleAllocation = {
      sleeping: 5,
      friends: 3,
      sports: 4,
      legalWork: 4,
      illegalWork: 8,
    };
    const stats = calculateStatModifiers(criminal);
    expect(stats.stealth).toBeGreaterThan(0.6);
    expect(stats.shooting).toBeGreaterThan(0.6);
  });

  it("statPower is monotone in total stat strength", () => {
    const a = calculateStatModifiers(base());
    const b = calculateStatModifiers({
      sleeping: 6,
      friends: 3,
      sports: 8,
      legalWork: 5,
      illegalWork: 2,
    });
    expect(statPower(b)).toBeGreaterThan(statPower(a));
  });
});

describe("normaliseLifestyle", () => {
  it("rescales any allocation to exactly 24h", () => {
    const input: LifestyleAllocation = {
      sleeping: 10,
      friends: 2,
      sports: 6,
      legalWork: 3,
      illegalWork: 5,
    };
    const out = normaliseLifestyle(input);
    const total =
      out.sleeping + out.friends + out.sports + out.legalWork + out.illegalWork;
    expect(total).toBeCloseTo(24, 5);
  });

  it("caps categories at 8 hours", () => {
    const input: LifestyleAllocation = {
      sleeping: 14,
      friends: 2,
      sports: 4,
      legalWork: 2,
      illegalWork: 2,
    };
    const out = normaliseLifestyle(input);
    expect(out.sleeping).toBeLessThanOrEqual(8);
  });

  it("default attributes pass validation after normalisation", () => {
    const attrs = createDefaultAttributes();
    expect(validateLifestyleBudget(attrs.lifestyle).valid).toBe(true);
  });
});
