# Task: AccessTagsWriteTask

> Capability #117 — **Access: Tags Write**

Atomic executable unit(s) for this capability.

### Task: ApplyAccessTagTask

```typescript
// task: ApplyAccessTagTask
const ApplyAccessTagTaskSpec: TaskSpecification = {
  taskId: 'ApplyAccessTagTask',
  operationRef: 'AccessTagsWriteProtocol',
  inputSchema: { capability: 'Access: Tags Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ApplyAccessTagTask

## Related artifacts
- [Protocol](../protocols/AccessTagsWriteProtocol.md) · [Trigger(s)](../triggers/AccessTagsWriteTrigger.md) · [Workflow](../workflows/AccessTagsWriteWorkflow.md)
