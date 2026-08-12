# Trigger: StreamWriteTrigger

> Capability #82 — **Stream Write**

Event source(s) that initiate execution for this capability.

### Trigger: StreamStartedTrigger

```typescript
// trigger: StreamStartedTrigger
const StreamStartedTriggerContract: TriggerContract = {
  triggerId: 'StreamStartedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for StreamStartedTrigger' },
  actionTarget: 'ManageStreamTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: StreamEndedTrigger

```typescript
// trigger: StreamEndedTrigger
const StreamEndedTriggerContract: TriggerContract = {
  triggerId: 'StreamEndedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for StreamEndedTrigger' },
  actionTarget: 'ManageStreamTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/StreamWriteProtocol.md) · [Tasks](../tasks/StreamWriteTask.md) · [Workflow](../workflows/StreamWriteWorkflow.md)
