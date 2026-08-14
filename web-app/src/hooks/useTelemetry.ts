import { useEffect, useRef, useState } from "react";
import {
  createTelemetryEngine,
  averageCoherence,
  type TelemetrySample,
} from "@dt-engine/telemetry";
import type { TelemetryEngine } from "@dt-engine/telemetry";

export interface UseTelemetryOptions {
  dt?: number;
  seed?: number;
  bufferSize?: number;
  live?: boolean;
  intervalMs?: number;
}

/**
 * useTelemetry — live 7.83 Hz Schumann resonance stream. When `live` is
 * enabled the hook advances the engine on an interval; otherwise it exposes
 * the engine for manual stepping.
 */
export function useTelemetry(opts: UseTelemetryOptions = {}) {
  const engineRef = useRef<TelemetryEngine | null>(null);
  if (!engineRef.current) {
    engineRef.current = createTelemetryEngine({
      dt: opts.dt ?? 1,
      seed: opts.seed ?? 7,
      bufferSize: opts.bufferSize ?? 120,
    });
  }
  const engine = engineRef.current;
  const [latest, setLatest] = useState<TelemetrySample | undefined>(undefined);

  useEffect(() => {
    if (!opts.live) return;
    const id = setInterval(() => {
      setLatest(engine.step());
    }, opts.intervalMs ?? 1000);
    return () => clearInterval(id);
  }, [engine, opts.live, opts.intervalMs]);

  return {
    engine,
    latest,
    buffer: engine.buffer,
    averageCoherence: () => averageCoherence(engine),
    step: (character?: { vitality?: number; harmony?: number }) =>
      engine.step(character),
  };
}
