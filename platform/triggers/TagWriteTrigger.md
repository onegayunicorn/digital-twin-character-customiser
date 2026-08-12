# Trigger: TagWriteTrigger

> Capability #51 — **Tag Write**

Event source(s) that initiate execution for this capability.

### Trigger: TagAddedTrigger

```typescript
// trigger: TagAddedTrigger
const TagAddedTriggerContract: TriggerContract = {
  triggerId: 'TagAddedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TagAddedTrigger' },
  actionTarget: 'ApplyResourceTagTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: TagUpdatedTrigger

```typescript
// trigger: TagUpdatedTrigger
const TagUpdatedTriggerContract: TriggerContract = {
  triggerId: 'TagUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TagUpdatedTrigger' },
  actionTarget: 'ApplyResourceTagTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/TagWriteProtocol.md) · [Tasks](../tasks/TagWriteTask.md) · [Workflow](../workflows/TagWriteWorkflow.md)
