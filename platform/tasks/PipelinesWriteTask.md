# Task: PipelinesWriteTask

> Capability #12 — **Pipelines Write**

Atomic executable unit(s) for this capability.

### Task: ManagePipelineTask

```typescript
// task: ManagePipelineTask
const ManagePipelineTaskSpec: TaskSpecification = {
  taskId: 'ManagePipelineTask',
  operationRef: 'PipelinesWriteProtocol',
  inputSchema: { capability: 'Pipelines Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManagePipelineTask

## Related artifacts
- [Protocol](../protocols/PipelinesWriteProtocol.md) · [Trigger(s)](../triggers/PipelinesWriteTrigger.md) · [Workflow](../workflows/PipelinesWriteWorkflow.md)
