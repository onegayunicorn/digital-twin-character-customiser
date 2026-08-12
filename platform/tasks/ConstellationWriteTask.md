# Task: ConstellationWriteTask

> Capability #27 — **Constellation Write**

Atomic executable unit(s) for this capability.

### Task: UpdateConstellationGraphTask

```typescript
// task: UpdateConstellationGraphTask
const UpdateConstellationGraphTaskSpec: TaskSpecification = {
  taskId: 'UpdateConstellationGraphTask',
  operationRef: 'ConstellationWriteProtocol',
  inputSchema: { capability: 'Constellation Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UpdateConstellationGraphTask

## Related artifacts
- [Protocol](../protocols/ConstellationWriteProtocol.md) · [Trigger(s)](../triggers/ConstellationWriteTrigger.md) · [Workflow](../workflows/ConstellationWriteWorkflow.md)
