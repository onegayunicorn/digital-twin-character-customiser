# Protocol: DmdRepairSimulationProtocol

> Capability #139 — **DMD Repair Simulation** · Domain: Access & Zero Trust · Access: `write`

## Purpose
DMD nonsense-mutation reference analysis + mechanism-level repair simulation (exon skipping, base/prime editing feasibility). Outputs mechanisms, never efficacy.

## Interface contract
```typescript
// protocol: DmdRepairSimulationProtocol
interface DmdRepairSimulationProtocol extends BaseOperation {
  id: string;
  name: 'DMD Repair Simulation';
  accessLevel: 'write';
  category: 'Access & Zero Trust';
  serviceDomain: string;
  enabled: boolean;
  auditLogging: boolean;
  rateLimit?: RateLimit;
  // capability-specific contract fields
}
```

## Related artifacts
| Type | File |
|---|---|
| Trigger(s) | [`MutationIngestedTrigger`](../triggers/DmdRepairSimulationTrigger.md) |
| Task(s) | [`ClassifyMutationTask`](../tasks/DmdRepairSimulationTask.md), [`SimulateRepairTask`](../tasks/DmdRepairSimulationTask.md) |
| Workflow | [`DmdRepairSimulationWorkflow`](../workflows/DmdRepairSimulationWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Classify -> Codon analysis -> Mechanism sim -> Disclaimer -> Report
