# Task: HttpApplicationsWriteTask

> Capability #47 — **HTTP Applications Write**

Atomic executable unit(s) for this capability.

### Task: ManageHTTPApplicationTask

```typescript
// task: ManageHTTPApplicationTask
const ManageHTTPApplicationTaskSpec: TaskSpecification = {
  taskId: 'ManageHTTPApplicationTask',
  operationRef: 'HttpApplicationsWriteProtocol',
  inputSchema: { capability: 'HTTP Applications Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageHTTPApplicationTask

## Related artifacts
- [Protocol](../protocols/HttpApplicationsWriteProtocol.md) · [Trigger(s)](../triggers/HttpApplicationsWriteTrigger.md) · [Workflow](../workflows/HttpApplicationsWriteWorkflow.md)
