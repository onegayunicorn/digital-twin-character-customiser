# Task: CancerDynamicsTask

> Capability #140 — **Cancer Dynamics**

Atomic executable unit(s) for this capability.

### Task: RunGrowthSimTask

```typescript
// task: RunGrowthSimTask
const RunGrowthSimTaskSpec: TaskSpecification = {
  taskId: 'RunGrowthSimTask',
  operationRef: 'CancerDynamicsProtocol',
  inputSchema: { capability: 'Cancer Dynamics' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RunGrowthSimTask

### Task: DetectReboundTask

```typescript
// task: DetectReboundTask
const DetectReboundTaskSpec: TaskSpecification = {
  taskId: 'DetectReboundTask',
  operationRef: 'CancerDynamicsProtocol',
  inputSchema: { capability: 'Cancer Dynamics' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute DetectReboundTask

## Related artifacts
- [Protocol](../protocols/CancerDynamicsProtocol.md) · [Trigger(s)](../triggers/CancerDynamicsTrigger.md) · [Workflow](../workflows/CancerDynamicsWorkflow.md)
