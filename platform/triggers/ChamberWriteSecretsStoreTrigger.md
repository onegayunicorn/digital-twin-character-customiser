# Trigger: ChamberWriteSecretsStoreTrigger

> Capability #13 — **Chamber Write -> Secrets Store**

Event source(s) that initiate execution for this capability.

### Trigger: SecretRotatedTrigger

```typescript
// trigger: SecretRotatedTrigger
const SecretRotatedTriggerContract: TriggerContract = {
  triggerId: 'SecretRotatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SecretRotatedTrigger' },
  actionTarget: 'ManageSecretTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: SecretAccessedTrigger

```typescript
// trigger: SecretAccessedTrigger
const SecretAccessedTriggerContract: TriggerContract = {
  triggerId: 'SecretAccessedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SecretAccessedTrigger' },
  actionTarget: 'ManageSecretTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ChamberWriteSecretsStoreProtocol.md) · [Tasks](../tasks/ChamberWriteSecretsStoreTask.md) · [Workflow](../workflows/ChamberWriteSecretsStoreWorkflow.md)
