# Task: MatrixIntegrationTask

> Capability #149 — **Matrix Integration**

Atomic executable unit(s) for this capability.

### Task: BuildAdjacencyTask

```typescript
// task: BuildAdjacencyTask
const BuildAdjacencyTaskSpec: TaskSpecification = {
  taskId: 'BuildAdjacencyTask',
  operationRef: 'MatrixIntegrationProtocol',
  inputSchema: { capability: 'Matrix Integration' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute BuildAdjacencyTask

### Task: ComputeGraphMetricsTask

```typescript
// task: ComputeGraphMetricsTask
const ComputeGraphMetricsTaskSpec: TaskSpecification = {
  taskId: 'ComputeGraphMetricsTask',
  operationRef: 'MatrixIntegrationProtocol',
  inputSchema: { capability: 'Matrix Integration' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ComputeGraphMetricsTask

## Related artifacts
- [Protocol](../protocols/MatrixIntegrationProtocol.md) · [Trigger(s)](../triggers/MatrixIntegrationTrigger.md) · [Workflow](../workflows/MatrixIntegrationWorkflow.md)
