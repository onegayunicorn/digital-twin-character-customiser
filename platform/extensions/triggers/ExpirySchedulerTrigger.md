# Trigger: ExpirySchedulerTrigger

> Capability #167 — **Expiry Scheduler**

Event source(s) that initiate execution for this capability.

### Trigger: ExpiryTickTrigger

```typescript
// trigger: ExpiryTickTrigger
const ExpiryTickTriggerContract: TriggerContract = {
  triggerId: 'ExpiryTickTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ExpiryTickTrigger' },
  actionTarget: 'RegisterAuthorizationTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: AuthorizationCreatedTrigger

```typescript
// trigger: AuthorizationCreatedTrigger
const AuthorizationCreatedTriggerContract: TriggerContract = {
  triggerId: 'AuthorizationCreatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AuthorizationCreatedTrigger' },
  actionTarget: 'RegisterAuthorizationTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ExpirySchedulerProtocol.md) · [Tasks](../tasks/ExpirySchedulerTask.md) · [Workflow](../workflows/ExpirySchedulerWorkflow.md)
