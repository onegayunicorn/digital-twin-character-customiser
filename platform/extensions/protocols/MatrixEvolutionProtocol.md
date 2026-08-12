# Protocol: MatrixEvolutionProtocol

> Capability #150 — **Matrix Evolution** · Domain: Access & Zero Trust · Access: `write`

## Purpose
GA over adjacency matrices toward structural targets (density, degree skew) using the genesis engine.

## Interface contract
```typescript
// protocol: MatrixEvolutionProtocol
interface MatrixEvolutionProtocol extends BaseOperation {
  id: string;
  name: 'Matrix Evolution';
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
| Trigger(s) | [`EvolutionRequestedTrigger`](../triggers/MatrixEvolutionTrigger.md) |
| Task(s) | [`EvolveMatrixTask`](../tasks/MatrixEvolutionTask.md) |
| Workflow | [`MatrixEvolutionWorkflow`](../workflows/MatrixEvolutionWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Encode -> Evolve -> Decode -> Validate -> Report
