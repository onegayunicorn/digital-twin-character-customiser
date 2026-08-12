# Task: WorkersR2StorageWriteTask

> Capability #17 — **Workers R2 Storage Write**

Atomic executable unit(s) for this capability.

### Task: UploadR2ObjectTask

```typescript
// task: UploadR2ObjectTask
const UploadR2ObjectTaskSpec: TaskSpecification = {
  taskId: 'UploadR2ObjectTask',
  operationRef: 'WorkersR2StorageWriteProtocol',
  inputSchema: { capability: 'Workers R2 Storage Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UploadR2ObjectTask

### Task: ManageR2BucketTask

```typescript
// task: ManageR2BucketTask
const ManageR2BucketTaskSpec: TaskSpecification = {
  taskId: 'ManageR2BucketTask',
  operationRef: 'WorkersR2StorageWriteProtocol',
  inputSchema: { capability: 'Workers R2 Storage Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageR2BucketTask

## Related artifacts
- [Protocol](../protocols/WorkersR2StorageWriteProtocol.md) · [Trigger(s)](../triggers/WorkersR2StorageWriteTrigger.md) · [Workflow](../workflows/WorkersR2StorageWriteWorkflow.md)
