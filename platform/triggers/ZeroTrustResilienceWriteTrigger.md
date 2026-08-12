# Trigger: ZeroTrustResilienceWriteTrigger

> Capability #129 — **Zero Trust Resilience Write**

Event source(s) that initiate execution for this capability.

### Trigger: ResilienceEventTrigger

```typescript
// trigger: ResilienceEventTrigger
const ResilienceEventTriggerContract: TriggerContract = {
  triggerId: 'ResilienceEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ResilienceEventTrigger' },
  actionTarget: 'ConfigureZeroTrustResilienceTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: FailoverTrigger

```typescript
// trigger: FailoverTrigger
const FailoverTriggerContract: TriggerContract = {
  triggerId: 'FailoverTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for FailoverTrigger' },
  actionTarget: 'ConfigureZeroTrustResilienceTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ZeroTrustResilienceWriteProtocol.md) · [Tasks](../tasks/ZeroTrustResilienceWriteTask.md) · [Workflow](../workflows/ZeroTrustResilienceWriteWorkflow.md)
