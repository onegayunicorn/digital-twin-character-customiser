# Task: GenesisOptimizerTask

> Capability #142 — **Genesis Optimizer**

Atomic executable unit(s) for this capability.

### Task: RunGaTask

```typescript
// task: RunGaTask
const RunGaTaskSpec: TaskSpecification = {
  taskId: 'RunGaTask',
  operationRef: 'GenesisOptimizerProtocol',
  inputSchema: { capability: 'Genesis Optimizer' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RunGaTask

### Task: RunSpsaTask

```typescript
// task: RunSpsaTask
const RunSpsaTaskSpec: TaskSpecification = {
  taskId: 'RunSpsaTask',
  operationRef: 'GenesisOptimizerProtocol',
  inputSchema: { capability: 'Genesis Optimizer' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RunSpsaTask

## Related artifacts
- [Protocol](../protocols/GenesisOptimizerProtocol.md) · [Trigger(s)](../triggers/GenesisOptimizerTrigger.md) · [Workflow](../workflows/GenesisOptimizerWorkflow.md)
