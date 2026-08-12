# Trigger: EmailSendingWriteTrigger

> Capability #78 — **Email Sending Write**

Event source(s) that initiate execution for this capability.

### Trigger: EmailSendTrigger

```typescript
// trigger: EmailSendTrigger
const EmailSendTriggerContract: TriggerContract = {
  triggerId: 'EmailSendTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for EmailSendTrigger' },
  actionTarget: 'SendEmailTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: DeliveryEventTrigger

```typescript
// trigger: DeliveryEventTrigger
const DeliveryEventTriggerContract: TriggerContract = {
  triggerId: 'DeliveryEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DeliveryEventTrigger' },
  actionTarget: 'SendEmailTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/EmailSendingWriteProtocol.md) · [Tasks](../tasks/EmailSendingWriteTask.md) · [Workflow](../workflows/EmailSendingWriteWorkflow.md)
