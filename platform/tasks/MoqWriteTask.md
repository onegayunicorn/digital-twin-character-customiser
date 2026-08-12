# Task: MoqWriteTask

> Capability #81 — **MoQ Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureMoQEndpointTask

```typescript
// task: ConfigureMoQEndpointTask
const ConfigureMoQEndpointTaskSpec: TaskSpecification = {
  taskId: 'ConfigureMoQEndpointTask',
  operationRef: 'MoqWriteProtocol',
  inputSchema: { capability: 'MoQ Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureMoQEndpointTask

## Related artifacts
- [Protocol](../protocols/MoqWriteProtocol.md) · [Trigger(s)](../triggers/MoqWriteTrigger.md) · [Workflow](../workflows/MoqWriteWorkflow.md)
