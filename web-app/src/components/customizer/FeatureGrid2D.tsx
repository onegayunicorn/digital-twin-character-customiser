import React, { useCallback, useRef } from "react";
import { pixelToGrid, quantisePoint } from "@dt-engine/feature-grid";
import type { Vector2D } from "@dt-core/types";

export interface FeatureGrid2DProps {
  label: string;
  value: Vector2D;
  onChange: (next: Vector2D) => void;
  xLabel?: string;
  yLabel?: string;
}

/**
 * FeatureGrid2D — GTA V-inspired dual-axis crosshair matrix. The user drags
 * the marker across the -1.0..1.0 X/Y space; values feed the customizer store.
 */
export function FeatureGrid2D({
  label,
  value,
  onChange,
  xLabel = "X",
  yLabel = "Y",
}: FeatureGrid2DProps) {
  const ref = useRef<HTMLDivElement>(null);
  const dragging = useRef(false);

  const updateFromEvent = useCallback(
    (clientX: number, clientY: number) => {
      const el = ref.current;
      if (!el) return;
      const rect = el.getBoundingClientRect();
      const next = quantisePoint(
        pixelToGrid(clientX - rect.left, clientY - rect.top, rect.width, rect.height),
        0.05,
      );
      onChange(next);
    },
    [onChange],
  );

  const cx = ((value.x + 1) / 2) * 100;
  const cy = ((value.y + 1) / 2) * 100;

  return (
    <div className="bg-slate-950/60 rounded-xl border border-slate-800 p-4">
      <label className="mb-2 block text-xs font-bold uppercase tracking-wider text-slate-400">
        {label} <span className="font-mono text-cyan-400">[{value.x.toFixed(2)}, {value.y.toFixed(2)}]</span>
      </label>
      <div
        ref={ref}
        className="group relative h-40 w-full cursor-crosshair touch-none overflow-hidden rounded-lg border border-slate-800 bg-slate-950 transition-colors hover:border-slate-700"
        onPointerDown={(e) => {
          dragging.current = true;
          (e.target as HTMLElement).setPointerCapture(e.pointerId);
          updateFromEvent(e.clientX, e.clientY);
        }}
        onPointerMove={(e) => {
          if (dragging.current) updateFromEvent(e.clientX, e.clientY);
        }}
        onPointerUp={() => {
          dragging.current = false;
        }}
      >
        {/* Quarter grid */}
        <div className="pointer-events-none absolute inset-0 grid grid-cols-2 grid-rows-2 opacity-20">
          <div className="border-r border-b border-dashed border-slate-500" />
          <div className="border-b border-dashed border-slate-500" />
          <div className="border-r border-dashed border-slate-500" />
          <div />
        </div>
        {/* Crosshair lines */}
        <div className="pointer-events-none absolute left-0 right-0 top-1/2 h-px bg-slate-700/60" />
        <div className="pointer-events-none absolute top-0 bottom-0 left-1/2 w-px bg-slate-700/60" />
        {/* Marker */}
        <div
          className="absolute h-3 w-3 -translate-x-1/2 -translate-y-1/2 rounded-full bg-cyan-400 shadow-lg shadow-cyan-500/50"
          style={{ left: `${cx}%`, top: `${cy}%` }}
        />
        {/* Axis labels */}
        <span className="pointer-events-none absolute bottom-1 left-2 font-mono text-[9px] text-slate-600">{xLabel}</span>
        <span className="pointer-events-none absolute right-2 top-1 font-mono text-[9px] text-slate-600">{yLabel}</span>
      </div>
    </div>
  );
}
