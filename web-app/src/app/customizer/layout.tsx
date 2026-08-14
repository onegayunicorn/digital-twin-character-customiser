import React, { useState, type ReactNode } from "react";
import { Link, useLocation } from "wouter";

interface NavItem {
  name: string;
  href: string;
  icon: string;
  description: string;
}

const NAVIGATION: NavItem[] = [
  {
    name: "Character Builder",
    href: "/customizer/builder",
    icon: "🧬",
    description: "Genetic heritage and facial fine-tuning",
  },
  {
    name: "AI Customizer Chat",
    href: "/customizer/ai-chat",
    icon: "🤖",
    description: "Prompt-to-mesh procedural creation",
  },
  {
    name: "Avatar Showcase",
    href: "/customizer/showcase",
    icon: "✨",
    description: "Studio lighting render and animation viewer",
  },
  {
    name: "Saved Characters",
    href: "/customizer/saved",
    icon: "📁",
    description: "Manage, export, and clone deployment profiles",
  },
];

/**
 * CustomizerLayout — the 4-page sidebar navigation shell (per the spec's
 * src/app/customizer/layout.tsx).
 */
export function CustomizerLayout({ children }: { children: ReactNode }) {
  const [location] = useLocation();
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  return (
    <div className="flex h-[calc(100vh-3.5rem)] w-full overflow-hidden bg-slate-950 font-sans text-slate-100 antialiased selection:bg-cyan-500/30 selection:text-cyan-200">
      {/* Sidebar Navigation */}
      <aside
        className={`${
          isSidebarOpen ? "w-80" : "w-20"
        } flex flex-col border-r border-slate-800 bg-slate-900/60 backdrop-blur-md transition-all duration-300 ease-in-out`}
      >
        {/* App Branding Header */}
        <div className="flex h-16 items-center justify-between border-b border-slate-800 px-4">
          <div className={`flex items-center gap-3 ${!isSidebarOpen && "hidden"}`}>
            <div className="h-8 w-8 rounded-lg bg-gradient-to-tr from-cyan-500 to-blue-600 shadow-md shadow-cyan-500/20" />
            <span className="bg-gradient-to-r from-slate-100 to-slate-400 bg-clip-text text-sm font-bold uppercase tracking-wider text-transparent">
              Digital Twin v1.0
            </span>
          </div>
          <button
            onClick={() => setIsSidebarOpen(!isSidebarOpen)}
            className="rounded-lg p-2 text-slate-400 transition-colors hover:bg-slate-800 hover:text-slate-100"
            aria-label="Toggle Sidebar"
          >
            {isSidebarOpen ? "◀" : "▶"}
          </button>
        </div>

        {/* Dynamic Navigation Links */}
        <nav className="flex-1 space-y-1 overflow-y-auto p-3">
          {NAVIGATION.map((item) => {
            const isActive = location === item.href;
            return (
              <Link
                key={item.href}
                href={item.href}
                className={`group flex items-center gap-4 rounded-xl px-4 py-3.5 transition-all duration-200 ${
                  isActive
                    ? "border-l-4 border-cyan-500 bg-gradient-to-r from-cyan-600/20 to-blue-600/10 text-cyan-400 shadow-inner"
                    : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
                }`}
              >
                <span className="text-xl drop-shadow-md transition-transform group-hover:scale-110">
                  {item.icon}
                </span>
                {isSidebarOpen && (
                  <div className="flex flex-col">
                    <span className="text-sm font-semibold tracking-wide">{item.name}</span>
                    <span className="line-clamp-1 text-xs text-slate-500 transition-colors group-hover:text-slate-400">
                      {item.description}
                    </span>
                  </div>
                )}
              </Link>
            );
          })}
        </nav>

        {/* Production Environment Footer */}
        <div className="border-t border-slate-800 bg-slate-950/40 p-4">
          {isSidebarOpen ? (
            <div className="flex items-center gap-3">
              <div className="h-2 w-2 animate-pulse rounded-full bg-emerald-500" />
              <div className="text-xs">
                <p className="font-medium text-slate-400">Vercel Environment</p>
                <p className="text-slate-600">Production Deploy Ready</p>
              </div>
            </div>
          ) : (
            <div className="mx-auto h-2 w-2 rounded-full bg-emerald-500" />
          )}
        </div>
      </aside>

      {/* Primary Context Canvas / Subpage Router */}
      <main className="relative flex h-full flex-1 flex-col overflow-hidden bg-slate-950">
        {children}
      </main>
    </div>
  );
}
