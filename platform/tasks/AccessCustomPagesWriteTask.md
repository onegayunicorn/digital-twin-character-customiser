# Task: AccessCustomPagesWriteTask

> Capability #103 — **Access: Custom Pages Write**

Atomic executable unit(s) for this capability.

### Task: UploadAccessCustomPageTask

```typescript
// task: UploadAccessCustomPageTask
const UploadAccessCustomPageTaskSpec: TaskSpecification = {
  taskId: 'UploadAccessCustomPageTask',
  operationRef: 'AccessCustomPagesWriteProtocol',
  inputSchema: { capability: 'Access: Custom Pages Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UploadAccessCustomPageTask

## Related artifacts
- [Protocol](../protocols/AccessCustomPagesWriteProtocol.md) · [Trigger(s)](../triggers/AccessCustomPagesWriteTrigger.md) · [Workflow](../workflows/AccessCustomPagesWriteWorkflow.md)
