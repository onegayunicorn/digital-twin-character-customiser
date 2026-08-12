# Trigger: AccessOrganizationsWriteTrigger

> Capability #108 — **Access: Organizations Write**

Event source(s) that initiate execution for this capability.

### Trigger: OrganizationCreatedTrigger

```typescript
// trigger: OrganizationCreatedTrigger
const OrganizationCreatedTriggerContract: TriggerContract = {
  triggerId: 'OrganizationCreatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for OrganizationCreatedTrigger' },
  actionTarget: 'ManageAccessOrganizationTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessOrganizationsWriteProtocol.md) · [Tasks](../tasks/AccessOrganizationsWriteTask.md) · [Workflow](../workflows/AccessOrganizationsWriteWorkflow.md)
