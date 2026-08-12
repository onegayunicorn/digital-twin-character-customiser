# Task: Sonar5dMeshTask

> Capability #141 — **Sonar 5D Mesh**

Atomic executable unit(s) for this capability.

### Task: GenerateMeshTask

```typescript
// task: GenerateMeshTask
const GenerateMeshTaskSpec: TaskSpecification = {
  taskId: 'GenerateMeshTask',
  operationRef: 'Sonar5dMeshProtocol',
  inputSchema: { capability: 'Sonar 5D Mesh' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute GenerateMeshTask

### Task: RunSweepTask

```typescript
// task: RunSweepTask
const RunSweepTaskSpec: TaskSpecification = {
  taskId: 'RunSweepTask',
  operationRef: 'Sonar5dMeshProtocol',
  inputSchema: { capability: 'Sonar 5D Mesh' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RunSweepTask

### Task: ExportObjTask

```typescript
// task: ExportObjTask
const ExportObjTaskSpec: TaskSpecification = {
  taskId: 'ExportObjTask',
  operationRef: 'Sonar5dMeshProtocol',
  inputSchema: { capability: 'Sonar 5D Mesh' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ExportObjTask

## Related artifacts
- [Protocol](../protocols/Sonar5dMeshProtocol.md) · [Trigger(s)](../triggers/Sonar5dMeshTrigger.md) · [Workflow](../workflows/Sonar5dMeshWorkflow.md)
