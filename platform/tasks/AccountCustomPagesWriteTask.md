# Task: AccountCustomPagesWriteTask

> Capability #56 — **Account Custom Pages Write**

Atomic executable unit(s) for this capability.

### Task: UploadCustomPageTask

```typescript
// task: UploadCustomPageTask
const UploadCustomPageTaskSpec: TaskSpecification = {
  taskId: 'UploadCustomPageTask',
  operationRef: 'AccountCustomPagesWriteProtocol',
  inputSchema: { capability: 'Account Custom Pages Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UploadCustomPageTask

## Related artifacts
- [Protocol](../protocols/AccountCustomPagesWriteProtocol.md) · [Trigger(s)](../triggers/AccountCustomPagesWriteTrigger.md) · [Workflow](../workflows/AccountCustomPagesWriteWorkflow.md)
