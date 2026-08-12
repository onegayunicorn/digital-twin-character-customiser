# Task: AccessOrganizationsWriteTask

> Capability #108 — **Access: Organizations Write**

Atomic executable unit(s) for this capability.

### Task: ManageAccessOrganizationTask

```typescript
// task: ManageAccessOrganizationTask
const ManageAccessOrganizationTaskSpec: TaskSpecification = {
  taskId: 'ManageAccessOrganizationTask',
  operationRef: 'AccessOrganizationsWriteProtocol',
  inputSchema: { capability: 'Access: Organizations Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageAccessOrganizationTask

## Related artifacts
- [Protocol](../protocols/AccessOrganizationsWriteProtocol.md) · [Trigger(s)](../triggers/AccessOrganizationsWriteTrigger.md) · [Workflow](../workflows/AccessOrganizationsWriteWorkflow.md)
