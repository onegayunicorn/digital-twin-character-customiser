# Task: TwinEngineSyncTask

> Capability #132 — **Twin Engine Sync**

Atomic executable unit(s) for this capability.

### Task: SyncTwinStateTask

```typescript
// task: SyncTwinStateTask
const SyncTwinStateTaskSpec: TaskSpecification = {
  taskId: 'SyncTwinStateTask',
  operationRef: 'TwinEngineSyncProtocol',
  inputSchema: { capability: 'Twin Engine Sync' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute SyncTwinStateTask

### Task: DetectStaleTwinTask

```typescript
// task: DetectStaleTwinTask
const DetectStaleTwinTaskSpec: TaskSpecification = {
  taskId: 'DetectStaleTwinTask',
  operationRef: 'TwinEngineSyncProtocol',
  inputSchema: { capability: 'Twin Engine Sync' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute DetectStaleTwinTask

## Related artifacts
- [Protocol](../protocols/TwinEngineSyncProtocol.md) · [Trigger(s)](../triggers/TwinEngineSyncTrigger.md) · [Workflow](../workflows/TwinEngineSyncWorkflow.md)
