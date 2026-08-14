import React, { useState } from "react";
import { AvatarR3FCanvas } from "@/components/canvas/AvatarR3FCanvas";

const ENVIRONMENTS = ["Studio", "Cyber", "Noir"] as const;
const POSES = ["Idle Pose", "Walking Cycle", "Combat Ready", "Combat Stance"] as const;

/**
 * Avatar Showcase — immersive studio-lighting presentation canvas with
 * environment staging rigs and cinematic pose cycles.
 */
export function AvatarShowcasePage() {
  const [environment, setEnvironment] = useState<string>("Studio");
  const [pose, setPose] = useState<string>("Idle Pose");

  const envBg: Record<string, string> = {
    Studio: "from-slate-950 via-slate-900 to-slate-950",
    Cyber: "from-cyan-950 via-slate-950 to-fuchsia-950",
    Noir: "from-slate-900 via-stone-950 to-black",
  };

  return (
    <div className="relative h-full w-full bg-slate-950">
      {/* Immersive Presentation Canvas */}
      <div className={`absolute inset-0 bg-gradient-to-br ${envBg[environment] ?? envBg.Studio}`}>
        <div className="p-6">
          <AvatarR3FCanvas modelId={pose === "Combat Ready" || pose === "Combat Stance" ? "armor" : "standing"} label="Showcase Viewport" />
        </div>
      </div>

      {/* Floating Control Staging Overlay */}
      <div className="pointer-events-none absolute bottom-6 left-6 right-6 z-10 flex items-end justify-between">
        {/* Environment Profile Configurations */}
        <div className="pointer-events-auto flex items-center gap-4 rounded-2xl border border-slate-800/80 bg-slate-900/80 p-4 shadow-2xl backdrop-blur-md">
          <div className="flex flex-col">
            <span className="text-[10px] font-bold uppercase tracking-widest text-slate-500">
              Staging Rig
            </span>
            <span className="text-xs font-semibold text-slate-200">
              {environment} {environment === "Cyber" ? "Grid Cyberpunk" : environment === "Noir" ? "Shadow" : "Lightbox"}
            </span>
          </div>
          <div className="h-6 w-px bg-slate-800" />
          <div className="flex gap-2">
            {ENVIRONMENTS.map((env) => (
              <button
                key={env}
                onClick={() => setEnvironment(env)}
                className={`rounded-lg border px-3 py-1.5 text-[11px] font-bold uppercase transition-colors ${
                  environment === env
                    ? "border-cyan-500 bg-cyan-950/40 text-cyan-300"
                    : "border-slate-800 bg-slate-950 text-slate-400 hover:border-slate-600 hover:text-slate-100"
                }`}
              >
                {env}
              </button>
            ))}
          </div>
        </div>

        {/* Dynamic Pose Cycles */}
        <div className="pointer-events-auto flex gap-2 rounded-2xl border border-slate-800/80 bg-slate-900/80 p-4 shadow-2xl backdrop-blur-md">
          {POSES.map((p) => (
            <button
              key={p}
              onClick={() => setPose(p)}
              className={`rounded-xl border px-3 py-2 text-xs font-medium transition-all ${
                pose === p
                  ? "border-cyan-500 text-cyan-400"
                  : "border-slate-800 bg-slate-950/60 text-slate-400 hover:border-cyan-500"
              }`}
            >
              {p}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
