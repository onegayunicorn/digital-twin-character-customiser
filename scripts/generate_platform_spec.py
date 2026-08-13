#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the platform contract from the 131-item Cloudflare Permissions &
Capabilities specification.

Outputs (under platform/):
  protocols/<Name>Protocol.md   - interface contract per capability
  triggers/<Name>Trigger.md     - event source per capability
  workflows/<Name>Workflow.md   - end-to-end process per capability
  tasks/<Name>Task.md           - atomic unit per capability
  schemas/base-types.md         - BaseOperation/TriggerContract/WorkflowDefinition/TaskSpecification
  README.md                     - capability -> file mapping index

Usage:
  python3 scripts/generate_platform_spec.py [--dry-run]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLATFORM = os.path.join(ROOT, "platform")

sys.path.insert(0, os.path.join(ROOT, "scripts"))
from spec_data_a import ENTRIES_A  # noqa: E402
from spec_data_b import ENTRIES_B  # noqa: E402

ENTRIES = ENTRIES_A + ENTRIES_B

# App-layer extension capabilities (batch 3, 2026-08-12): new systems added to
# the monorepo. Generated under platform/extensions/ to keep the 131-item
# Cloudflare contract intact.
EXTENSIONS = [
    (132, "Twin Engine Sync",
     "Event-sourced digital-twin synchronization: typed event bus, versioned state store, interpolation, heartbeat staleness.",
     "TwinStateChangedTrigger (on state update) | HeartbeatTimeoutTrigger",
     "SyncTwinStateTask | DetectStaleTwinTask",
     "Capture -> Version -> Broadcast -> Reconcile -> Verify"),
    (133, "Agent Orchestration",
     "Sovereign orchestrator core: agent lifecycle state machine, priority task queue, scheduler tick loop, memory stores, tool ACL, audit chain.",
     "TaskQueuedTrigger | AgentReadyTrigger",
     "DispatchTaskTask | RegisterAgentTask",
     "Enqueue -> Schedule -> Execute -> Audit"),
    (134, "MT Communion CLI",
     "IpAI MirrorTwin dialogue: intent -> sentiment valence -> 3-cell resonance routing -> reply -> engram persistence.",
     "IntentReceivedTrigger",
     "RouteIntentTask | StoreEngramTask",
     "Intent -> Sentiment -> Route -> Reply -> Persist"),
    (135, "Crystal Nucleation Sim",
     "Crystal Planet Formation engine: thermal gradient field, nucleation P = exp(-dG*/(kT)), growth, accretion feedback, stabilization.",
     "SimulationStepTrigger | StabilizationTrigger",
     "NucleateCrystalTask | AccreteMassTask",
     "Init -> Nucleate -> Grow -> Feedback -> Stabilize"),
    (136, "Photonic Analysis",
     "PERO photonic toolkit: splitting efficiency, spatial coherence, spectral decomposition, FFT, Bell S-parameter, SPDC coincidence.",
     "MeasurementIngestedTrigger",
     "AnalyzeClassicalTask | VerifyQuantumTask",
     "Ingest -> Classical metrics -> Quantum verify -> Verdict -> Report"),
    (137, "Quantum Sphere Mode",
     "IPS energy-sphere twin-state visualization: sphere charge state, energy metrics, phase-synced rendering.",
     "SphereStateChangedTrigger",
     "RenderSphereTask | ComputeEnergyTask",
     "Sync -> Compute -> Render -> Observe"),
    (138, "Medical Decision Support",
     "Healthcare agency agents (hospital triage, doctor case review, researcher matching) — decision-support only, never autonomous treatment; every output carries clinical_claim_level=none.",
     "VitalsReceivedTrigger | CaseSubmittedTrigger",
     "RunTriageTask | ReviewCaseTask | MatchLiteratureTask",
     "Ingest -> Score -> Present -> Log -> Escalate"),
    (139, "DMD Repair Simulation",
     "DMD nonsense-mutation reference analysis + mechanism-level repair simulation (exon skipping, base/prime editing feasibility). Outputs mechanisms, never efficacy.",
     "MutationIngestedTrigger",
     "ClassifyMutationTask | SimulateRepairTask",
     "Classify -> Codon analysis -> Mechanism sim -> Disclaimer -> Report"),
    (140, "Cancer Dynamics",
     "Gompertz tumor growth + therapy-response simulation (kill rate, resistance emergence, rebound detection). SIMULATED math only.",
     "TherapyScenarioTrigger",
     "RunGrowthSimTask | DetectReboundTask",
     "Init -> Grow -> Treat -> Detect rebound -> Report"),
    (141, "Sonar 5D Mesh",
     "Crystal-mesh geometry (diamond-cubic lattice, OBJ export) + 5D sonar sweep (x,y,z,time,intensity echo field).",
     "MeshRequestedTrigger | SweepTrigger",
     "GenerateMeshTask | RunSweepTask | ExportObjTask",
     "Generate -> Invariants -> Sweep -> Export -> Visualize"),
    (142, "Genesis Optimizer",
     "Genetic-algorithm + SPSA optimizer with pluggable fitness (sphere/rastrigin/molecule stub). Optimization artifacts only.",
     "OptimizationRequestedTrigger",
     "RunGaTask | RunSpsaTask",
     "Init population -> Evolve -> SPSA refine -> Validate -> Report"),
    (143, "Healthcare Agency",
     "Hospital/doctor/researcher agent roster for medtech operations: triage, case review, literature matching, and audit-logged decision support.",
     "AgencyRequestTrigger | AuditTrigger",
     "DispatchAgencyAgentTask | AuditHealthcareActionTask",
     "Dispatch -> Execute -> Guardrail check -> Audit -> Report"),
    (144, "Governance Orchestrator",
     "Dispatch-coordination agent: routes task batches to agents by role with audit logging.",
     "BatchReceivedTrigger",
     "RouteBatchTask | LogDispatchTask",
     "Ingest -> Route -> Dispatch -> Audit"),
    (145, "Gatekeeper",
     "Policy gate: blocks unverified claim markers and enforces ACLs. The enforcement point of the claims register.",
     "ContentSubmittedTrigger | AccessRequestTrigger",
     "CheckClaimsTask | CheckAclTask",
     "Submit -> Check claims -> Check ACL -> Allow/Block -> Log"),
    (146, "Watcher",
     "Health monitoring: heartbeat staleness, spec integrity counts, test status; flags attention items.",
     "HealthCheckTrigger | SpecDriftTrigger",
     "ScanHeartbeatsTask | VerifySpecCountsTask",
     "Collect -> Compare -> Flag -> Report"),
    (147, "Tallyman",
     "Accounting agent: aggregates task/test/claim counts and cost metrics; flags anomalies.",
     "TallyRequestTrigger",
     "AggregateMetricsTask | FlagAnomalyTask",
     "Collect metrics -> Aggregate -> Flag -> Report"),
    (148, "Chat Agent",
     "Operator dialogue router: intent -> governance agent or direct reply; refuses quarantined requests.",
     "MessageReceivedTrigger",
     "RouteIntentTask | RefuseQuarantinedTask",
     "Parse -> Classify -> Route/Refuse -> Reply"),
    (149, "Matrix Integration",
     "Build adjacency matrices from repo inventories and dependency declarations; graph metrics (density, centrality).",
     "InventoryUpdatedTrigger",
     "BuildAdjacencyTask | ComputeGraphMetricsTask",
     "Load inventory -> Build matrix -> Metrics -> Report"),
    (150, "Matrix Evolution",
     "GA over adjacency matrices toward structural targets (density, degree skew) using the genesis engine.",
     "EvolutionRequestedTrigger",
     "EvolveMatrixTask",
     "Encode -> Evolve -> Decode -> Validate -> Report"),
    (151, "Mathematical Hardening",
     "Numerical stability checks: condition estimates, residual norms, relative error bounds for sim outputs.",
     "SimOutputReadyTrigger",
     "EstimateConditionTask | CheckResidualTask",
     "Analyze -> Condition -> Residual -> Grade -> Report"),
    (152, "Repo Sandbox",
     "Per-repository agent + sandbox workspace generation from the 420-repo inventory (manifest, sim stub, README).",
     "RepoInventoriedTrigger",
     "GenerateSandboxTask | InstantiateRepoAgentTask",
     "Load repo -> Generate sandbox -> Agent -> Verify -> Report"),
    (153, "Pipeline Runner",
     "Declarative pipelines: ordered steps referencing queue tasks with dependency gating and audit.",
     "PipelineSubmittedTrigger",
     "ExecutePipelineTask | GateDependenciesTask",
     "Validate -> Enqueue steps -> Dispatch -> Audit -> Report"),
    (154, "Sovereign Kernel",
     "Twelve shared primitives (identity, trust, policy, permissions, ledger, events, payments, contracts, compliance, audit, ai-agents, interoperability) used by every vertical.",
     "PrimitiveAttachedTrigger",
     "RegisterPrimitiveTask | AttachPrimitiveTask",
     "Register -> Attach -> Health check -> Report"),
    (155, "Jurisdiction Engine",
     "Six-dimension jurisdiction classification (user/entity/transaction/asset/service/data) -> regulatory profile -> policy check.",
     "TransactionSubmittedTrigger",
     "ClassifyJurisdictionTask | ResolveProfileTask",
     "Classify -> Profile -> Check -> Warn -> Report"),
    (156, "Compliance OS",
     "Regulatory capability gates (jurisdiction -> classification -> registration -> AML -> KYC -> monitoring -> travel rule -> sanctions -> records -> evaluation -> ENABLE/BLOCK) with evidence log.",
     "FeatureEnableRequestTrigger",
     "RunGateChainTask | LogComplianceEvidenceTask",
     "Gate chain -> Evidence -> Allow/Block -> Audit"),
    (157, "Ledger & Payments",
     "Double-entry ledger, conditional settlement (escrow hold/release/refund), Stripe-style payment orchestration (test-mode).",
     "PaymentInitiatedTrigger | EscrowEventTrigger",
     "PostLedgerEntryTask | RunPaymentFlowTask | HoldEscrowTask",
     "Gate -> Intent -> Hold -> Capture -> Release -> Reconcile"),
    (158, "Procurement Engine",
     "RFQ/RFP/tender, bid evaluation (value-for-money), three-way matching (PO/GRN/invoice) with rules engine.",
     "TenderOpenedTrigger | InvoiceSubmittedTrigger",
     "EvaluateBidsTask | ThreeWayMatchTask",
     "Tender -> Bids -> Evaluate -> PO -> GRN -> Invoice -> Match -> Pay"),
    (159, "Off-grid Sync",
     "Offline transaction queue, store-and-forward, local ledger, eventual-consistency merge, disaster mode.",
     "OfflineTransactionTrigger | SyncOpportunityTrigger",
     "EnqueueOfflineTask | MergeLedgerTask | EnterDisasterModeTask",
     "Queue -> Sync -> Merge -> Reconcile -> Report"),
    (160, "Entity Registry",
     "Legal entity registry (person..DAO), beneficial ownership, governance requirements per entity type.",
     "EntityRegisteredTrigger",
     "RegisterEntityTask | AddBeneficialOwnerTask",
     "Register -> Verify type -> Ownership -> Governance -> Report"),
    (161, "Supply Chain Provenance",
     "SKU registry, serialisation, batch tracking, chain-of-custody with hash chaining.",
     "UnitSerialisedTrigger | CustodyEventTrigger",
     "SerialiseUnitTask | AppendCustodyEventTask",
     "Register SKU -> Serialise -> Track -> Verify chain -> Report"),
    (162, "NFC Escrow",
     "NFC-tap conditional settlement bridge: tap -> hold -> verify condition -> release/refund (nfc-escrow-bridge integration).",
     "NfcTapTrigger | ConditionVerifiedTrigger",
     "TapHoldTask | ReleaseOrRefundTask",
     "Tap -> Hold -> Verify -> Release/Refund -> Audit"),
]

