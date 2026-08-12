# Protocol: TallymanProtocol

> Capability #147 — **Tallyman** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Accounting agent: aggregates task/test/claim counts and cost metrics; flags anomalies.

## Interface contract
```typescript
// protocol: TallymanProtocol
interface TallymanProtocol extends BaseOperation {
  id: string;
  name: 'Tallyman';
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
| Trigger(s) | [`TallyRequestTrigger`](../triggers/TallymanTrigger.md) |
| Task(s) | [`AggregateMetricsTask`](../tasks/TallymanTask.md), [`FlagAnomalyTask`](../tasks/TallymanTask.md) |
| Workflow | [`TallymanWorkflow`](../workflows/TallymanWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Collect metrics -> Aggregate -> Flag -> Report
