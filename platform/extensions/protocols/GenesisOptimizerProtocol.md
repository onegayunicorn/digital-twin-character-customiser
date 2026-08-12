# Protocol: GenesisOptimizerProtocol

> Capability #142 — **Genesis Optimizer** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Genetic-algorithm + SPSA optimizer with pluggable fitness (sphere/rastrigin/molecule stub). Optimization artifacts only.

## Interface contract
```typescript
// protocol: GenesisOptimizerProtocol
interface GenesisOptimizerProtocol extends BaseOperation {
  id: string;
  name: 'Genesis Optimizer';
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
| Trigger(s) | [`OptimizationRequestedTrigger`](../triggers/GenesisOptimizerTrigger.md) |
| Task(s) | [`RunGaTask`](../tasks/GenesisOptimizerTask.md), [`RunSpsaTask`](../tasks/GenesisOptimizerTask.md) |
| Workflow | [`GenesisOptimizerWorkflow`](../workflows/GenesisOptimizerWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Init population -> Evolve -> SPSA refine -> Validate -> Report
