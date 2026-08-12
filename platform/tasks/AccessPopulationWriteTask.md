# Task: AccessPopulationWriteTask

> Capability #112 — **Access: Population Write**

Atomic executable unit(s) for this capability.

### Task: ManageAccessPopulationTask

```typescript
// task: ManageAccessPopulationTask
const ManageAccessPopulationTaskSpec: TaskSpecification = {
  taskId: 'ManageAccessPopulationTask',
  operationRef: 'AccessPopulationWriteProtocol',
  inputSchema: { capability: 'Access: Population Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageAccessPopulationTask

## Related artifacts
- [Protocol](../protocols/AccessPopulationWriteProtocol.md) · [Trigger(s)](../triggers/AccessPopulationWriteTrigger.md) · [Workflow](../workflows/AccessPopulationWriteWorkflow.md)