ACCESS_LEVELS = ["read", "write", "admin"]


def slugify(title: str) -> str:
    """'Access: Organizations, Identity Providers, and Groups Write' ->
    'AccessOrganizationsIdentityProvidersAndGroupsWrite'"""
    s = re.sub(r"[^0-9A-Za-z ]+", "", title)
    return "".join(part.capitalize() for part in s.split())


def access_level(entry_num: int, title: str) -> str:
    t = title.lower()
    if "read" in t:
        return "read"
    if "admin" in t:
        return "admin"
    return "write"


def category(num: int) -> str:
    # Domain grouping mirroring the source document's section headers
    if num <= 7:
        return "Agents & AI / Automation"
    if num <= 14:
        return "Workers, Compute & Code"
    if num <= 20:
        return "Storage & Data"
    if num <= 23:
        return "Messaging, PubSub & Queues"
    if num <= 29:
        return "Observability & Telemetry"
    if num <= 34:
        return "Domain, DNS & Networking"
    if num <= 62:
        return "Security & Edge"
    if num <= 78:
        return "Account, Auth, Email & Billing"
    if num <= 82:
        return "Media & Streaming"
    if num <= 89:
        return "Load Balancing & Traffic"
    return "Access & Zero Trust"


def split_items(s: str):
    return [x.strip() for x in s.split("|") if x.strip()]


