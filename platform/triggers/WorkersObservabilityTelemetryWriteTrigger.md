# Trigger: WorkersObservabilityTelemetryWriteTrigger

> Capability #25 — **Workers Observability Telemetry Write**

Event source(s) that initiate execution for this capability.

### Trigger: TelemetryIngestTrigger

```typescript
// trigger: TelemetryIngestTrigger
const TelemetryIngestTriggerContract: TriggerContract = {
  triggerId: 'TelemetryIngestTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TelemetryIngestTrigger' },
  actionTarget: 'ExportTelemetryTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WorkersObservabilityTelemetryWriteProtocol.md) · [Tasks](../tasks/WorkersObservabilityTelemetryWriteTask.md) · [Workflow](../workflows/WorkersObservabilityTelemetryWriteWorkflow.md)
