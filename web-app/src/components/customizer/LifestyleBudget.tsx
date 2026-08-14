import React from "react";
import {
  calculateStatModifiers,
  validateLifestyleBudget,
} from "@dt-engine/lifestyle";
import {
  LIFESTYLE_KEYS,
  LIFESTYLE_TOTAL_HOURS,
  type LifestyleAllocation,
  type StatBlock,
  type StatKey,
} from "@dt-core/types";
import { StatBar } from "@/components/ui";

export interface LifestyleBudgetProps {
  value: LifestyleAllocation;
  onChange: (next: LifestyleAllocation) => void;
}

const CATEGORY_LABELS: Record<(typeof LIFESTYLE_KEYS)[number], string> = {
  sleeping: "Sleep",
  friends: "Friends & Family",
  sports: "Playing Sports",
  legalWork: "Legal Work",
  illegalWork: "Illegal Work",
};

const STAT_LABELS: Record<StatKey, string> = {
  stamina: "Stamina",
  strength: "Strength",
  stealth: "Stealth",
  shooting: "Shooting",
  driving: "Driving",
  lungCapacity: "Lung Capacity",
  flying: "Flying",
};

/**
 * LifestyleBudget — 24-hour hour-allocation matrix with live validation
 * (sum = 24, sleep ≥ 4h, no category > 8h) and stat modifier readout.
 */
export function LifestyleBudget({ value, onChange }: LifestyleBudgetProps) {
  const validation = validateLifestyleBudget(value);
  const stats: StatBlock = calculateStatModifiers(value);
  const used = LIFESTYLE_KEYS.reduce((acc, k) => acc + (value[k] ?? 0), 0);
  const remaining = LIFESTYLE_TOTAL_HOURS - used;

  const setCategory = (key: keyof LifestyleAllocation, hours: number) => {
    const clamped = Math.max(0, Math.min(10, hours));
    onChange({ ...value, [key]: clamped });
  };

  return (
    <div className="space-y-4 bg-slate-950/60 rounded-xl border border-slate-800 p-4">
      <div className="flex items-center justify-between">
        <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
          Time Allocation Budget
        </span>
        <span
          className={`font-mono text-xs font-bold ${
            validation.valid ? "text-emerald-400" : "text-rose-400"
          }`}
        >
          {remaining.toFixed(1)}h Remaining
        </span>
      </div>

      <div className="space-y-3">
        {LIFESTYLE_KEYS.map((key) => (
          <div key={key}>
            <div className="mb-1 flex justify-between text-xs">
              <span className="text-slate-300">{CATEGORY_LABELS[key]}</span>
              <span className="font-mono text-slate-400">{Math.round(value[key]!)}h</span>
            </div>
            <input
              type="range"
              min={0}
              max={10}
              step={1}
              value={value[key]}
              onChange={(e) => setCategory(key, Number(e.target.value))}
              className="w-full accent-cyan-500"
              aria-label={CATEGORY_LABELS[key]}
            />
          </div>
        ))}
      </div>

      {!validation.valid && (
        <ul className="space-y-1 rounded-lg border border-rose-800/60 bg-rose-950/30 p-3">
          {validation.errors.map((err) => (
            <li key={err} className="text-[11px] font-mono text-rose-300">
              ⚠ {err}
            </li>
          ))}
        </ul>
      )}

      <div className="border-t border-slate-800 pt-3">
        <p className="mb-2 text-[10px] font-bold uppercase tracking-widest text-slate-500">
          Active Attribute Impact Modifiers
        </p>
        <div className="grid grid-cols-2 gap-x-4 gap-y-2">
          {(Object.keys(stats) as StatKey[]).map((k) => (
            <StatBar key={k} label={STAT_LABELS[k]} value={stats[k]} />
          ))}
        </div>
      </div>
    </div>
  );
}
