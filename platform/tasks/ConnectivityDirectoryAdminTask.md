# Task: ConnectivityDirectoryAdminTask

> Capability #87 — **Connectivity Directory Admin**

Atomic executable unit(s) for this capability.

### Task: ManageConnectivityDirectoryTask

```typescript
// task: ManageConnectivityDirectoryTask
const ManageConnectivityDirectoryTaskSpec: TaskSpecification = {
  taskId: 'ManageConnectivityDirectoryTask',
  operationRef: 'ConnectivityDirectoryAdminProtocol',
  inputSchema: { capability: 'Connectivity Directory Admin' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageConnectivityDirectoryTask

## Related artifacts
- [Protocol](../protocols/ConnectivityDirectoryAdminProtocol.md) · [Trigger(s)](../triggers/ConnectivityDirectoryAdminTrigger.md) · [Workflow](../workflows/ConnectivityDirectoryAdminWorkflow.md)
