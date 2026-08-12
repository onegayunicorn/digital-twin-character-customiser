# Trigger: QueuesWriteTrigger

> Capability #23 — **Queues Write**

Event source(s) that initiate execution for this capability.

### Trigger: QueueMessageEnqueueTrigger

```typescript
// trigger: QueueMessageEnqueueTrigger
const QueueMessageEnqueueTriggerContract: TriggerContract = {
  triggerId: 'QueueMessageEnqueueTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for QueueMessageEnqueueTrigger' },
  actionTarget: 'EnqueueMessageTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: QueueDepthThresholdTrigger

```typescript
// trigger: QueueDepthThresholdTrigger
const QueueDepthThresholdTriggerContract: TriggerContract = {
  triggerId: 'QueueDepthThresholdTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for QueueDepthThresholdTrigger' },
  actionTarget: 'EnqueueMessageTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/QueuesWriteProtocol.md) · [Tasks](../tasks/QueuesWriteTask.md) · [Workflow](../workflows/QueuesWriteWorkflow.md)
