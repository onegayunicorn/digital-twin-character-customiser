# Trigger: AccessTagsWriteTrigger

> Capability #117 — **Access: Tags Write**

Event source(s) that initiate execution for this capability.

### Trigger: AccessTagUpdatedTrigger

```typescript
// trigger: AccessTagUpdatedTrigger
const AccessTagUpdatedTriggerContract: TriggerContract = {
  triggerId: 'AccessTagUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AccessTagUpdatedTrigger' },
  actionTarget: 'ApplyAccessTagTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessTagsWriteProtocol.md) · [Tasks](../tasks/AccessTagsWriteTask.md) · [Workflow](../workflows/AccessTagsWriteWorkflow.md)