def protocol_md(num, title, purpose, triggers, tasks, workflow):
    slug = slugify(title)
    trig = split_items(triggers)
    task_list = split_items(tasks)
    return f"""# Protocol: {slug}Protocol

> Capability #{num} — **{title}** · Domain: {category(num)} · Access: `{access_level(num, title)}`

## Purpose
{purpose}

## Interface contract
```typescript
// protocol: {slug}Protocol
interface {slug}Protocol extends BaseOperation {{
  id: string;
  name: '{title}';
  accessLevel: '{access_level(num, title)}';
  category: '{category(num)}';
  serviceDomain: string;
  enabled: boolean;
  auditLogging: boolean;
  rateLimit?: RateLimit;
  // capability-specific contract fields
}}
```

## Related artifacts
| Type | File |
|---|---|
| Trigger(s) | {', '.join(f'[`{t}`](../triggers/{slug}Trigger.md)' for t in trig)} |
| Task(s) | {', '.join(f'[`{t}`](../tasks/{slug}Task.md)' for t in task_list)} |
| Workflow | [`{slug}Workflow`](../workflows/{slug}Workflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
{workflow}
"""


def trigger_md(num, title, triggers, tasks):
    slug = slugify(title)
    trig = split_items(triggers)
    task_list = split_items(tasks)
    lines = []
    for i, t in enumerate(trig):
        name = t.split(" (")[0]
        cond = t.split(" (")[1][:-1] if " (" in t else f"condition for {name}"
        lines.append(f"""### Trigger: {name}

```typescript
// trigger: {name}
const {name}Contract: TriggerContract = {{
  triggerId: '{name}',
  triggerType: 'event',
  condition: {{ matchExpression: '{cond}' }},
  actionTarget: '{task_list[0] if task_list else 'N/A'}',
  enabled: true,
  retryPolicy: {{ maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 }},
  timeoutMs: 30000
}};
```
""")
    return f"""# Trigger: {slug}Trigger

> Capability #{num} — **{title}**

Event source(s) that initiate execution for this capability.

{chr(10).join(lines)}
## Related artifacts
- [Protocol](../protocols/{slug}Protocol.md) · [Tasks](../tasks/{slug}Task.md) · [Workflow](../workflows/{slug}Workflow.md)
"""


