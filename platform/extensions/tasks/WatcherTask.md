# Task: WatcherTask

> Capability #146 — **Watcher**

Atomic executable unit(s) for this capability.

### Task: ScanHeartbeatsTask

```typescript
// task: ScanHeartbeatsTask
const ScanHeartbeatsTaskSpec: TaskSpecification = {
  taskId: 'ScanHeartbeatsTask',
  operationRef: 'WatcherProtocol',
  inputSchema: { capability: 'Watcher' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ScanHeartbeatsTask

### Task: VerifySpecCountsTask

```typescript
// task: VerifySpecCountsTask
const VerifySpecCountsTaskSpec: TaskSpecification = {
  taskId: 'VerifySpecCountsTask',
  operationRef: 'WatcherProtocol',
  inputSchema: { capability: 'Watcher' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute VerifySpecCountsTask

## Related artifacts
- [Protocol](../protocols/WatcherProtocol.md) · [Trigger(s)](../triggers/WatcherTrigger.md) · [Workflow](../workflows/WatcherWorkflow.md)
