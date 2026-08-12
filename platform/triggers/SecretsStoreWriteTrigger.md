# Trigger: SecretsStoreWriteTrigger

> Capability #14 — **Secrets Store Write**

Event source(s) that initiate execution for this capability.

### Trigger: SecretUpdatedTrigger

```typescript
// trigger: SecretUpdatedTrigger
const SecretUpdatedTriggerContract: TriggerContract = {
  triggerId: 'SecretUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SecretUpdatedTrigger' },
  actionTarget: 'WriteSecretToStoreTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: SecretExpiryTrigger

```typescript
// trigger: SecretExpiryTrigger
const SecretExpiryTriggerContract: TriggerContract = {
  triggerId: 'SecretExpiryTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SecretExpiryTrigger' },
  actionTarget: 'WriteSecretToStoreTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/SecretsStoreWriteProtocol.md) · [Tasks](../tasks/SecretsStoreWriteTask.md) · [Workflow](../workflows/SecretsStoreWriteWorkflow.md)
