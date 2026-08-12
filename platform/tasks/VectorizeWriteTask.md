# Task: VectorizeWriteTask

> Capability #20 — **Vectorize Write**

Atomic executable unit(s) for this capability.

### Task: IngestVectorsTask

```typescript
// task: IngestVectorsTask
const IngestVectorsTaskSpec: TaskSpecification = {
  taskId: 'IngestVectorsTask',
  operationRef: 'VectorizeWriteProtocol',
  inputSchema: { capability: 'Vectorize Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute IngestVectorsTask

### Task: BuildVectorIndexTask

```typescript
// task: BuildVectorIndexTask
const BuildVectorIndexTaskSpec: TaskSpecification = {
  taskId: 'BuildVectorIndexTask',
  operationRef: 'VectorizeWriteProtocol',
  inputSchema: { capability: 'Vectorize Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute BuildVectorIndexTask

## Related artifacts
- [Protocol](../protocols/VectorizeWriteProtocol.md) · [Trigger(s)](../triggers/VectorizeWriteTrigger.md) · [Workflow](../workflows/VectorizeWriteWorkflow.md)
