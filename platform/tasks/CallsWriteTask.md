# Task: CallsWriteTask

> Capability #79 — **Calls Write**

Atomic executable unit(s) for this capability.

### Task: ManageCallSessionTask

```typescript
// task: ManageCallSessionTask
const ManageCallSessionTaskSpec: TaskSpecification = {
  taskId: 'ManageCallSessionTask',
  operationRef: 'CallsWriteProtocol',
  inputSchema: { capability: 'Calls Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageCallSessionTask

## Related artifacts
- [Protocol](../protocols/CallsWriteProtocol.md) · [Trigger(s)](../triggers/CallsWriteTrigger.md) · [Workflow](../workflows/CallsWriteWorkflow.md)
