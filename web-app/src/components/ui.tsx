import React, { type ButtonHTMLAttributes, type ReactNode } from "react";

/** Minimal shadcn-style primitives (button, card, badge, panel). */

export function cn(...parts: Array<string | false | null | undefined>): string {
  return parts.filter(Boolean).join(" ");
}

type ButtonVariant = "default" | "ghost" | "accent" | "danger";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
}

export function Button({
  variant = "default",
  className,
  children,
  ...rest
}: ButtonProps) {
  const styles: Record<ButtonVariant, string> = {
    default:
      "bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700/60",
    ghost: "bg-transparent hover:bg-slate-800/60 text-slate-400 hover:text-slate-100",
    accent:
      "bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-bold shadow-lg shadow-cyan-500/10",
    danger: "bg-rose-600 hover:bg-rose-500 text-white",
  };
  return (
    <button
      className={cn(
        "rounded-xl px-4 py-2 text-xs font-semibold uppercase tracking-wider transition-all disabled:opacity-50",
        styles[variant],
        className,
      )}
      {...rest}
    >
      {children}
    </button>
  );
}

export function Card({
  children,
  className,
}: {
  children: ReactNode;
  className?: string;
}) {
  return (
    <div
      className={cn(
        "rounded-2xl border border-slate-800 bg-slate-900/40 p-5 shadow-xl backdrop-blur-sm",
        className,
      )}
    >
      {children}
    </div>
  );
}

export function Badge({
  children,
  tone = "slate",
}: {
  children: ReactNode;
  tone?: "slate" | "cyan" | "emerald" | "amber";
}) {
  const tones = {
    slate: "bg-slate-950 border-slate-800 text-slate-400",
    cyan: "bg-cyan-950/40 border-cyan-700/50 text-cyan-300",
    emerald: "bg-emerald-950/40 border-emerald-700/50 text-emerald-300",
    amber: "bg-amber-950/40 border-amber-700/50 text-amber-300",
  };
  return (
    <span
      className={cn(
        "inline-flex items-center rounded-md border px-2 py-0.5 font-mono text-[10px] uppercase tracking-wider",
        tones[tone],
      )}
    >
      {children}
    </span>
  );
}

export function StatBar({
  label,
  value,
  max = 1,
}: {
  label: string;
  value: number;
  max?: number;
}) {
  const pct = Math.min(100, Math.max(0, (value / max) * 100));
  return (
    <div>
      <div className="mb-1 flex justify-between text-[10px] font-mono uppercase tracking-wider text-slate-500">
        <span>{label}</span>
        <span className="text-cyan-400">{value.toFixed(2)}</span>
      </div>
      <div className="h-1.5 overflow-hidden rounded-full bg-slate-800">
        <div
          className="h-full rounded-full bg-gradient-to-r from-cyan-500 to-blue-600 transition-all duration-300"
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}
