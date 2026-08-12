# Trigger: AccessCustomPagesWriteTrigger

> Capability #103 — **Access: Custom Pages Write**

Event source(s) that initiate execution for this capability.

### Trigger: AccessPageRequestedTrigger

```typescript
// trigger: AccessPageRequestedTrigger
const AccessPageRequestedTriggerContract: TriggerContract = {
  triggerId: 'AccessPageRequestedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AccessPageRequestedTrigger' },
  actionTarget: 'UploadAccessCustomPageTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessCustomPagesWriteProtocol.md) · [Tasks](../tasks/AccessCustomPagesWriteTask.md) · [Workflow](../workflows/AccessCustomPagesWriteWorkflow.md)
