# Trigger: AllowRequestTracerReadTrigger

> Capability #39 — **Allow Request Tracer Read**

Event source(s) that initiate execution for this capability.

### Trigger: TraceRequestTrigger

```typescript
// trigger: TraceRequestTrigger
const TraceRequestTriggerContract: TriggerContract = {
  triggerId: 'TraceRequestTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TraceRequestTrigger' },
  actionTarget: 'TraceRequestTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: SamplingTrigger

```typescript
// trigger: SamplingTrigger
const SamplingTriggerContract: TriggerContract = {
  triggerId: 'SamplingTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SamplingTrigger' },
  actionTarget: 'TraceRequestTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AllowRequestTracerReadProtocol.md) · [Tasks](../tasks/AllowRequestTracerReadTask.md) · [Workflow](../workflows/AllowRequestTracerReadWorkflow.md)
