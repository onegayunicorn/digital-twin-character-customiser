/**
 * Simulation: 24-hour lifestyle hour-allocation.
 *
 * Seeds a population of lifestyles, validates every budget against the hard
 * rules, computes stat modifiers, and reports the cohort statistics.
 * Status: SIMULATED — modifier weights are model-internal.
 */
import { writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import {
  calculateStatModifiers,
  validateLifestyleBudget,
  statPower,
  rebalanceLifestyle,
} from "@dt-engine/lifestyle";
import { mulberry32 } from "@dt-core/simulation";
import {
  LIFESTYLE_KEYS,
  LIFESTYLE_TOTAL_HOURS,
  type LifestyleAllocation,
} from "@dt-core/types";

const POPULATION = 256;
const seed = Number(process.env.SIM_SEED ?? 2026);
const rng = mulberry32(seed);

console.log("══════════════════════════════════════════════════════");
console.log(" LIFESTYLE HOUR-ALLOCATION SIMULATION");
console.log(" Status: SIMULATED (deterministic, seeded)");
console.log(` Population: ${POPULATION} · Seed: ${seed}`);
console.log("══════════════════════════════════════════════════════\n");

const budgets: LifestyleAllocation[] = [];
let validated = 0;
let invalid = 0;
const invalidReasons = new Map<string, number>();

for (let i = 0; i < POPULATION; i += 1) {
  // Random raw allocation (may violate the hard rules — that is the point of
  // the validator below)
  const raw: LifestyleAllocation = {
    sleeping: 1 + rng() * 9,
    friends: 1 + rng() * 9,
    sports: 1 + rng() * 9,
    legalWork: 1 + rng() * 9,
    illegalWork: 1 + rng() * 9,
  };

  const result = validateLifestyleBudget(raw);
  if (result.valid) {
    validated += 1;
  } else {
    invalid += 1;
    for (const err of result.errors) {
      invalidReasons.set(err, (invalidReasons.get(err) ?? 0) + 1);
    }
  }
  // The cohort uses the rule-compliant rebalanced budget
  budgets.push(rebalanceLifestyle(raw));
}

// Cohort stats (all budgets valid post-rebalance)
const stats = budgets.map((b) => calculateStatModifiers(b));
const power = stats.map(statPower);
const avgPower = power.reduce((a, b) => a + b, 0) / power.length;
const maxPower = Math.max(...power);
const strongest = budgets[power.indexOf(maxPower)];

console.log(` Valid budgets: ${validated}/${POPULATION}`);
console.log(` Invalid budgets: ${invalid}/${POPULATION}`);
if (invalidReasons.size > 0) {
  console.log("\n Invalid reasons:");
  for (const [reason, count] of invalidReasons) {
    console.log(`   × ${count} — ${reason}`);
  }
}
console.log(`\n Cohort stat power: avg=${avgPower.toFixed(3)} max=${maxPower.toFixed(3)}`);
if (strongest) {
  console.log("\n Strongest profile (by stat power):");
  console.log(JSON.stringify(strongest, null, 2));
  const s = calculateStatModifiers(strongest);
  console.log(` Modifiers: ${JSON.stringify(s)}`);
}

// Report
const outDir = join(import.meta.dirname, "output");
mkdirSync(outDir, { recursive: true });
const report = {
  title: "Lifestyle Hour-Allocation Simulation",
  status: "SIMULATED",
  seed,
  population: POPULATION,
  valid: validated,
  invalid,
  invalidReasons: Object.fromEntries(invalidReasons),
  cohort: { avgPower, maxPower },
  strongest: strongest ? { budget: strongest, modifiers: calculateStatModifiers(strongest) } : null,
};
const outPath = join(outDir, "lifestyle-report.json");
writeFileSync(outPath, JSON.stringify(report, null, 2));
console.log(`\n✔ Report written → ${outPath}`);
