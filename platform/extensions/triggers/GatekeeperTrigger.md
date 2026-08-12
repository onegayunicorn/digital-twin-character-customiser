# Trigger: GatekeeperTrigger

> Capability #145 — **Gatekeeper**

Event source(s) that initiate execution for this capability.

### Trigger: ContentSubmittedTrigger

```typescript
// trigger: ContentSubmittedTrigger
const ContentSubmittedTriggerContract: TriggerContract = {
  triggerId: 'ContentSubmittedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ContentSubmittedTrigger' },
  actionTarget: 'CheckClaimsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: AccessRequestTrigger

```typescript
// trigger: AccessRequestTrigger
const AccessRequestTriggerContract: TriggerContract = {
  triggerId: 'AccessRequestTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AccessRequestTrigger' },
  actionTarget: 'CheckClaimsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/GatekeeperProtocol.md) · [Tasks](../tasks/GatekeeperTask.md) · [Workflow](../workflows/GatekeeperWorkflow.md)
