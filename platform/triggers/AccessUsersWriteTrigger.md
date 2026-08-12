# Trigger: AccessUsersWriteTrigger

> Capability #118 — **Access: Users Write**

Event source(s) that initiate execution for this capability.

### Trigger: UserCreatedTrigger

```typescript
// trigger: UserCreatedTrigger
const UserCreatedTriggerContract: TriggerContract = {
  triggerId: 'UserCreatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for UserCreatedTrigger' },
  actionTarget: 'ManageAccessUserTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: UserLoginTrigger

```typescript
// trigger: UserLoginTrigger
const UserLoginTriggerContract: TriggerContract = {
  triggerId: 'UserLoginTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for UserLoginTrigger' },
  actionTarget: 'ManageAccessUserTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessUsersWriteProtocol.md) · [Tasks](../tasks/AccessUsersWriteTask.md) · [Workflow](../workflows/AccessUsersWriteWorkflow.md)
