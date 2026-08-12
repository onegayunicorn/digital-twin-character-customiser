# Trigger: AccessIdentityProvidersWriteTrigger

> Capability #104 — **Access: Identity Providers Write**

Event source(s) that initiate execution for this capability.

### Trigger: IdPConfigUpdatedTrigger

```typescript
// trigger: IdPConfigUpdatedTrigger
const IdPConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'IdPConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for IdPConfigUpdatedTrigger' },
  actionTarget: 'RegisterIdentityProviderTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessIdentityProvidersWriteProtocol.md) · [Tasks](../tasks/AccessIdentityProvidersWriteTask.md) · [Workflow](../workflows/AccessIdentityProvidersWriteWorkflow.md)
