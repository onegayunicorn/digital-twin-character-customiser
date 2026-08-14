import React, { useState } from "react";
import { useCustomizerStore } from "@/stores/useCustomizerStore";
import { FeatureGrid2D } from "@/components/customizer/FeatureGrid2D";
import { LifestyleBudget } from "@/components/customizer/LifestyleBudget";
import { AvatarR3FCanvas } from "@/components/canvas/AvatarR3FCanvas";
import { Button, Card } from "@/components/ui";

type BuilderTab = "heritage" | "features" | "lifestyle";

/**
 * Character Builder — genetic heritage, dual-axis feature matrix, and 24h
 * lifestyle allocation, rendered alongside the live 3D viewport.
 */
export function CharacterBuilderPage() {
  const { activeCharacter, activeGender, setGender, updateAttributes, saveCurrentCharacter } =
    useCustomizerStore();
  const [activeTab, setActiveTab] = useState<BuilderTab>("heritage");
  const [saveName, setSaveName] = useState("Twin_Alpha_01");

  const updateVector = (key: string) => (value: { x: number; y: number }) => {
    updateAttributes((s) => {
      const vec = s.features[key as keyof typeof s.features] as { x: number; y: number };
      vec.x = value.x;
      vec.y = value.y;
    });
  };

  const randomise = () => {
    updateAttributes((s) => {
      const rnd = () => Math.random() * 2 - 1;
      s.resemblance = Math.random();
      s.skinTone = Math.random();
      s.features.nose.x = rnd();
      s.features.nose.y = rnd();
      s.features.jaw.x = rnd();
      s.features.jaw.y = rnd();
      s.features.brows.y = rnd();
      s.features.eyes.y = rnd();
      s.features.cheekbones.y = rnd();
      s.features.chinShape.x = rnd();
      s.features.lips = rnd();
      s.features.neckWidth = rnd();
    });
  };

  return (
    <div className="flex h-full w-full">
      {/* Parameter Control Sidebar (Left) */}
      <div className="z-10 flex h-full w-96 flex-col overflow-y-auto border-r border-slate-800 bg-slate-900/40 p-6 shadow-2xl backdrop-blur-sm">
        <h1 className="mb-2 text-xl font-bold uppercase tracking-widest text-slate-200">
          Character Creator
        </h1>
        <p className="mb-6 text-xs text-slate-400">
          Modify genetic traits and fine-tune spatial feature arrays.
        </p>

        {/* Gender + In-Panel Sub Tabs */}
        <div className="mb-3 flex gap-2">
          {(["Male", "Female"] as const).map((g) => (
            <button
              key={g}
              onClick={() => setGender(g)}
              className={`flex-1 rounded-lg border py-2 text-xs font-bold uppercase tracking-wider transition-all ${
                activeGender === g
                  ? "border-cyan-500 bg-cyan-950/40 text-cyan-400"
                  : "border-slate-800 bg-slate-950 text-slate-500 hover:text-slate-300"
              }`}
            >
              {g}
            </button>
          ))}
        </div>
        <div className="mb-6 grid grid-cols-3 gap-1 rounded-lg border border-slate-800/80 bg-slate-950 p-1">
          {(["heritage", "features", "lifestyle"] as BuilderTab[]).map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`rounded-md py-2 text-xs font-bold uppercase tracking-wider transition-all ${
                activeTab === tab
                  ? "border border-slate-700/50 bg-slate-800 text-cyan-400 shadow-md"
                  : "text-slate-500 hover:text-slate-300"
              }`}
            >
              {tab}
            </button>
          ))}
        </div>

        {/* Active Sub-Panel */}
        <div className="flex-1 space-y-6">
          {activeTab === "heritage" && (
            <div className="space-y-4">
              <Card className="p-4">
                <label className="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-400">
                  Maternal Profile
                </label>
                <select
                  value={activeCharacter.motherId}
                  onChange={(e) =>
                    updateAttributes((s) => {
                      s.motherId = Number(e.target.value);
                    })
                  }
                  className="w-full rounded-lg border border-slate-700 bg-slate-900 p-2.5 text-sm font-medium text-slate-200 outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500"
                >
                  <option value={0}>Hannah</option>
                  <option value={1}>Sophia</option>
                  <option value={2}>Misty</option>
                </select>
              </Card>
              <Card className="p-4">
                <label className="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-400">
                  Paternal Profile
                </label>
                <select
                  value={activeCharacter.fatherId}
                  onChange={(e) =>
                    updateAttributes((s) => {
                      s.fatherId = Number(e.target.value);
                    })
                  }
                  className="w-full rounded-lg border border-slate-700 bg-slate-900 p-2.5 text-sm font-medium text-slate-200 outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500"
                >
                  <option value={0}>Niko</option>
                  <option value={1}>Claude</option>
                  <option value={2}>Trevor</option>
                </select>
              </Card>
              <Card className="p-4">
                <label className="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-400">
                  Resemblance Blend — {activeCharacter.resemblance.toFixed(2)}
                </label>
                <input
                  type="range"
                  min={0}
                  max={1}
                  step={0.01}
                  value={activeCharacter.resemblance}
                  onChange={(e) =>
                    updateAttributes((s) => {
                      s.resemblance = Number(e.target.value);
                    })
                  }
                  className="w-full cursor-pointer appearance-none accent-cyan-500"
                />
                <div className="mt-1 flex justify-between font-mono text-[10px] text-slate-500">
                  <span>Mother</span>
                  <span>Father</span>
                </div>
              </Card>
              <Card className="p-4">
                <label className="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-400">
                  Skin Tone — {activeCharacter.skinTone.toFixed(2)}
                </label>
                <input
                  type="range"
                  min={0}
                  max={1}
                  step={0.01}
                  value={activeCharacter.skinTone}
                  onChange={(e) =>
                    updateAttributes((s) => {
                      s.skinTone = Number(e.target.value);
                    })
                  }
                  className="w-full cursor-pointer appearance-none accent-cyan-500"
                />
              </Card>
            </div>
          )}

          {activeTab === "features" && (
            <div className="space-y-4">
              <FeatureGrid2D label="Nose Parameters" value={activeCharacter.features.nose} onChange={updateVector("nose")} xLabel="Wide" yLabel="Long" />
              <FeatureGrid2D label="Jaw Matrix" value={activeCharacter.features.jaw} onChange={updateVector("jaw")} xLabel="Square" yLabel="Sharp" />
              <FeatureGrid2D label="Brow Heaviness" value={activeCharacter.features.brows} onChange={updateVector("brows")} xLabel="X" yLabel="Heavy" />
              <FeatureGrid2D label="Eye Size" value={activeCharacter.features.eyes} onChange={updateVector("eyes")} xLabel="X" yLabel="Large" />
              <FeatureGrid2D label="Cheekbone Height" value={activeCharacter.features.cheekbones} onChange={updateVector("cheekbones")} xLabel="X" yLabel="High" />
              <Card className="p-4">
                <label className="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-400">
                  Lip Fullness — {activeCharacter.features.lips.toFixed(2)}
                </label>
                <input
                  type="range"
                  min={-1}
                  max={1}
                  step={0.05}
                  value={activeCharacter.features.lips}
                  onChange={(e) =>
                    updateAttributes((s) => {
                      s.features.lips = Number(e.target.value);
                    })
                  }
                  className="w-full accent-cyan-500"
                />
              </Card>
              <Card className="p-4">
                <label className="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-400">
                  Neck Width — {activeCharacter.features.neckWidth.toFixed(2)}
                </label>
                <input
                  type="range"
                  min={-1}
                  max={1}
                  step={0.05}
                  value={activeCharacter.features.neckWidth}
                  onChange={(e) =>
                    updateAttributes((s) => {
                      s.features.neckWidth = Number(e.target.value);
                    })
                  }
                  className="w-full accent-cyan-500"
                />
              </Card>
            </div>
          )}

          {activeTab === "lifestyle" && (
            <LifestyleBudget
              value={activeCharacter.lifestyle}
              onChange={(lifestyle) =>
                updateAttributes((s) => {
                  s.lifestyle = lifestyle;
                })
              }
            />
          )}
        </div>

        {/* Global Blueprint Commit Footers */}
        <div className="mt-auto flex gap-3 border-t border-slate-800 pt-4">
          <Button variant="default" className="flex-1" onClick={randomise}>
            Randomise
          </Button>
          <div className="flex flex-1 gap-2">
            <input
              value={saveName}
              onChange={(e) => setSaveName(e.target.value)}
              className="w-0 flex-1 rounded-xl border border-slate-700 bg-slate-900 px-2 text-xs text-slate-200 outline-none focus:border-cyan-500"
              placeholder="Name"
            />
            <Button variant="accent" className="flex-1" onClick={() => saveCurrentCharacter(saveName)}>
              Save Data
            </Button>
          </div>
        </div>
      </div>

      {/* 3D WebGL Canvas */}
      <div className="relative flex-1 bg-slate-950 p-8">
        <AvatarR3FCanvas modelId="standing" label="Identity Forge Viewport" />
      </div>
    </div>
  );
}
