# Task: CdsComputeAccountWriteTask

> Capability #121 — **CDS Compute Account Write**

Atomic executable unit(s) for this capability.

### Task: DeployCDSComputeTask

```typescript
// task: DeployCDSComputeTask
const DeployCDSComputeTaskSpec: TaskSpecification = {
  taskId: 'DeployCDSComputeTask',
  operationRef: 'CdsComputeAccountWriteProtocol',
  inputSchema: { capability: 'CDS Compute Account Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute DeployCDSComputeTask

## Related artifacts
- [Protocol](../protocols/CdsComputeAccountWriteProtocol.md) · [Trigger(s)](../triggers/CdsComputeAccountWriteTrigger.md) · [Workflow](../workflows/CdsComputeAccountWriteWorkflow.md)
