# Task: StreamWriteTask

> Capability #82 — **Stream Write**

Atomic executable unit(s) for this capability.

### Task: ManageStreamTask

```typescript
// task: ManageStreamTask
const ManageStreamTaskSpec: TaskSpecification = {
  taskId: 'ManageStreamTask',
  operationRef: 'StreamWriteProtocol',
  inputSchema: { capability: 'Stream Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageStreamTask

## Related artifacts
- [Protocol](../protocols/StreamWriteProtocol.md) · [Trigger(s)](../triggers/StreamWriteTrigger.md) · [Workflow](../workflows/StreamWriteWorkflow.md)
