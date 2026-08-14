/**
 * Aether Core — Procedural AI Prompt Router Engine.
 *
 * A rule-based compiler: analyzes natural-language strings, pulls configuration
 * adjustments using RegEx/keyword heuristics, and outputs structured state
 * overrides (mutator + human-readable operation logs).
 */
import {
  FEATURE_MAX,
  FEATURE_MIN,
  LIFESTYLE_TOTAL_HOURS,
  type CharacterAttributes,
} from "@dt-core/types";

export interface AIParserResult {
  mutator: (state: CharacterAttributes) => void;
  logs: string[];
}

type Mutation = (s: CharacterAttributes) => void;

/** Clamp a feature coordinate into the -1.0..1.0 matrix bounds. */
export function clampFeature(v: number, min = FEATURE_MIN, max = FEATURE_MAX): number {
  return Math.min(max, Math.max(min, v));
}

/** Normalise a 0..1 style value (e.g. resemblance, skinTone). */
export function clampUnit(v: number): number {
  return clampFeature(v, 0, 1);
}

const has = (text: string, ...words: string[]) =>
  words.some((w) => text.includes(w));

export function parseAIPrompt(prompt: string): AIParserResult {
  const normalized = prompt.toLowerCase();
  const logs: string[] = [];
  const mutations: Mutation[] = [];

  // ── 1. Heritage mapping heuristics ──────────────────────────────────────
  if (has(normalized, "resemblance", "look like")) {
    if (has(normalized, "mother", "mom", "maternal")) {
      mutations.push((s) => {
        s.resemblance = 0.15;
      });
      logs.push("🧬 Adjusted resemblance matrix weighted close to Maternal tree (85% Mother).");
    } else if (has(normalized, "father", "dad", "paternal")) {
      mutations.push((s) => {
        s.resemblance = 0.85;
      });
      logs.push("🧬 Adjusted resemblance matrix weighted close to Paternal tree (85% Father).");
    }
  }
  if (has(normalized, "skin")) {
    if (has(normalized, "pale", "lighter", "light skin", "paler")) {
      mutations.push((s) => {
        s.skinTone = 0.2;
      });
      logs.push("🎨 Skin tone shifted toward pale (0.20).");
    } else if (has(normalized, "dark", "darker", "deep")) {
      mutations.push((s) => {
        s.skinTone = 0.85;
      });
      logs.push("🎨 Skin tone shifted toward deep (0.85).");
    }
  }

  // ── 2. Structural feature vector parsing ────────────────────────────────
  if (has(normalized, "nose")) {
    if (has(normalized, "wide", "broad")) {
      mutations.push((s) => {
        s.features.nose.x = 0.8;
      });
      logs.push("📐 Extruded Morph Target: [Nose Width] set to 0.80.");
    }
    if (has(normalized, "narrow", "thin")) {
      mutations.push((s) => {
        s.features.nose.x = -0.8;
      });
      logs.push("📐 Extruded Morph Target: [Nose Width] set to -0.80.");
    }
    if (has(normalized, "long")) {
      mutations.push((s) => {
        s.features.nose.y = 0.75;
      });
      logs.push("📐 Extruded Morph Target: [Nose Length] set to 0.75.");
    }
    if (has(normalized, "short")) {
      mutations.push((s) => {
        s.features.nose.y = -0.75;
      });
      logs.push("📐 Extruded Morph Target: [Nose Length] set to -0.75.");
    }
  }
  if (has(normalized, "jaw")) {
    if (has(normalized, "square", "strong jaw", "alpha", "chiseled", "chiselled")) {
      mutations.push((s) => {
        s.features.jaw.x = 0.9;
        s.features.jaw.y = 0.9;
      });
      logs.push("📐 Bone Translation: Amplified [Jaw Width & Squareness] to 0.90.");
    }
    if (has(normalized, "round", "soft jaw", "v-shape", "v shape", "pointed")) {
      mutations.push((s) => {
        s.features.jaw.x = -0.8;
        s.features.jaw.y = -0.6;
      });
      logs.push("📐 Bone Translation: Softened [Jaw] toward V-shape (-0.80).");
    }
  }
  if (has(normalized, "brow", "eyebrow")) {
    if (has(normalized, "thick", "heavy")) {
      mutations.push((s) => {
        s.features.brows.y = 0.8;
      });
      logs.push("📐 Morph Target: [Brow Heaviness] set to 0.80.");
    }
    if (has(normalized, "thin", "light brow")) {
      mutations.push((s) => {
        s.features.brows.y = -0.7;
      });
      logs.push("📐 Morph Target: [Brow Heaviness] set to -0.70.");
    }
  }
  if (has(normalized, "eye", "eyes")) {
    if (has(normalized, "big", "large", "wide eye")) {
      mutations.push((s) => {
        s.features.eyes.y = 0.75;
      });
      logs.push("📐 Morph Target: [Eye Size] set to 0.75.");
    }
    if (has(normalized, "small", "narrow eye")) {
      mutations.push((s) => {
        s.features.eyes.y = -0.7;
      });
      logs.push("📐 Morph Target: [Eye Size] set to -0.70.");
    }
  }
  if (has(normalized, "cheekbone", "cheek")) {
    if (has(normalized, "high", "sharp")) {
      mutations.push((s) => {
        s.features.cheekbones.y = 0.8;
      });
      logs.push("📐 Morph Target: [Cheekbone Height] set to 0.80.");
    }
  }
  if (has(normalized, "chin")) {
    if (has(normalized, "strong", "square")) {
      mutations.push((s) => {
        s.features.chinShape.x = 0.8;
      });
      logs.push("📐 Morph Target: [Chin Shape] set to 0.80.");
    }
    if (has(normalized, "weak", "receding")) {
      mutations.push((s) => {
        s.features.chinShape.x = -0.8;
      });
      logs.push("📐 Morph Target: [Chin Shape] set to -0.80.");
    }
  }
  if (has(normalized, "lips", "lip")) {
    if (has(normalized, "full", "thick lip")) {
      mutations.push((s) => {
        s.features.lips = 0.8;
      });
      logs.push("📐 Morph Target: [Lip Fullness] set to 0.80.");
    }
    if (has(normalized, "thin lip")) {
      mutations.push((s) => {
        s.features.lips = -0.8;
      });
      logs.push("📐 Morph Target: [Lip Fullness] set to -0.80.");
    }
  }
  if (has(normalized, "neck")) {
    if (has(normalized, "thick", "wide neck")) {
      mutations.push((s) => {
        s.features.neckWidth = 0.85;
      });
      logs.push("📐 Morph Target: [Neck Width] set to 0.85.");
    }
  }

  // ── 3. Statistical lifestyle budget parsing ─────────────────────────────
  if (has(normalized, "athletic", "fighter", "strong", "muscular", "gym", "sports")) {
    mutations.push((s) => {
      s.lifestyle.sports = 8;
      s.lifestyle.sleeping = 6;
      s.lifestyle.friends = 4;
      s.lifestyle.legalWork = 4;
      s.lifestyle.illegalWork = 2; // Total validation sum = 24
    });
    logs.push("📊 Budget reallocated: Set High Physical Activity traits (Sports: 8h, Sleep: 6h).");
  }
  if (has(normalized, "criminal", "heist", "hustler", "underground", "thief")) {
    mutations.push((s) => {
      s.lifestyle.illegalWork = 8;
      s.lifestyle.sleeping = 5;
      s.lifestyle.friends = 3;
      s.lifestyle.sports = 4;
      s.lifestyle.legalWork = 4; // Total validation sum = 24
    });
    logs.push("📊 Budget reallocated: Injected Underground Hustle profile parameters.");
  }
  if (has(normalized, "business", "executive", "corporate", "lawyer", "legal")) {
    mutations.push((s) => {
      s.lifestyle.legalWork = 8;
      s.lifestyle.sleeping = 7;
      s.lifestyle.friends = 3;
      s.lifestyle.sports = 4;
      s.lifestyle.illegalWork = 2; // Total validation sum = 24
    });
    logs.push("📊 Budget reallocated: Corporate Executive profile (Legal Work: 8h).");
  }
  if (has(normalized, "social", "party", "clubbing", "charisma")) {
    mutations.push((s) => {
      s.lifestyle.friends = 8;
      s.lifestyle.sleeping = 6;
      s.lifestyle.sports = 3;
      s.lifestyle.legalWork = 5;
      s.lifestyle.illegalWork = 2; // Total validation sum = 24
    });
    logs.push("📊 Budget reallocated: Social Butterfly profile (Friends: 8h).");
  }
  if (has(normalized, "sleepy", "tired", "rest", "relax", "lazy")) {
    mutations.push((s) => {
      s.lifestyle.sleeping = 10;
      s.lifestyle.friends = 3;
      s.lifestyle.sports = 3;
      s.lifestyle.legalWork = 4;
      s.lifestyle.illegalWork = 4; // Total validation sum = 24
    });
    logs.push("📊 Budget reallocated: Low-energy profile (Sleep: 10h).");
  }
  if (has(normalized, "balanced", "default", "reset lifestyle", "average")) {
    mutations.push((s) => {
      s.lifestyle.sleeping = 8;
      s.lifestyle.friends = 4;
      s.lifestyle.sports = 4;
      s.lifestyle.legalWork = 4;
      s.lifestyle.illegalWork = 4; // Total validation sum = 24
    });
    logs.push("📊 Budget reallocated: Balanced baseline (24h evenly distributed).");
  }

  // ── 4. Hair & appearance -------------------------------------------------
  if (has(normalized, "hair")) {
    if (has(normalized, "neon", "green")) {
      mutations.push((s) => {
        s.appearance.hairColor = 3;
      });
      logs.push("💇 Hair color slot set to neon green (id 3).");
    } else if (has(normalized, "black", "dark hair")) {
      mutations.push((s) => {
        s.appearance.hairColor = 1;
      });
      logs.push("💇 Hair color slot set to black (id 1).");
    } else if (has(normalized, "blonde", "blond", "golden")) {
      mutations.push((s) => {
        s.appearance.hairColor = 2;
      });
      logs.push("💇 Hair color slot set to blonde (id 2).");
    }
    if (has(normalized, "bald", "shaved", "buzz")) {
      mutations.push((s) => {
        s.appearance.hairId = 0;
      });
      logs.push("💇 Hair style set to shaved/bald (id 0).");
    }
  }

  // Fallback structural notice if no rules matched
  if (mutations.length === 0) {
    logs.push("⚠ Input prompt evaluated successfully, but no matching parameters rules were found.");
  }

  // Compound all parsed execution statements into a clean single-pass executor
  const dynamicMutator = (state: CharacterAttributes) => {
    mutations.forEach((mutate) => mutate(state));
    // Post-condition: keep every vector/scalar inside matrix bounds
    const f = state.features;
    const record = f as unknown as Record<string, number>;
    const vecRecord = f as unknown as Record<string, { x: number; y: number }>;
    (Object.keys(f) as (keyof typeof f)[]).forEach((key) => {
      const v = f[key] as { x?: number; y?: number } | number;
      if (typeof v === "number") {
        record[key as string] = clampFeature(v);
      } else if (v && typeof v.x === "number" && typeof v.y === "number") {
        const vec = vecRecord[key as string];
        if (vec) {
          vec.x = clampFeature(v.x);
          vec.y = clampFeature(v.y);
        }
      }
    });
    state.resemblance = clampUnit(state.resemblance);
    state.skinTone = clampUnit(state.skinTone);
    // Enforce 24h budget invariant post-mutation
    const b = state.lifestyle;
    const sum = b.sleeping + b.friends + b.sports + b.legalWork + b.illegalWork;
    if (sum !== LIFESTYLE_TOTAL_HOURS) {
      const diff = LIFESTYLE_TOTAL_HOURS - sum;
      b.sleeping = Math.max(4, Math.min(10, b.sleeping + diff));
    }
  };

  return { mutator: dynamicMutator, logs };
}
