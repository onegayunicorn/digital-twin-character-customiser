import React from "react";
import { Link } from "wouter";

const NAV_ITEMS = [
  { href: "/", label: "Home" },
  { href: "/customizer/builder", label: "Customizer" },
  { href: "/journey", label: "Journey" },
  { href: "/telemetry", label: "Telemetry" },
  { href: "/dashboard", label: "Ops Dashboard" },
];

export function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-slate-800/80 bg-slate-950/80 backdrop-blur-md">
      <div className="mx-auto flex h-14 max-w-7xl items-center justify-between px-4">
        <Link href="/" className="flex items-center gap-2.5">
          <div className="h-7 w-7 rounded-lg bg-gradient-to-tr from-cyan-500 to-blue-600 shadow-md shadow-cyan-500/20" />
          <span className="text-sm font-bold uppercase tracking-widest text-transparent bg-clip-text bg-gradient-to-r from-slate-100 to-slate-400">
            Digital Twin v1.0
          </span>
        </Link>
        <nav className="flex items-center gap-1">
          {NAV_ITEMS.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="rounded-lg px-3 py-1.5 text-xs font-semibold tracking-wide text-slate-400 transition-colors hover:bg-slate-800/60 hover:text-cyan-300"
            >
              {item.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
