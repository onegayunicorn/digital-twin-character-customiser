# Task: OneConnectorsWriteTask

> Capability #124 — **One Connectors Write**

Atomic executable unit(s) for this capability.

### Task: ManageOneConnectorTask

```typescript
// task: ManageOneConnectorTask
const ManageOneConnectorTaskSpec: TaskSpecification = {
  taskId: 'ManageOneConnectorTask',
  operationRef: 'OneConnectorsWriteProtocol',
  inputSchema: { capability: 'One Connectors Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageOneConnectorTask

## Related artifacts
- [Protocol](../protocols/OneConnectorsWriteProtocol.md) · [Trigger(s)](../triggers/OneConnectorsWriteTrigger.md) · [Workflow](../workflows/OneConnectorsWriteWorkflow.md)
