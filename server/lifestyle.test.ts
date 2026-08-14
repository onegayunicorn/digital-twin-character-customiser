import { describe, it, expect } from "vitest";
import {
  validateLifestyleBudget,
  calculateStatModifiers,
  statPower,
  normaliseLifestyle,
} from "@dt-engine/lifestyle";
import { createDefaultAttributes, LIFESTYLE_TOTAL_HOURS } from "@dt-core/types";

/**
 * Server-side lifestyle suite — validates the budget rules through the server
 * package's dependency surface (spec parity: server/lifestyle.test.ts).
 */
describe("server lifestyle rules", () => {
  it("accepts the balanced default budget", () => {
    const attrs = createDefaultAttributes();
    const result = validateLifestyleBudget(attrs.lifestyle);
    expect(result.valid).toBe(true);
    expect(result.total).toBe(LIFESTYLE_TOTAL_HOURS);
  });

  it("rejects >8h categories and <4h sleep", () => {
    const bad = { ...createDefaultAttributes().lifestyle, illegalWork: 10, sleeping: 3 };
    const result = validateLifestyleBudget(bad);
    expect(result.valid).toBe(false);
    expect(result.errors.length).toBeGreaterThanOrEqual(2);
  });

  it("modifiers cover all seven stats and stay in [0,1]", () => {
    const stats = calculateStatModifiers(createDefaultAttributes().lifestyle);
    expect(Object.keys(stats)).toHaveLength(7);
    for (const v of Object.values(stats)) {
      expect(v).toBeGreaterThanOrEqual(0);
      expect(v).toBeLessThanOrEqual(1);
    }
  });

  it("statPower orders profiles consistently", () => {
    const balanced = statPower(calculateStatModifiers(createDefaultAttributes().lifestyle));
    const athletic = statPower(
      calculateStatModifiers({
        sleeping: 6,
        friends: 4,
        sports: 8,
        legalWork: 4,
        illegalWork: 2,
      }),
    );
    expect(athletic).toBeGreaterThan(balanced);
  });

  it("normaliseLifestyle restores the 24h invariant", () => {
    const fixed = normaliseLifestyle({
      sleeping: 12,
      friends: 5,
      sports: 5,
      legalWork: 1,
      illegalWork: 1,
    });
    const sum = fixed.sleeping + fixed.friends + fixed.sports + fixed.legalWork + fixed.illegalWork;
    expect(sum).toBeCloseTo(24, 5);
  });
});
