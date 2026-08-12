# Task: QueuesWriteTask

> Capability #23 — **Queues Write**

Atomic executable unit(s) for this capability.

### Task: EnqueueMessageTask

```typescript
// task: EnqueueMessageTask
const EnqueueMessageTaskSpec: TaskSpecification = {
  taskId: 'EnqueueMessageTask',
  operationRef: 'QueuesWriteProtocol',
  inputSchema: { capability: 'Queues Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute EnqueueMessageTask

### Task: ManageQueueTask

```typescript
// task: ManageQueueTask
const ManageQueueTaskSpec: TaskSpecification = {
  taskId: 'ManageQueueTask',
  operationRef: 'QueuesWriteProtocol',
  inputSchema: { capability: 'Queues Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageQueueTask

## Related artifacts
- [Protocol](../protocols/QueuesWriteProtocol.md) · [Trigger(s)](../triggers/QueuesWriteTrigger.md) · [Workflow](../workflows/QueuesWriteWorkflow.md)
