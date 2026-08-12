# Task: PipelineRunnerTask

> Capability #153 — **Pipeline Runner**

Atomic executable unit(s) for this capability.

### Task: ExecutePipelineTask

```typescript
// task: ExecutePipelineTask
const ExecutePipelineTaskSpec: TaskSpecification = {
  taskId: 'ExecutePipelineTask',
  operationRef: 'PipelineRunnerProtocol',
  inputSchema: { capability: 'Pipeline Runner' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ExecutePipelineTask

### Task: GateDependenciesTask

```typescript
// task: GateDependenciesTask
const GateDependenciesTaskSpec: TaskSpecification = {
  taskId: 'GateDependenciesTask',
  operationRef: 'PipelineRunnerProtocol',
  inputSchema: { capability: 'Pipeline Runner' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute GateDependenciesTask

## Related artifacts
- [Protocol](../protocols/PipelineRunnerProtocol.md) · [Trigger(s)](../triggers/PipelineRunnerTrigger.md) · [Workflow](../workflows/PipelineRunnerWorkflow.md)
