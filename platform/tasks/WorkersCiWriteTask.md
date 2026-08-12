# Task: WorkersCiWriteTask

> Capability #10 — **Workers CI Write**

Atomic executable unit(s) for this capability.

### Task: RunWorkersCITask

```typescript
// task: RunWorkersCITask
const RunWorkersCITaskSpec: TaskSpecification = {
  taskId: 'RunWorkersCITask',
  operationRef: 'WorkersCiWriteProtocol',
  inputSchema: { capability: 'Workers CI Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RunWorkersCITask

## Related artifacts
- [Protocol](../protocols/WorkersCiWriteProtocol.md) · [Trigger(s)](../triggers/WorkersCiWriteTrigger.md) · [Workflow](../workflows/WorkersCiWriteWorkflow.md)
