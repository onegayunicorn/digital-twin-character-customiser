/**
 * Design: Graphite Specimen Ledger — an asymmetric research bench pairing avatar study with bounded scientific analogy.
 * All simulator copy emphasizes that this browser experience is a visual model, not operational physics.
 */
import { lazy, Suspense, useEffect, useMemo, useState } from "react";
import { ArrowUpRight, CircleAlert, CircleCheck, Database, Download, FileJson, FileText, Pause, Play, RotateCcw, ShieldCheck, SlidersHorizontal } from "lucide-react";
import { Button } from "@/components/ui/button";
import type { FaceVector } from "@/components/AvatarViewport";
import { FeatureGrid } from "@/components/FeatureGrid";
import { buildRunRecord, calculateTelemetry, downloadJson, downloadPdf, type RunRecord, type ScenarioSpec } from "@/lib/simulation-record";
import { UrbanArchivePanel } from "@/components/UrbanArchivePanel";

const AvatarViewport = lazy(() => import("@/components/AvatarViewport").then((module) => ({ default: module.AvatarViewport })));
const ParticleChamber = lazy(() => import("@/components/ParticleChamber").then((module) => ({ default: module.ParticleChamber })));

type ScenarioId = "lattice" | "ensemble" | "boundary" | "optics" | "coupled";
type Scenario = ScenarioSpec & { evidence: string; description: string };

const scenarios: Record<ScenarioId, Scenario> = {
  lattice: { id: "lattice", label: "Correlation lattice", short: "SPDC-inspired", evidence: "Established concept · simplified visualization", ceiling: 0.92, description: "Paired particle links illustrate correlation fidelity under an environment-like noise term." },
  ensemble: { id: "ensemble", label: "Resonant ensemble", short: "Coherent motion", evidence: "Qualitative analogy", ceiling: 0.78, description: "A phased particle ensemble makes collective motion and damping visually comparable." },
  boundary: { id: "boundary", label: "Dynamic boundary", short: "Casimir context", evidence: "Educational reference only", ceiling: 0.66, description: "A read-only reference track visualizes a changing boundary pattern without modelling a device." },
  optics: { id: "optics", label: "Optical-metric tunnel", short: "Transformation optics", evidence: "Established optical analogy", ceiling: 0.86, description: "Contour geometry illustrates how an effective optical path can be remapped for light." },
  coupled: { id: "coupled", label: "Coupled avatar field", short: "Interface metaphor", evidence: "Original interface metaphor", ceiling: 0.73, description: "Avatar feature anchors and visual telemetry share one display grammar; no physical coupling is implied." },
};

const stages = ["Establish baseline", "Trace correlation", "Introduce field pattern", "Evaluate analogy", "Archive and cool-down"];
const initialVectors: Record<string, FaceVector> = { brow: { x: -0.14, y: 0.08 }, eyes: { x: 0.08, y: 0.02 }, nose: { x: -0.04, y: -0.08 }, jaw: { x: 0.18, y: 0.02 } };

function Metric({ label, value, accent, detail }: { label: string; value: string; accent: "cyan" | "amber" | "paper"; detail: string }) {
  return <div className={`metric metric-${accent}`}><span>{label}</span><strong>{value}</strong><small>{detail}</small></div>;
}

