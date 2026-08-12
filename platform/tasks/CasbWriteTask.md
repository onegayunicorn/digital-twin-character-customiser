# Task: CasbWriteTask

> Capability #120 — **CASB Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureCASBIntegrationTask

```typescript
// task: ConfigureCASBIntegrationTask
const ConfigureCASBIntegrationTaskSpec: TaskSpecification = {
  taskId: 'ConfigureCASBIntegrationTask',
  operationRef: 'CasbWriteProtocol',
  inputSchema: { capability: 'CASB Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureCASBIntegrationTask

## Related artifacts
- [Protocol](../protocols/CasbWriteProtocol.md) · [Trigger(s)](../triggers/CasbWriteTrigger.md) · [Workflow](../workflows/CasbWriteWorkflow.md)
