# Protocol: CrystalNucleationSimProtocol

> Capability #135 — **Crystal Nucleation Sim** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Crystal Planet Formation engine: thermal gradient field, nucleation P = exp(-dG*/(kT)), growth, accretion feedback, stabilization.

## Interface contract
```typescript
// protocol: CrystalNucleationSimProtocol
interface CrystalNucleationSimProtocol extends BaseOperation {
  id: string;
  name: 'Crystal Nucleation Sim';
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
| Trigger(s) | [`SimulationStepTrigger`](../triggers/CrystalNucleationSimTrigger.md), [`StabilizationTrigger`](../triggers/CrystalNucleationSimTrigger.md) |
| Task(s) | [`NucleateCrystalTask`](../tasks/CrystalNucleationSimTask.md), [`AccreteMassTask`](../tasks/CrystalNucleationSimTask.md) |
| Workflow | [`CrystalNucleationSimWorkflow`](../workflows/CrystalNucleationSimWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Init -> Nucleate -> Grow -> Feedback -> Stabilize
