# Trigger: WorkersObservabilityWriteTrigger

> Capability #24 — **Workers Observability Write**

Event source(s) that initiate execution for this capability.

### Trigger: MetricThresholdTrigger

```typescript
// trigger: MetricThresholdTrigger
const MetricThresholdTriggerContract: TriggerContract = {
  triggerId: 'MetricThresholdTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MetricThresholdTrigger' },
  actionTarget: 'ConfigureObservabilityTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ObservabilityConfigTrigger

```typescript
// trigger: ObservabilityConfigTrigger
const ObservabilityConfigTriggerContract: TriggerContract = {
  triggerId: 'ObservabilityConfigTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ObservabilityConfigTrigger' },
  actionTarget: 'ConfigureObservabilityTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WorkersObservabilityWriteProtocol.md) · [Tasks](../tasks/WorkersObservabilityWriteTask.md) · [Workflow](../workflows/WorkersObservabilityWriteWorkflow.md)
