# Task: WorkersObservabilityWriteTask

> Capability #24 — **Workers Observability Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureObservabilityTask

```typescript
// task: ConfigureObservabilityTask
const ConfigureObservabilityTaskSpec: TaskSpecification = {
  taskId: 'ConfigureObservabilityTask',
  operationRef: 'WorkersObservabilityWriteProtocol',
  inputSchema: { capability: 'Workers Observability Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureObservabilityTask

## Related artifacts
- [Protocol](../protocols/WorkersObservabilityWriteProtocol.md) · [Trigger(s)](../triggers/WorkersObservabilityWriteTrigger.md) · [Workflow](../workflows/WorkersObservabilityWriteWorkflow.md)
