# Trigger: AccountCustomPagesWriteTrigger

> Capability #56 — **Account Custom Pages Write**

Event source(s) that initiate execution for this capability.

### Trigger: CustomPageRequestedTrigger

```typescript
// trigger: CustomPageRequestedTrigger
const CustomPageRequestedTriggerContract: TriggerContract = {
  triggerId: 'CustomPageRequestedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for CustomPageRequestedTrigger' },
  actionTarget: 'UploadCustomPageTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: PageUpdatedTrigger

```typescript
// trigger: PageUpdatedTrigger
const PageUpdatedTriggerContract: TriggerContract = {
  triggerId: 'PageUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PageUpdatedTrigger' },
  actionTarget: 'UploadCustomPageTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountCustomPagesWriteProtocol.md) · [Tasks](../tasks/AccountCustomPagesWriteTask.md) · [Workflow](../workflows/AccountCustomPagesWriteWorkflow.md)
