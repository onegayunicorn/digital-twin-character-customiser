# Protocol: WorkersObservabilityTelemetryWriteProtocol

> Capability #25 — **Workers Observability Telemetry Write** · Domain: Observability & Telemetry · Access: `write`

## Purpose
OpenTelemetry traces, spans, logs, and exporters for telemetry.

## Interface contract
```typescript
// protocol: WorkersObservabilityTelemetryWriteProtocol
interface WorkersObservabilityTelemetryWriteProtocol extends BaseOperation {
  id: string;
  name: 'Workers Observability Telemetry Write';
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
| Trigger(s) | [`TelemetryIngestTrigger`](../triggers/WorkersObservabilityTelemetryWriteTrigger.md) |
| Task(s) | [`ExportTelemetryTask`](../tasks/WorkersObservabilityTelemetryWriteTask.md), [`ConfigureTelemetryTask`](../tasks/WorkersObservabilityTelemetryWriteTask.md) |
| Workflow | [`WorkersObservabilityTelemetryWriteWorkflow`](../workflows/WorkersObservabilityTelemetryWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Instrument -> Collect -> Sample -> Export -> Store