def workflow_md(num, title, workflow, triggers):
    slug = slugify(title)
    steps = [s.strip() for s in workflow.split("->")]
    step_list = "".join(
        f"""  - stepId: 'step{i + 1}'
    name: '{s}'
    taskRef: 'Task'
    continueOnError: false
""" for i, s in enumerate(steps)
    )
    return f"""# Workflow: {slug}Workflow

> Capability #{num} — **{title}**

## Definition
```typescript
// workflow: {slug}Workflow
const {slug}Workflow: WorkflowDefinition = {{
  workflowId: '{slug}Workflow',
  version: '1.0.0',
  description: '{title} — {workflow}',
  trigger: {{ triggerId: '{split_items(triggers)[0]}' }},
  steps: [
{step_list}  ],
  errorHandling: {{ onFailure: 'retry', notifyOnError: true }},
  executionMode: 'sequential',
  timeoutTotalMs: 120000
}};
```

## Pipeline
{workflow}

## Related artifacts
- [Protocol](../protocols/{slug}Protocol.md) · [Trigger(s)](../triggers/{slug}Trigger.md) · [Tasks](../tasks/{slug}Task.md)
"""


def task_md(num, title, tasks):
    slug = slugify(title)
    task_list = split_items(tasks)
    blocks = []
    for i, t in enumerate(task_list):
        tname = t.split(" (")[0]
        tdesc = t.split(" (")[1][:-1] if " (" in t else f"Execute {tname}"
        blocks.append(f"""### Task: {tname}

```typescript
// task: {tname}
const {tname}Spec: TaskSpecification = {{
  taskId: '{tname}',
  operationRef: '{slug}Protocol',
  inputSchema: {{ capability: '{title}' }},
  outputSchema: {{ status: 'ok' }},
  implementation: 'api_call',
  dependencies: []
}};
```
**Description:** {tdesc}
""")
    return f"""# Task: {slug}Task

> Capability #{num} — **{title}**

Atomic executable unit(s) for this capability.

{chr(10).join(blocks)}
## Related artifacts
- [Protocol](../protocols/{slug}Protocol.md) · [Trigger(s)](../triggers/{slug}Trigger.md) · [Workflow](../workflows/{slug}Workflow.md)
"""


