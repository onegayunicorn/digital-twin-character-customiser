# Task: WorkersContainersWriteTask

> Capability #9 — **Workers Containers Write**

Atomic executable unit(s) for this capability.

### Task: DeployWorkerContainerTask

```typescript
// task: DeployWorkerContainerTask
const DeployWorkerContainerTaskSpec: TaskSpecification = {
  taskId: 'DeployWorkerContainerTask',
  operationRef: 'WorkersContainersWriteProtocol',
  inputSchema: { capability: 'Workers Containers Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute DeployWorkerContainerTask

## Related artifacts
- [Protocol](../protocols/WorkersContainersWriteProtocol.md) · [Trigger(s)](../triggers/WorkersContainersWriteTrigger.md) · [Workflow](../workflows/WorkersContainersWriteWorkflow.md)
