# Task: TagWriteTask

> Capability #51 — **Tag Write**

Atomic executable unit(s) for this capability.

### Task: ApplyResourceTagTask

```typescript
// task: ApplyResourceTagTask
const ApplyResourceTagTaskSpec: TaskSpecification = {
  taskId: 'ApplyResourceTagTask',
  operationRef: 'TagWriteProtocol',
  inputSchema: { capability: 'Tag Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ApplyResourceTagTask

## Related artifacts
- [Protocol](../protocols/TagWriteProtocol.md) · [Trigger(s)](../triggers/TagWriteTrigger.md) · [Workflow](../workflows/TagWriteWorkflow.md)