BASE_TYPES = """# Base Types & Contracts

Canonical interfaces referenced by every protocol/trigger/workflow/task definition
in this platform contract. All capabilities in `protocols/`, `triggers/`,
`workflows/`, and `tasks/` conform to these base types.

## 1. BaseOperation (protocol base)

```typescript
// protocol: BaseOperation
interface BaseOperation {
  id: string;
  name: string;
  description: string;
  accessLevel: 'read' | 'write' | 'admin';
  category: string;
  serviceDomain: string;
  enabled: boolean;
  rateLimit?: RateLimit;
  auditLogging: boolean;
}

interface RateLimit {
  requestsPerSecond: number;
  requestsPerMinute: number;
  burstLimit: number;
}
```

## 2. TriggerContract (trigger base)

```typescript
// protocol: TriggerContract
interface TriggerContract {
  triggerId: string;
  triggerType: 'event' | 'schedule' | 'api' | 'webhook' | 'metric' | 'log';
  condition: TriggerCondition;
  actionTarget: string;
  enabled: boolean;
  retryPolicy?: RetryPolicy;
  timeoutMs: number;
}

interface TriggerCondition {
  eventSource?: string;
  matchExpression?: string;
  threshold?: number;
  cronSchedule?: string;
  httpMethod?: string;
  pathPattern?: string;
}

interface RetryPolicy {
  maxAttempts: number;
  backoffStrategy: 'linear' | 'exponential';
  delayMs: number;
}
```

## 3. WorkflowDefinition (workflow base)

```typescript
// protocol: WorkflowDefinition
interface WorkflowDefinition {
  workflowId: string;
  version: string;
  description: string;
  trigger: TriggerContract;
  steps: WorkflowStep[];
  errorHandling: ErrorHandlingStrategy;
  executionMode: 'sequential' | 'parallel';
  timeoutTotalMs: number;
}

interface WorkflowStep {
  stepId: string;
  name: string;
  taskRef: string;
  dependsOn?: string[];
  inputMapping: Record<string, string>;
  outputMapping: Record<string, string>;
  continueOnError: boolean;
}

interface ErrorHandlingStrategy {
  onFailure: 'abort' | 'retry' | 'fallback' | 'ignore';
  fallbackTask?: string;
  notifyOnError: boolean;
}
```

## 4. TaskSpecification (task base)

```typescript
// protocol: TaskSpecification
interface TaskSpecification {
  taskId: string;
  operationRef: string;
  inputSchema: Record<string, any>;
  outputSchema: Record<string, any>;
  implementation: 'api_call' | 'script' | 'function' | 'pipeline';
  endpoint?: string;
  code?: string;
  dependencies?: string[];
}
```
"""


