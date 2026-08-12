# Trigger: NotificationsWriteTrigger

> Capability #69 — **Notifications Write**

Event source(s) that initiate execution for this capability.

### Trigger: NotificationEventTrigger

```typescript
// trigger: NotificationEventTrigger
const NotificationEventTriggerContract: TriggerContract = {
  triggerId: 'NotificationEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for NotificationEventTrigger' },
  actionTarget: 'ConfigureNotificationTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/NotificationsWriteProtocol.md) · [Tasks](../tasks/NotificationsWriteTask.md) · [Workflow](../workflows/NotificationsWriteWorkflow.md)
