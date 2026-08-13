# Trigger: MultitenantIsolationTrigger

> Capability #164 — **Multi-Tenant Isolation**

Event source(s) that initiate execution for this capability.

### Trigger: TenantCreatedTrigger

```typescript
// trigger: TenantCreatedTrigger
const TenantCreatedTriggerContract: TriggerContract = {
  triggerId: 'TenantCreatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TenantCreatedTrigger' },
  actionTarget: 'CreateTenantTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MultitenantIsolationProtocol.md) · [Tasks](../tasks/MultitenantIsolationTask.md) · [Workflow](../workflows/MultitenantIsolationWorkflow.md)
