# Task: OneNetworksWriteTask

> Capability #125 — **One Networks Write**

Atomic executable unit(s) for this capability.

### Task: ManageOneNetworkTask

```typescript
// task: ManageOneNetworkTask
const ManageOneNetworkTaskSpec: TaskSpecification = {
  taskId: 'ManageOneNetworkTask',
  operationRef: 'OneNetworksWriteProtocol',
  inputSchema: { capability: 'One Networks Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageOneNetworkTask

## Related artifacts
- [Protocol](../protocols/OneNetworksWriteProtocol.md) · [Trigger(s)](../triggers/OneNetworksWriteTrigger.md) · [Workflow](../workflows/OneNetworksWriteWorkflow.md)
