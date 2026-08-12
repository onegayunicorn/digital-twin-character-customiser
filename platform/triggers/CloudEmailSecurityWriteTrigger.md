# Trigger: CloudEmailSecurityWriteTrigger

> Capability #74 — **Cloud Email Security: Write**

Event source(s) that initiate execution for this capability.

### Trigger: EmailReceivedTrigger

```typescript
// trigger: EmailReceivedTrigger
const EmailReceivedTriggerContract: TriggerContract = {
  triggerId: 'EmailReceivedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for EmailReceivedTrigger' },
  actionTarget: 'ConfigureEmailSecurityPolicyTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: SecurityAlertTrigger

```typescript
// trigger: SecurityAlertTrigger
const SecurityAlertTriggerContract: TriggerContract = {
  triggerId: 'SecurityAlertTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SecurityAlertTrigger' },
  actionTarget: 'ConfigureEmailSecurityPolicyTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/CloudEmailSecurityWriteProtocol.md) · [Tasks](../tasks/CloudEmailSecurityWriteTask.md) · [Workflow](../workflows/CloudEmailSecurityWriteWorkflow.md)
