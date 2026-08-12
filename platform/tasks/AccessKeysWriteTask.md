# Task: AccessKeysWriteTask

> Capability #106 — **Access: Keys Write**

Atomic executable unit(s) for this capability.

### Task: ManageAccessKeyTask

```typescript
// task: ManageAccessKeyTask
const ManageAccessKeyTaskSpec: TaskSpecification = {
  taskId: 'ManageAccessKeyTask',
  operationRef: 'AccessKeysWriteProtocol',
  inputSchema: { capability: 'Access: Keys Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageAccessKeyTask

## Related artifacts
- [Protocol](../protocols/AccessKeysWriteProtocol.md) · [Trigger(s)](../triggers/AccessKeysWriteTrigger.md) · [Workflow](../workflows/AccessKeysWriteWorkflow.md)
