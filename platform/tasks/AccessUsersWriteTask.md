# Task: AccessUsersWriteTask

> Capability #118 — **Access: Users Write**

Atomic executable unit(s) for this capability.

### Task: ManageAccessUserTask

```typescript
// task: ManageAccessUserTask
const ManageAccessUserTaskSpec: TaskSpecification = {
  taskId: 'ManageAccessUserTask',
  operationRef: 'AccessUsersWriteProtocol',
  inputSchema: { capability: 'Access: Users Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageAccessUserTask

## Related artifacts
- [Protocol](../protocols/AccessUsersWriteProtocol.md) · [Trigger(s)](../triggers/AccessUsersWriteTrigger.md) · [Workflow](../workflows/AccessUsersWriteWorkflow.md)
