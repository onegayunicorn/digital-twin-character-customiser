# Task: AccountCustomAssetWriteTask

> Capability #65 — **Account Custom Asset Write**

Atomic executable unit(s) for this capability.

### Task: UploadCustomAssetTask

```typescript
// task: UploadCustomAssetTask
const UploadCustomAssetTaskSpec: TaskSpecification = {
  taskId: 'UploadCustomAssetTask',
  operationRef: 'AccountCustomAssetWriteProtocol',
  inputSchema: { capability: 'Account Custom Asset Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UploadCustomAssetTask

## Related artifacts
- [Protocol](../protocols/AccountCustomAssetWriteProtocol.md) · [Trigger(s)](../triggers/AccountCustomAssetWriteTrigger.md) · [Workflow](../workflows/AccountCustomAssetWriteWorkflow.md)