export default function Home() {
  const [scenarioId, setScenarioId] = useState<ScenarioId>("optics");
  const [running, setRunning] = useState(false);
  const [time, setTime] = useState(0);
  const [correlation, setCorrelation] = useState(0.72);
  const [fieldPattern, setFieldPattern] = useState(0.6);
  const [environment, setEnvironment] = useState(0.18);
  const [particleCount, setParticleCount] = useState(72);
  const [resemblance, setResemblance] = useState(0.52);
  const [tone, setTone] = useState(0.44);
  const [vectors, setVectors] = useState(initialVectors);
  const [runHistory, setRunHistory] = useState<RunRecord[]>([]);
  const scenario = scenarios[scenarioId];
  const simulationInputs = useMemo(() => ({ scenario, correlation, fieldPattern, environment, particleCount, resemblance, tone, vectors }), [scenario, correlation, fieldPattern, environment, particleCount, resemblance, tone, vectors]);

  useEffect(() => {
    if (!running) return;
    const timer = window.setInterval(() => setTime((current) => Math.min(100, current + 1.25)), 45);
    return () => window.clearInterval(timer);
  }, [running]);

  useEffect(() => {
    if (!running || time < 100) return;
    const completed = buildRunRecord(simulationInputs, 100, `run-${Date.now().toString(36)}`);
    setRunning(false);
    setRunHistory((history) => [completed, ...history].slice(0, 8));
  }, [running, time, simulationInputs]);

  const telemetry = useMemo(() => calculateTelemetry(simulationInputs, time), [simulationInputs, time]);
  const stageIndex = Math.min(4, Math.floor((time / 100) * 5));
  const activeRecord = useMemo(() => runHistory[0] ?? (time > 0 ? buildRunRecord(simulationInputs, time, "preview") : null), [runHistory, simulationInputs, time]);

  const begin = () => { setTime(0); setRunning(true); };
  const reset = () => { setRunning(false); setTime(0); };
  const exportJson = () => { if (activeRecord) downloadJson(activeRecord); };
  const exportPdf = () => { if (activeRecord) downloadPdf(activeRecord); };
  const updateVector = (key: string, next: FaceVector) => setVectors((current) => ({ ...current, [key]: next }));

  return (
    <main className="lab-shell">
      <header className="topbar">
        <a className="brand" href="#top" aria-label="Quantum Avatar Simulation Lab home">
          <img src="/manus-storage/qasl-logo_f979cef4.png" alt="" />
          <span><b>QUANTUM AVATAR</b><i>SIMULATION LAB</i></span>
        </a>
        <nav aria-label="Primary navigation"><a href="#lab">Workbench</a><a href="#method">Method</a><a href="#sources">Evidence</a></nav>
        <div className="topbar-status"><span className="status-dot" /> BROWSER-ONLY MODEL</div>
      </header>

      <section id="top" className="hero">
        <div className="hero-copy">
          <p className="eyebrow">VISUAL SIMULATION / AVATAR STUDY</p>
          <h1>Trace the analogy,<br /><em>not the impossible claim.</em></h1>
          <p className="hero-intro">A transparent 3D workspace that brings character customisation, photonic correlations, particle coherence, and optical analogs into one carefully labelled visual model.</p>
          <div className="hero-actions"><Button onClick={() => document.getElementById("lab")?.scrollIntoView({ behavior: "smooth" })} className="primary-action">Open workbench <ArrowUpRight /></Button><a href="#method" className="text-action">Read the boundary <ArrowUpRight /></a></div>
        </div>
        <img className="hero-art" src="/manus-storage/qasl-hero-chamber_463268dc.jpg" alt="Abstract 3D microcell resonance chamber visualisation" />
        <aside className="hero-record"><span>CHAMBER RECORD</span><b>SPEC-01 / OPTICAL ANALOG</b><i>grid: normalized · device link: none</i><div><em>CAL 01</em><em>CAL 02</em><em>CAL 03</em></div></aside>
        <div className="hero-caption"><span>SPECIMEN 01</span><span>VISUAL CORRELATION CHAMBER</span></div>
      </section>

      <section className="boundary-note" aria-label="Scientific scope notice"><CircleAlert /><p><strong>Scientific scope:</strong> This interface is an educational, browser-only visualization. It has no hardware connection, does not provide operating instructions, and does not claim physical portal creation, spacetime alteration, or material reconstruction.</p><a href="#sources">Evidence ledger <ArrowUpRight /></a></section>

      <section id="lab" className="workbench">
        <aside className="specimen-rail">
          <div className="rail-heading"><span className="eyebrow">MODEL INDEX</span><strong>Select a visual track</strong></div>
          <div className="scenario-list">
            {(Object.keys(scenarios) as ScenarioId[]).map((id, index) => <button className={`scenario-option ${scenarioId === id ? "selected" : ""}`} onClick={() => { setScenarioId(id); reset(); }} key={id}><span>{String(index + 1).padStart(2, "0")}</span><div><b>{scenarios[id].label}</b><small>{scenarios[id].short}</small></div><i /></button>)}
          </div>
          <div className="rail-foot"><ShieldCheck /><p><strong>{scenario.evidence}</strong>{scenario.description}</p></div>
        </aside>

        <div className="chamber-panel">
          <div className="panel-titlebar"><div><span className="eyebrow">CHAMBER / {scenario.short}</span><h2>{scenario.label}</h2></div><div className="stage-readout"><span>STAGE {stageIndex + 1}/5</span><b>{stages[stageIndex]}</b></div></div>
          <Suspense fallback={<div className="canvas-fallback">Loading 3D visual model…</div>}><ParticleChamber time={time} correlation={correlation} fieldPattern={fieldPattern} environment={environment} particleCount={particleCount} /></Suspense>
          <div className="timeline"><div className="timeline-track"><span style={{ width: `${time}%` }} /></div><div>{stages.map((stage, index) => <span className={index <= stageIndex ? "active" : ""} key={stage}>{String(index + 1).padStart(2, "0")} {stage}</span>)}</div></div>
          <div className="control-deck">
            <div className="run-controls"><Button onClick={begin} disabled={running} className="run-button"><Play /> Run visual model</Button><Button variant="outline" onClick={() => setRunning((current) => !current)} disabled={!time || time >= 100}>{running ? <><Pause /> Pause</> : <><Play /> Resume</>}</Button><Button variant="ghost" onClick={reset}><RotateCcw /> Reset</Button></div>
            <div className="run-record-actions"><div><span className="eyebrow">RUN ARCHIVE</span><small>{activeRecord ? `${runHistory.length ? "Latest completed record" : "Live preview record"} · ${activeRecord.recordId}` : "Complete or start a visual run to create a record."}</small></div><div className="export-buttons"><Button variant="outline" size="sm" onClick={exportJson} disabled={!activeRecord}><FileJson /> JSON</Button><Button variant="outline" size="sm" onClick={exportPdf} disabled={!activeRecord}><FileText /> PDF</Button></div></div>
            <div className="control-sliders">
              <label>Correlation <output>{correlation.toFixed(2)}</output><input type="range" min="0.2" max="1" step="0.01" value={correlation} onChange={(event) => setCorrelation(Number(event.target.value))} /></label>
              <label>Field pattern <output>{fieldPattern.toFixed(2)}</output><input type="range" min="0.2" max="1" step="0.01" value={fieldPattern} onChange={(event) => setFieldPattern(Number(event.target.value))} /></label>
              <label>Environment <output>{environment.toFixed(2)}</output><input type="range" min="0.02" max="0.8" step="0.01" value={environment} onChange={(event) => setEnvironment(Number(event.target.value))} /></label>
              <label>Particle count <output>{particleCount}</output><input type="range" min="30" max="120" step="6" value={particleCount} onChange={(event) => setParticleCount(Number(event.target.value))} /></label>
            </div>
          </div>
        </div>

        <aside className="evidence-ledger">
          <div className="ledger-heading"><span className="eyebrow">LIVE LEDGER</span><strong>Normalized telemetry</strong></div>
          <Metric label="Correlation fidelity" value={telemetry.fidelity.toFixed(3)} accent="cyan" detail="visual state" />
          <Metric label="Ensemble coherence" value={telemetry.coherence.toFixed(3)} accent="paper" detail="visual state" />
          <Metric label="Environmental noise" value={telemetry.noise.toFixed(3)} accent="amber" detail="model weight" />
          <div className="analogy-score"><span>OPTICAL ANALOGY INDEX</span><strong>{telemetry.analogyIndex.toFixed(3)}</strong><p>{telemetry.analogyIndex > 0.55 ? "Visual analogy sustained" : "Visual analogy developing"}</p><small>Interpretation is limited to this software model.</small></div>
          <div className="ledger-result"><CircleCheck /><p><strong>{time >= 100 ? "Run archived" : "Awaiting completed run"}</strong>{time >= 100 ? "Result: simulation-only visual model — no physical claim." : "A completed run records the model state, not an experiment."}</p></div>
          <div className="ledger-archive"><Download /><span>{runHistory.length} saved run{runHistory.length === 1 ? "" : "s"}</span><small>JSON and PDF exports include the full telemetry series.</small></div>
        </aside>
      </section>

      <section className="avatar-workbench">
        <div className="avatar-title"><span className="eyebrow">AVATAR / NEUTRAL STUDY MODEL</span><h2>A 3D form that responds to <em>abstract</em> vectors.</h2><p>Influenced by the supplied character-creator interaction patterns, this renderer uses neutral presets and normalised controls. It does not infer identity, ancestry, health, or genetics.</p><aside className="avatar-record"><span>MAQUETTE RECORD</span><b>FORM: ARC / VELA</b><small>anchors: 04 · range: -1.00 → +1.00</small></aside></div>
        <div className="avatar-layout">
          <div className="avatar-controls"><div className="control-section"><div className="section-kicker"><SlidersHorizontal /><span>FORM BLEND</span></div><label>Resemblance mix <output>{resemblance.toFixed(2)}</output><input type="range" min="0" max="1" step="0.01" value={resemblance} onChange={(event) => setResemblance(Number(event.target.value))} /></label><label>Tone blend <output>{tone.toFixed(2)}</output><input type="range" min="0" max="1" step="0.01" value={tone} onChange={(event) => setTone(Number(event.target.value))} /></label></div><div className="profile-card"><span>ORIGIN FORM</span><b>ARC / VELA</b><small>Two neutral structural presets</small></div><div className="lifestyle"><div><span>LIFESTYLE BUDGET</span><b>24 / 24 h</b></div><div className="lifestyle-bars"><i style={{ width: "33%" }} /><i style={{ width: "25%" }} /><i style={{ width: "25%" }} /><i style={{ width: "17%" }} /></div><small>Rest 8h · Craft 6h · Motion 6h · Community 4h</small></div></div>
          <div className="avatar-frame"><Suspense fallback={<div className="canvas-fallback avatar-fallback">Loading avatar study…</div>}><AvatarViewport resemblance={resemblance} tone={tone} vectors={vectors} /></Suspense><div className="avatar-still"><img src="/manus-storage/qasl-avatar-hologram_81bafc13.jpg" alt="Abstract avatar hologram reference visual" /><span>REFERENCE STUDY</span></div></div>
          <div className="feature-controls"><div className="section-kicker"><Database /><span>FEATURE VECTORS</span></div><p>Move a crosshair to set each normalized vector.</p><div className="feature-grid-list">{Object.entries(vectors).map(([key, value]) => <FeatureGrid key={key} label={key} value={value} onChange={(next) => updateVector(key, next)} />)}</div></div>
        </div>
      </section>

      <UrbanArchivePanel />

      <section id="method" className="method-section">
        <div className="method-heading"><span className="eyebrow">MODEL METHOD</span><h2>Every visual output carries an assumption.</h2></div>
        <div className="method-records"><aside><span className="eyebrow">METHOD INDEX</span><b>Assumption<br />register</b><small>Each record declares what the model can and cannot represent.</small><div><i /> <i /> <i /> <i /></div></aside><div className="method-grid"><article><span>01</span><h3>Visual correlation</h3><p>Correlation curves, paired links, and noise are normalized state variables for comparison, not measured entanglement data.</p></article><article><span>02</span><h3>Particle ensemble</h3><p>Particles represent a qualitative, bounded motion analogy. They are not dust, molecules, plasma, or a material model.</p></article><article><span>03</span><h3>Optical mapping</h3><p>Field contours represent an effective optical-path analogy. They do not model space, gravity, an actual tunnel, or a portal.</p></article></div></div>
        <div className="method-art"><img src="/manus-storage/qasl-field-mesh_725d22c6.jpg" alt="Abstract transformation optics field mesh" /><div><span className="eyebrow">EXPLANATORY VISUAL</span><h3>Light may be modeled through engineered optical analogies. The analogy is not a claim about spacetime.</h3><a href="#sources">Open source ledger <ArrowUpRight /></a></div></div>
      </section>

      <section id="sources" className="sources-section"><div><span className="eyebrow">EVIDENCE LEDGER</span><h2>Grounded concepts; explicit limits.</h2><p>SPDC photon-pair sources and entanglement distribution are real areas of quantum optics. Dynamical-Casimir research concerns time-varying electromagnetic boundaries. Transformation-optics structures can demonstrate photonic analogies; none of these establish a mechanism for a portal in reality.</p></div><ol><li><a href="https://www.nist.gov/pml/productsservices/quantum-networks-nist/technologies-quantum-networks/sources-nonclassical-light" target="_blank" rel="noreferrer"><b>01</b><span>NIST — Sources of Nonclassical Light for Quantum Networks</span><ArrowUpRight /></a></li><li><a href="https://www.riken.jp/en/news_pubs/research_news/rr/20180511_FY20180005" target="_blank" rel="noreferrer"><b>02</b><span>RIKEN — Dynamical Casimir effect within reach of optomechanics</span><ArrowUpRight /></a></li><li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12504751/" target="_blank" rel="noreferrer"><b>03</b><span>Nature Communications — Photonic analogies of parallel spaces and wormholes</span><ArrowUpRight /></a></li></ol></section>

      <footer><span>QUANTUM AVATAR SIMULATION LAB / 2026</span><span>SIMULATION-ONLY · NO DEVICE CONNECTED</span></footer>
    </main>
  );
}
