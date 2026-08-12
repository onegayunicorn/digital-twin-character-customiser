# Task: WorkersScriptsWriteTask

> Capability #8 — **Workers Scripts Write**

Atomic executable unit(s) for this capability.

### Task: UploadUpdateWorkerScriptTask

```typescript
// task: UploadUpdateWorkerScriptTask
const UploadUpdateWorkerScriptTaskSpec: TaskSpecification = {
  taskId: 'UploadUpdateWorkerScriptTask',
  operationRef: 'WorkersScriptsWriteProtocol',
  inputSchema: { capability: 'Workers Scripts Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UploadUpdateWorkerScriptTask

## Related artifacts
- [Protocol](../protocols/WorkersScriptsWriteProtocol.md) · [Trigger(s)](../triggers/WorkersScriptsWriteTrigger.md) · [Workflow](../workflows/WorkersScriptsWriteWorkflow.md)
