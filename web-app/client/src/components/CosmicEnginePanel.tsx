/**
 * Design: Graphite Specimen Ledger — cosmic subsystem ledger with mineral-paper record surfaces.
 * All values are normalized visual outputs; no physical engine or external connector is present.
 */
import { useMemo, useState } from "react";
import { Orbit, Radio, ShieldCheck, Sparkles } from "lucide-react";
import { Button } from "@/components/ui/button";
import { CosmicEngine, type CosmicSnapshot } from "../../../engines/cosmic/src";

const records: Array<{ key: keyof CosmicSnapshot; label: string; color: string }> = [
  { key: "lattice", label: "Mass / equilibrium lattice", color: "#e8b77a" },
  { key: "lightGrid", label: "Light / shadow grid", color: "#74ded6" },
  { key: "resonanceMesh", label: "Resonance mesh", color: "#a7a3f3" },
  { key: "voidField", label: "Void gradient", color: "#9aa39d" },
];

export function CosmicEnginePanel() {
  const [runCount, setRunCount] = useState(0);
  const result = useMemo<CosmicSnapshot | null>(() => {
    if (!runCount) return null;
    const engine = new CosmicEngine({ seed: 441, nodeCount: 12 });
    let snapshot: CosmicSnapshot | null = null;
    for (let step = 0; step < 32; step += 1) snapshot = engine.step();
    return snapshot;
  }, [runCount]);

  const metric = (key: keyof CosmicSnapshot) => {
    const value = result?.[key];
    if (!value || typeof value !== "object") return 0;
    const numbers = Object.values(value).filter((entry): entry is number => typeof entry === "number");
    return numbers.reduce((sum, entry) => sum + entry, 0) / Math.max(1, numbers.length);
  };

  return (
    <article className="cosmic-engine-panel" aria-labelledby="cosmic-engine-title">
      <div className="cosmic-engine-heading">
        <div className="section-kicker"><Orbit /><span>COSMIC ENGINE / NORMALIZED SYSTEMS</span></div>
        <span className="cosmic-engine-id">CE-04 / READ-ONLY</span>
      </div>
      <div className="cosmic-engine-title-row">
        <div>
          <h3 id="cosmic-engine-title">Four systems, one visual record</h3>
          <p>The supplied lattice, grid, mesh, and void ideas are rewritten as bounded, deterministic visual modules for the digital-twin workbench.</p>
        </div>
        <div className="cosmic-engine-status"><Radio /><span>{result ? `TICK ${result.tick} · ${result.safety}` : "READY · SIMULATION ONLY"}</span></div>
      </div>
      <div className="cosmic-engine-records">
        {records.map((record) => {
          const value = metric(record.key);
          return <div className="cosmic-engine-record" key={record.key}><div><span>{record.label}</span><small>{value.toFixed(3)}</small></div><i><b style={{ width: `${value * 100}%`, background: record.color }} /></i></div>;
        })}
      </div>
      <div className="cosmic-engine-footer"><span><ShieldCheck /> SOFTWARE CAP / NO EXTERNAL CONNECTOR</span><span><Sparkles /> OUTPUT STATUS: SIMULATED</span></div>
      <Button variant="outline" className="cosmic-engine-run" onClick={() => setRunCount((count) => count + 1)}>{result ? "Rerun cosmic record" : "Run cosmic record"}</Button>
      <small className="cosmic-engine-boundary">No gravity, photon, quantum, portal, financial, or hardware claim.</small>
    </article>
  );
}
