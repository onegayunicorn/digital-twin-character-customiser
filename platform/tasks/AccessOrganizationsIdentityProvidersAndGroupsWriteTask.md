# Task: AccessOrganizationsIdentityProvidersAndGroupsWriteTask

> Capability #109 — **Access: Organizations, Identity Providers, and Groups Write**

Atomic executable unit(s) for this capability.

### Task: SyncOrgIdPGroupTask

```typescript
// task: SyncOrgIdPGroupTask
const SyncOrgIdPGroupTaskSpec: TaskSpecification = {
  taskId: 'SyncOrgIdPGroupTask',
  operationRef: 'AccessOrganizationsIdentityProvidersAndGroupsWriteProtocol',
  inputSchema: { capability: 'Access: Organizations, Identity Providers, and Groups Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute SyncOrgIdPGroupTask

## Related artifacts
- [Protocol](../protocols/AccessOrganizationsIdentityProvidersAndGroupsWriteProtocol.md) · [Trigger(s)](../triggers/AccessOrganizationsIdentityProvidersAndGroupsWriteTrigger.md) · [Workflow](../workflows/AccessOrganizationsIdentityProvidersAndGroupsWriteWorkflow.md)
