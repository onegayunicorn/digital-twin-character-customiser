import React from "react";
import { Link } from "wouter";
import { AvatarR3FCanvas } from "@/components/canvas/AvatarR3FCanvas";
import { Badge, Button, Card } from "@/components/ui";

const FEATURES = [
  {
    icon: "🧬",
    title: "Identity Forge",
    desc: "GTA V-style dual-axis facial matrix with maternal/paternal heritage blending.",
    href: "/customizer/builder",
  },
  {
    icon: "🤖",
    title: "Procedural AI Router",
    desc: "Prompt-to-mesh: natural language compiles directly into character array parameters.",
    href: "/customizer/ai-chat",
  },
  {
    icon: "🎛️",
    title: "Simulation Engine",
    desc: "24h lifestyle lifecycle sims, 7.83 Hz Schumann telemetry, and agent matrix evolution.",
    href: "/telemetry",
  },
  {
    icon: "🧿",
    title: "Agent Matrix Evolution",
    desc: "A genetic algorithm evolves twin populations across generations toward fitness targets.",
    href: "/dashboard",
  },
];

/**
 * Home — landing page. "DNA is a library, not a sentence." → the Identity Forge.
 */
export function Home() {
  return (
    <main className="relative mx-auto max-w-7xl px-6 pb-20 pt-12">
      <div className="grid items-center gap-10 lg:grid-cols-2">
        <div>
          <Badge tone="cyan">Aether Core · v4.1.0</Badge>
          <h1 className="mt-4 bg-gradient-to-r from-slate-100 via-cyan-200 to-slate-400 bg-clip-text text-5xl font-black leading-tight tracking-tight text-transparent">
            DNA is a library,
            <br />
            not a sentence.
          </h1>
          <p className="mt-4 max-w-lg text-sm leading-relaxed text-slate-400">
            Forge your digital twin in cinematic 3D. Sculpt heritage, facial vectors, and a
            24-hour lifestyle budget — then let the simulation engine and agent matrix
            evolve them across generations.
          </p>
          <div className="mt-6 flex gap-3">
            <Link href="/customizer/builder">
              <Button variant="accent" className="px-6 py-3">
                Open Identity Forge
              </Button>
            </Link>
            <Link href="/dashboard">
              <Button variant="default" className="px-6 py-3">
                Ops Dashboard
              </Button>
            </Link>
          </div>
        </div>
        <div className="h-[420px]">
          <AvatarR3FCanvas modelId="standing" label="Aether Core Hero Rig" />
        </div>
      </div>

      <div className="mt-16 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {FEATURES.map((f) => (
          <Link key={f.title} href={f.href}>
            <Card className="h-full transition-all hover:border-cyan-700/60 hover:bg-slate-900/70">
              <div className="text-2xl">{f.icon}</div>
              <h3 className="mt-3 text-sm font-bold uppercase tracking-wider text-slate-200">
                {f.title}
              </h3>
              <p className="mt-2 text-xs leading-relaxed text-slate-500">{f.desc}</p>
            </Card>
          </Link>
        ))}
      </div>
    </main>
  );
}
