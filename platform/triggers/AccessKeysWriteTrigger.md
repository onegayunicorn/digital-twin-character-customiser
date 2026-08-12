# Trigger: AccessKeysWriteTrigger

> Capability #106 — **Access: Keys Write**

Event source(s) that initiate execution for this capability.

### Trigger: AccessKeyCreatedTrigger

```typescript
// trigger: AccessKeyCreatedTrigger
const AccessKeyCreatedTriggerContract: TriggerContract = {
  triggerId: 'AccessKeyCreatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AccessKeyCreatedTrigger' },
  actionTarget: 'ManageAccessKeyTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessKeysWriteProtocol.md) · [Tasks](../tasks/AccessKeysWriteTask.md) · [Workflow](../workflows/AccessKeysWriteWorkflow.md)
