# Task: AccessGroupsWriteTask

> Capability #105 — **Access: Groups Write**

Atomic executable unit(s) for this capability.

### Task: ManageAccessGroupTask

```typescript
// task: ManageAccessGroupTask
const ManageAccessGroupTaskSpec: TaskSpecification = {
  taskId: 'ManageAccessGroupTask',
  operationRef: 'AccessGroupsWriteProtocol',
  inputSchema: { capability: 'Access: Groups Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageAccessGroupTask

## Related artifacts
- [Protocol](../protocols/AccessGroupsWriteProtocol.md) · [Trigger(s)](../triggers/AccessGroupsWriteTrigger.md) · [Workflow](../workflows/AccessGroupsWriteWorkflow.md)
