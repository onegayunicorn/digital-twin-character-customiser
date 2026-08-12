# Trigger: AccountApiTokensWriteTrigger

> Capability #64 — **Account API Tokens Write**

Event source(s) that initiate execution for this capability.

### Trigger: TokenCreatedTrigger

```typescript
// trigger: TokenCreatedTrigger
const TokenCreatedTriggerContract: TriggerContract = {
  triggerId: 'TokenCreatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TokenCreatedTrigger' },
  actionTarget: 'IssueAPITokenTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: TokenExpiryTrigger

```typescript
// trigger: TokenExpiryTrigger
const TokenExpiryTriggerContract: TriggerContract = {
  triggerId: 'TokenExpiryTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TokenExpiryTrigger' },
  actionTarget: 'IssueAPITokenTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountApiTokensWriteProtocol.md) · [Tasks](../tasks/AccountApiTokensWriteTask.md) · [Workflow](../workflows/AccountApiTokensWriteWorkflow.md)
