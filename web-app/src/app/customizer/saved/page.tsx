import React from "react";
import { useCustomizerStore } from "@/stores/useCustomizerStore";
import { calculateStatModifiers } from "@/utils/statCalculators";
import { Badge, Button } from "@/components/ui";
import type { CharacterAttributes } from "@dt-core/types";

interface MockCharacter {
  id: string;
  name: string;
  gender: string;
  heritage: string;
  created: string;
  stats: string;
}

const MOCK_CHARACTERS: MockCharacter[] = [
  {
    id: "1",
    name: "Twin_Alpha_01",
    gender: "Male",
    heritage: "Niko x Emma",
    created: "2026-08-10",
    stats: "High Stealth / Combat",
  },
  {
    id: "2",
    name: "Cyber_Model_V2",
    gender: "Female",
    heritage: "Claude x Misty",
    created: "2026-08-14",
    stats: "High Stamina / Business",
  },
];

/**
 * Saved Characters — Deployment Registry. Review, load, or hot-deploy saved
 * character profiles straight to production pipelines.
 */
export function SavedCharactersPage() {
  const { savedRegistry, loadCharacter } = useCustomizerStore();
  const profiles = savedRegistry.length > 0 ? savedRegistry : MOCK_CHARACTERS;

  const statSummary = (attributes: CharacterAttributes) => {
    const stats = calculateStatModifiers(attributes.lifestyle);
    const top = (Object.entries(stats) as Array<[string, number]>).sort(
      (a, b) => b[1] - a[1],
    )[0];
    return top ? `${top[0] === "lungCapacity" ? "Lung Cap." : top[0]} ${top[1].toFixed(2)}` : "—";
  };

  return (
    <div className="h-full w-full space-y-6 overflow-y-auto p-8">
      <div>
        <h1 className="text-2xl font-bold uppercase tracking-widest text-slate-200">
          Deployment Registry
        </h1>
        <p className="mt-1 text-xs text-slate-500">
          Review, load, or hot-deploy saved characters straight to production pipelines.
        </p>
      </div>

      <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
        {profiles.map((char) => {
          const isStored = "attributes" in char;
          return (
            <div
              key={char.id}
              className="group relative flex flex-col overflow-hidden rounded-2xl border border-slate-800 bg-slate-900/40 p-5 shadow-xl transition-all hover:border-slate-700/80 hover:shadow-2xl"
            >
              <div className="pointer-events-none absolute -right-4 -top-4 h-24 w-24 rounded-full bg-cyan-500/5 blur-xl transition-colors group-hover:bg-cyan-500/10" />
              <div className="mb-4 flex items-start justify-between">
                <div>
                  <h3 className="text-base font-bold tracking-wide text-slate-200 transition-colors group-hover:text-cyan-400">
                    {char.name}
                  </h3>
                  <span className="mt-1.5 inline-block rounded border border-slate-800 bg-slate-950 px-2 py-0.5 font-mono text-[10px] uppercase text-slate-500">
                    {char.gender} Profile
                  </span>
                </div>
                <span className="font-mono text-[10px] text-slate-600">{char.created}</span>
              </div>

              <div className="my-2 space-y-2 rounded-xl border border-slate-900 bg-slate-950/40 p-3">
                <div className="flex justify-between text-xs">
                  <span className="text-slate-500">Genetic Roots:</span>
                  <span className="font-medium text-slate-400">
                    {isStored ? "Custom" : char.heritage}
                  </span>
                </div>
                <div className="flex justify-between text-xs">
                  <span className="text-slate-500">Build Profile:</span>
                  <span className="font-medium text-slate-400">
                    {isStored
                      ? statSummary(char.attributes)
                      : char.stats}
                  </span>
                </div>
                {isStored && (
                  <div className="flex justify-between text-xs">
                    <span className="text-slate-500">Resemblance:</span>
                    <span className="font-medium text-slate-400">
                      {(char.attributes as { resemblance: number }).resemblance.toFixed(2)}
                    </span>
                  </div>
                )}
              </div>

              <div className="mt-4 grid grid-cols-2 gap-2 border-t border-slate-800/60 pt-2">
                <Button variant="default" className="py-2 text-slate-300">
                  Edit Blueprint
                </Button>
                <Button
                  variant="accent"
                  className="py-2"
                  onClick={() => {
                    if (isStored) loadCharacter(char.id);
                  }}
                >
                  {isStored ? "Instantiate" : "Hot-Deploy"}
                </Button>
              </div>
            </div>
          );
        })}
      </div>

      {savedRegistry.length === 0 && (
        <div className="flex items-center gap-2">
          <Badge tone="cyan">Registry Empty</Badge>
          <span className="text-xs text-slate-500">
            Showing demo profiles — save a character from the Builder to populate the registry.
          </span>
        </div>
      )}
    </div>
  );
}
