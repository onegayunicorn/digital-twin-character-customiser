# Task: WorkersAiWriteTask

> Capability #7 — **Workers AI Write**

Atomic executable unit(s) for this capability.

### Task: DeployWorkersAIModelTask

```typescript
// task: DeployWorkersAIModelTask
const DeployWorkersAIModelTaskSpec: TaskSpecification = {
  taskId: 'DeployWorkersAIModelTask',
  operationRef: 'WorkersAiWriteProtocol',
  inputSchema: { capability: 'Workers AI Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute DeployWorkersAIModelTask

## Related artifacts
- [Protocol](../protocols/WorkersAiWriteProtocol.md) · [Trigger(s)](../triggers/WorkersAiWriteTrigger.md) · [Workflow](../workflows/WorkersAiWriteWorkflow.md)
