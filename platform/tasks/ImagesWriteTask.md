# Task: ImagesWriteTask

> Capability #80 — **Images Write**

Atomic executable unit(s) for this capability.

### Task: UploadTransformImageTask

```typescript
// task: UploadTransformImageTask
const UploadTransformImageTaskSpec: TaskSpecification = {
  taskId: 'UploadTransformImageTask',
  operationRef: 'ImagesWriteProtocol',
  inputSchema: { capability: 'Images Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UploadTransformImageTask

## Related artifacts
- [Protocol](../protocols/ImagesWriteProtocol.md) · [Trigger(s)](../triggers/ImagesWriteTrigger.md) · [Workflow](../workflows/ImagesWriteWorkflow.md)
