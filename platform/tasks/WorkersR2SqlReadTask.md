# Task: WorkersR2SqlReadTask

> Capability #18 — **Workers R2 SQL Read**

Atomic executable unit(s) for this capability.

### Task: ExecuteR2SQLQueryTask

```typescript
// task: ExecuteR2SQLQueryTask
const ExecuteR2SQLQueryTaskSpec: TaskSpecification = {
  taskId: 'ExecuteR2SQLQueryTask',
  operationRef: 'WorkersR2SqlReadProtocol',
  inputSchema: { capability: 'Workers R2 SQL Read' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ExecuteR2SQLQueryTask

## Related artifacts
- [Protocol](../protocols/WorkersR2SqlReadProtocol.md) · [Trigger(s)](../triggers/WorkersR2SqlReadTrigger.md) · [Workflow](../workflows/WorkersR2SqlReadWorkflow.md)
