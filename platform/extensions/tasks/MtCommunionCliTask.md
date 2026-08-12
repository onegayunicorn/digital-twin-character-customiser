# Task: MtCommunionCliTask

> Capability #134 — **MT Communion CLI**

Atomic executable unit(s) for this capability.

### Task: RouteIntentTask

```typescript
// task: RouteIntentTask
const RouteIntentTaskSpec: TaskSpecification = {
  taskId: 'RouteIntentTask',
  operationRef: 'MtCommunionCliProtocol',
  inputSchema: { capability: 'MT Communion CLI' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RouteIntentTask

### Task: StoreEngramTask

```typescript
// task: StoreEngramTask
const StoreEngramTaskSpec: TaskSpecification = {
  taskId: 'StoreEngramTask',
  operationRef: 'MtCommunionCliProtocol',
  inputSchema: { capability: 'MT Communion CLI' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute StoreEngramTask

## Related artifacts
- [Protocol](../protocols/MtCommunionCliProtocol.md) · [Trigger(s)](../triggers/MtCommunionCliTrigger.md) · [Workflow](../workflows/MtCommunionCliWorkflow.md)
