# Task: WebsearchWriteTask

> Capability #6 — **Websearch Write**

Atomic executable unit(s) for this capability.

### Task: UpdateWebsearchConfigTask

```typescript
// task: UpdateWebsearchConfigTask
const UpdateWebsearchConfigTaskSpec: TaskSpecification = {
  taskId: 'UpdateWebsearchConfigTask',
  operationRef: 'WebsearchWriteProtocol',
  inputSchema: { capability: 'Websearch Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UpdateWebsearchConfigTask

## Related artifacts
- [Protocol](../protocols/WebsearchWriteProtocol.md) · [Trigger(s)](../triggers/WebsearchWriteTrigger.md) · [Workflow](../workflows/WebsearchWriteWorkflow.md)
