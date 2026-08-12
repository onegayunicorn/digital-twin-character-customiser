# Trigger: EmailRoutingSuppressionsWriteTrigger

> Capability #77 — **Email Routing Suppressions Write**

Event source(s) that initiate execution for this capability.

### Trigger: BounceReceivedTrigger

```typescript
// trigger: BounceReceivedTrigger
const BounceReceivedTriggerContract: TriggerContract = {
  triggerId: 'BounceReceivedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for BounceReceivedTrigger' },
  actionTarget: 'ManageEmailSuppressionTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ComplaintTrigger

```typescript
// trigger: ComplaintTrigger
const ComplaintTriggerContract: TriggerContract = {
  triggerId: 'ComplaintTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ComplaintTrigger' },
  actionTarget: 'ManageEmailSuppressionTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/EmailRoutingSuppressionsWriteProtocol.md) · [Tasks](../tasks/EmailRoutingSuppressionsWriteTask.md) · [Workflow](../workflows/EmailRoutingSuppressionsWriteWorkflow.md)
