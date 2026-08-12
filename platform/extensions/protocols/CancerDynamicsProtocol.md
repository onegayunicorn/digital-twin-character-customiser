# Protocol: CancerDynamicsProtocol

> Capability #140 — **Cancer Dynamics** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Gompertz tumor growth + therapy-response simulation (kill rate, resistance emergence, rebound detection). SIMULATED math only.

## Interface contract
```typescript
// protocol: CancerDynamicsProtocol
interface CancerDynamicsProtocol extends BaseOperation {
  id: string;
  name: 'Cancer Dynamics';
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
| Trigger(s) | [`TherapyScenarioTrigger`](../triggers/CancerDynamicsTrigger.md) |
| Task(s) | [`RunGrowthSimTask`](../tasks/CancerDynamicsTask.md), [`DetectReboundTask`](../tasks/CancerDynamicsTask.md) |
| Workflow | [`CancerDynamicsWorkflow`](../workflows/CancerDynamicsWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Init -> Grow -> Treat -> Detect rebound -> Report
