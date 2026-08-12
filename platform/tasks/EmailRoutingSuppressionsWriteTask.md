# Task: EmailRoutingSuppressionsWriteTask

> Capability #77 — **Email Routing Suppressions Write**

Atomic executable unit(s) for this capability.

### Task: ManageEmailSuppressionTask

```typescript
// task: ManageEmailSuppressionTask
const ManageEmailSuppressionTaskSpec: TaskSpecification = {
  taskId: 'ManageEmailSuppressionTask',
  operationRef: 'EmailRoutingSuppressionsWriteProtocol',
  inputSchema: { capability: 'Email Routing Suppressions Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageEmailSuppressionTask

## Related artifacts
- [Protocol](../protocols/EmailRoutingSuppressionsWriteProtocol.md) · [Trigger(s)](../triggers/EmailRoutingSuppressionsWriteTrigger.md) · [Workflow](../workflows/EmailRoutingSuppressionsWriteWorkflow.md)
