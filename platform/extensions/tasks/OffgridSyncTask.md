# Task: OffgridSyncTask

> Capability #159 — **Off-grid Sync**

Atomic executable unit(s) for this capability.

### Task: EnqueueOfflineTask

```typescript
// task: EnqueueOfflineTask
const EnqueueOfflineTaskSpec: TaskSpecification = {
  taskId: 'EnqueueOfflineTask',
  operationRef: 'OffgridSyncProtocol',
  inputSchema: { capability: 'Off-grid Sync' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute EnqueueOfflineTask

### Task: MergeLedgerTask

```typescript
// task: MergeLedgerTask
const MergeLedgerTaskSpec: TaskSpecification = {
  taskId: 'MergeLedgerTask',
  operationRef: 'OffgridSyncProtocol',
  inputSchema: { capability: 'Off-grid Sync' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute MergeLedgerTask

### Task: EnterDisasterModeTask

```typescript
// task: EnterDisasterModeTask
const EnterDisasterModeTaskSpec: TaskSpecification = {
  taskId: 'EnterDisasterModeTask',
  operationRef: 'OffgridSyncProtocol',
  inputSchema: { capability: 'Off-grid Sync' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute EnterDisasterModeTask

## Related artifacts
- [Protocol](../protocols/OffgridSyncProtocol.md) · [Trigger(s)](../triggers/OffgridSyncTrigger.md) · [Workflow](../workflows/OffgridSyncWorkflow.md)
