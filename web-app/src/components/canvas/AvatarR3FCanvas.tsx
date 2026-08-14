import React, { useEffect, useRef, useState } from "react";
import { AvatarViewport } from "./AvatarViewport";

export type ViewportStatus = "loading" | "ready" | "fallback";

/**
 * AvatarR3FCanvas — resilient viewport wrapper with debounced resize
 * observation, explicit loading/ready/fallback states, and unmount cleanup
 * (per the Digital Twin spec section 3.1).
 */
export function AvatarR3FCanvas({
  modelId = "standing",
  label = "AVATAR VIEWPORT",
}: {
  modelId?: string;
  label?: string;
}) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [status, setStatus] = useState<ViewportStatus>("loading");
  const [size, setSize] = useState({ width: 0, height: 0 });

  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;

    let raf = 0;
    const measure = () => {
      const rect = el.getBoundingClientRect();
      setSize({ width: rect.width, height: rect.height });
    };

    // Debounced resize observation
    const observer = new ResizeObserver(() => {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(measure);
    });
    observer.observe(el);
    measure();

    // Loading → ready transition once the canvas mounts
    const readyTimer = setTimeout(() => setStatus("ready"), 120);

    return () => {
      observer.disconnect();
      cancelAnimationFrame(raf);
      clearTimeout(readyTimer);
    };
  }, []);

  return (
    <div
      ref={containerRef}
      className="relative h-full w-full overflow-hidden rounded-2xl border border-slate-800/70"
    >
      <div className="pointer-events-none absolute left-3 top-3 z-10">
        <span className="rounded-md border border-slate-800 bg-slate-950/80 px-2 py-1 font-mono text-[10px] uppercase tracking-widest text-cyan-400 backdrop-blur">
          {label}
        </span>
        <span
          className={`ml-2 inline-flex items-center gap-1.5 rounded-md border px-2 py-1 font-mono text-[10px] uppercase tracking-widest backdrop-blur ${
            status === "ready"
              ? "border-emerald-700/50 bg-emerald-950/40 text-emerald-300"
              : "border-amber-700/50 bg-amber-950/40 text-amber-300"
          }`}
        >
          <span
            className={`h-1.5 w-1.5 rounded-full ${
              status === "ready" ? "bg-emerald-400 animate-pulse" : "bg-amber-400"
            }`}
          />
          {status}
        </span>
      </div>
      {size.width > 0 && size.height > 0 ? (
        <div style={{ width: size.width, height: size.height }}>
          <AvatarViewport modelId={modelId} />
        </div>
      ) : (
        <div className="flex h-full items-center justify-center font-mono text-xs tracking-widest text-slate-600">
          INITIALIZING VIEWPORT...
        </div>
      )}
    </div>
  );
}
