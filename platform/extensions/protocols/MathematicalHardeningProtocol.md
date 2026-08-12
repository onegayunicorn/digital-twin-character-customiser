# Protocol: MathematicalHardeningProtocol

> Capability #151 — **Mathematical Hardening** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Numerical stability checks: condition estimates, residual norms, relative error bounds for sim outputs.

## Interface contract
```typescript
// protocol: MathematicalHardeningProtocol
interface MathematicalHardeningProtocol extends BaseOperation {
  id: string;
  name: 'Mathematical Hardening';
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
| Trigger(s) | [`SimOutputReadyTrigger`](../triggers/MathematicalHardeningTrigger.md) |
| Task(s) | [`EstimateConditionTask`](../tasks/MathematicalHardeningTask.md), [`CheckResidualTask`](../tasks/MathematicalHardeningTask.md) |
| Workflow | [`MathematicalHardeningWorkflow`](../workflows/MathematicalHardeningWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Analyze -> Condition -> Residual -> Grade -> Report
