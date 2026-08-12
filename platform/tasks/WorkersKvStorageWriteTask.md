# Task: WorkersKvStorageWriteTask

> Capability #16 — **Workers KV Storage Write**

Atomic executable unit(s) for this capability.

### Task: WriteKVEntryTask

```typescript
// task: WriteKVEntryTask
const WriteKVEntryTaskSpec: TaskSpecification = {
  taskId: 'WriteKVEntryTask',
  operationRef: 'WorkersKvStorageWriteProtocol',
  inputSchema: { capability: 'Workers KV Storage Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute WriteKVEntryTask

### Task: BulkWriteKVTask

```typescript
// task: BulkWriteKVTask
const BulkWriteKVTaskSpec: TaskSpecification = {
  taskId: 'BulkWriteKVTask',
  operationRef: 'WorkersKvStorageWriteProtocol',
  inputSchema: { capability: 'Workers KV Storage Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute BulkWriteKVTask

## Related artifacts
- [Protocol](../protocols/WorkersKvStorageWriteProtocol.md) · [Trigger(s)](../triggers/WorkersKvStorageWriteTrigger.md) · [Workflow](../workflows/WorkersKvStorageWriteWorkflow.md)
