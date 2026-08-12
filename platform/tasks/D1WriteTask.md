# Task: D1WriteTask

> Capability #15 — **D1 Write**

Atomic executable unit(s) for this capability.

### Task: ExecuteD1QueryTask

```typescript
// task: ExecuteD1QueryTask
const ExecuteD1QueryTaskSpec: TaskSpecification = {
  taskId: 'ExecuteD1QueryTask',
  operationRef: 'D1WriteProtocol',
  inputSchema: { capability: 'D1 Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ExecuteD1QueryTask

### Task: RunD1MigrationTask

```typescript
// task: RunD1MigrationTask
const RunD1MigrationTaskSpec: TaskSpecification = {
  taskId: 'RunD1MigrationTask',
  operationRef: 'D1WriteProtocol',
  inputSchema: { capability: 'D1 Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RunD1MigrationTask

## Related artifacts
- [Protocol](../protocols/D1WriteProtocol.md) · [Trigger(s)](../triggers/D1WriteTrigger.md) · [Workflow](../workflows/D1WriteWorkflow.md)
