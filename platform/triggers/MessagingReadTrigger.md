# Trigger: MessagingReadTrigger

> Capability #21 — **Messaging Read**

Event source(s) that initiate execution for this capability.

### Trigger: MessageAvailableTrigger

```typescript
// trigger: MessageAvailableTrigger
const MessageAvailableTriggerContract: TriggerContract = {
  triggerId: 'MessageAvailableTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MessageAvailableTrigger' },
  actionTarget: 'ReadMessageTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: MessageReceivedTrigger

```typescript
// trigger: MessageReceivedTrigger
const MessageReceivedTriggerContract: TriggerContract = {
  triggerId: 'MessageReceivedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MessageReceivedTrigger' },
  actionTarget: 'ReadMessageTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MessagingReadProtocol.md) · [Tasks](../tasks/MessagingReadTask.md) · [Workflow](../workflows/MessagingReadWorkflow.md)
