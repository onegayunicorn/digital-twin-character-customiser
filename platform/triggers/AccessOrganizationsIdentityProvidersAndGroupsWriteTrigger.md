# Trigger: AccessOrganizationsIdentityProvidersAndGroupsWriteTrigger

> Capability #109 — **Access: Organizations, Identity Providers, and Groups Write**

Event source(s) that initiate execution for this capability.

### Trigger: OrgStructureUpdatedTrigger

```typescript
// trigger: OrgStructureUpdatedTrigger
const OrgStructureUpdatedTriggerContract: TriggerContract = {
  triggerId: 'OrgStructureUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for OrgStructureUpdatedTrigger' },
  actionTarget: 'SyncOrgIdPGroupTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessOrganizationsIdentityProvidersAndGroupsWriteProtocol.md) · [Tasks](../tasks/AccessOrganizationsIdentityProvidersAndGroupsWriteTask.md) · [Workflow](../workflows/AccessOrganizationsIdentityProvidersAndGroupsWriteWorkflow.md)
