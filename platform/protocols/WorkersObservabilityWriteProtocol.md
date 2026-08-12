# Protocol: WorkersObservabilityWriteProtocol

> Capability #24 — **Workers Observability Write** · Domain: Observability & Telemetry · Access: `write`

## Purpose
Metrics, alerts, dashboards, and sampling rates for Workers observability.

## Interface contract
```typescript
// protocol: WorkersObservabilityWriteProtocol
interface WorkersObservabilityWriteProtocol extends BaseOperation {
  id: string;
  name: 'Workers Observability Write';
  accessLevel: 'write';
  category: 'Observability & Telemetry';
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
| Trigger(s) | [`MetricThresholdTrigger`](../triggers/WorkersObservabilityWriteTrigger.md), [`ObservabilityConfigTrigger`](../triggers/WorkersObservabilityWriteTrigger.md) |
| Task(s) | [`ConfigureObservabilityTask`](../tasks/WorkersObservabilityWriteTask.md) |
| Workflow | [`WorkersObservabilityWriteWorkflow`](../workflows/WorkersObservabilityWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define metrics -> Set retention -> Build dash -> Create alerts -> Deploy
