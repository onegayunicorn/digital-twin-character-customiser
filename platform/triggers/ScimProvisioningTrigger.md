# Trigger: ScimProvisioningTrigger

> Capability #71 — **SCIM Provisioning**

Event source(s) that initiate execution for this capability.

### Trigger: SCIMSyncTrigger

```typescript
// trigger: SCIMSyncTrigger
const SCIMSyncTriggerContract: TriggerContract = {
  triggerId: 'SCIMSyncTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SCIMSyncTrigger' },
  actionTarget: 'ProvisionSCIMResourceTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: IdentityProviderTrigger

```typescript
// trigger: IdentityProviderTrigger
const IdentityProviderTriggerContract: TriggerContract = {
  triggerId: 'IdentityProviderTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for IdentityProviderTrigger' },
  actionTarget: 'ProvisionSCIMResourceTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ScimProvisioningProtocol.md) · [Tasks](../tasks/ScimProvisioningTask.md) · [Workflow](../workflows/ScimProvisioningWorkflow.md)
