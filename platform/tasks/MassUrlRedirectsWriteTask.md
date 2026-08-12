# Task: MassUrlRedirectsWriteTask

> Capability #60 — **Mass URL Redirects Write**

Atomic executable unit(s) for this capability.

### Task: ImportRedirectsTask

```typescript
// task: ImportRedirectsTask
const ImportRedirectsTaskSpec: TaskSpecification = {
  taskId: 'ImportRedirectsTask',
  operationRef: 'MassUrlRedirectsWriteProtocol',
  inputSchema: { capability: 'Mass URL Redirects Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ImportRedirectsTask

## Related artifacts
- [Protocol](../protocols/MassUrlRedirectsWriteProtocol.md) · [Trigger(s)](../triggers/MassUrlRedirectsWriteTrigger.md) · [Workflow](../workflows/MassUrlRedirectsWriteWorkflow.md)