def generate_set(entries, base_dir, prefix="capability"):
    """Generate protocol/trigger/workflow/task files for a set of entries."""
    rows = []
    counts = {"protocols": 0, "triggers": 0, "workflows": 0, "tasks": 0}
    for num, title, purpose, triggers, tasks, workflow in entries:
        slug = slugify(title)
        for sub, writer in (
            ("protocols", protocol_md),
            ("triggers", trigger_md),
            ("workflows", workflow_md),
            ("tasks", task_md),
        ):
            path = os.path.join(base_dir, sub, f"{slug}{sub.capitalize()[:-1]}.md")
            if sub == "protocols":
                content = writer(num, title, purpose, triggers, tasks, workflow)
            elif sub == "triggers":
                content = writer(num, title, triggers, tasks)
            elif sub == "workflows":
                content = writer(num, title, workflow, triggers)
            else:
                content = writer(num, title, tasks)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            counts[sub] += 1
        rows.append(
            f"| {num} | {title} | [`{slug}Protocol`](protocols/{slug}Protocol.md) | "
            f"[`{slug}Trigger`](triggers/{slug}Trigger.md) | [`{slug}Workflow`](workflows/{slug}Workflow.md) | "
            f"[`{slug}Task`](tasks/{slug}Task.md) |"
        )
    return counts, rows


def main():
    dry = "--dry-run" in sys.argv
    counts = {"protocols": 0, "triggers": 0, "workflows": 0, "tasks": 0}
    index_rows = []

    if dry:
        print(f"[DRY-RUN] would generate {len(ENTRIES)} capabilities x 4 artifact types "
              f"+ {len(EXTENSIONS)} extensions x 4")
        assert len(ENTRIES) == 131, f"expected 131 entries, got {len(ENTRIES)}"
        assert len(EXTENSIONS) == 31, f"expected 31 extensions, got {len(EXTENSIONS)}"
        return

    counts, index_rows = generate_set(ENTRIES, PLATFORM)
    ext_counts, ext_rows = generate_set(EXTENSIONS, os.path.join(PLATFORM, "extensions"))

    os.makedirs(os.path.join(PLATFORM, "schemas"), exist_ok=True)
    with open(os.path.join(PLATFORM, "schemas", "base-types.md"), "w", encoding="utf-8") as fh:
        fh.write(BASE_TYPES)

    index = f"""# Platform Contract — Protocol / Trigger / Workflow / Task Specification

Formalization of the Cloudflare Permissions & Capabilities list: **{len(ENTRIES)} capabilities**,
each mapped to a Protocol (interface contract), Trigger(s) (event sources), Workflow(s)
(end-to-end process), and Task(s) (atomic units). Plus **{len(EXTENSIONS)} app-layer
extensions** under `extensions/`.

- Base types: [`schemas/base-types.md`](schemas/base-types.md)
- Extensions: [`extensions/README.md`](extensions/README.md)
- Storage layout: [`manifests/buckets.yaml`](../manifests/buckets.yaml)
- Regenerate: `python3 scripts/generate_platform_spec.py`

## Capability index

| # | Capability | Protocol | Trigger | Workflow | Task |
|---|---|---|---|---|---|
{chr(10).join(index_rows)}

---
*Generated by `scripts/generate_platform_spec.py` — do not hand-edit.*
"""
    with open(os.path.join(PLATFORM, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(index)

    ext_index = f"""# Platform Extensions — App-Layer Capabilities

Additional capabilities added 2026-08-12 (batch 3) for the new platform systems
(ipai-cli, digital-twin, cpf-sim, pero, sovereign). Same contract shape as the
131-item Cloudflare specification: Protocol / Trigger / Workflow / Task.

| # | Capability | Protocol | Trigger | Workflow | Task |
|---|---|---|---|---|---|
{chr(10).join(ext_rows)}

---
*Generated by `scripts/generate_platform_spec.py` — do not hand-edit.*
"""
    os.makedirs(os.path.join(PLATFORM, "extensions"), exist_ok=True)
    with open(os.path.join(PLATFORM, "extensions", "README.md"), "w", encoding="utf-8") as fh:
        fh.write(ext_index)

    total = sum(counts.values()) + sum(ext_counts.values())
    print(f"Core: {counts} | Extensions: {ext_counts} | Total artifact files: {total}")


if __name__ == "__main__":
    main()
