# Task: OneWriteTask

> Capability #41 — **One Write**

Atomic executable unit(s) for this capability.

### Task: UpdateCloudflareOneConfigTask

```typescript
// task: UpdateCloudflareOneConfigTask
const UpdateCloudflareOneConfigTaskSpec: TaskSpecification = {
  taskId: 'UpdateCloudflareOneConfigTask',
  operationRef: 'OneWriteProtocol',
  inputSchema: { capability: 'One Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UpdateCloudflareOneConfigTask

## Related artifacts
- [Protocol](../protocols/OneWriteProtocol.md) · [Trigger(s)](../triggers/OneWriteTrigger.md) · [Workflow](../workflows/OneWriteWorkflow.md)
