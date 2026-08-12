# Task: IntegrationWriteTask

> Capability #68 — **Integration Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureIntegrationTask

```typescript
// task: ConfigureIntegrationTask
const ConfigureIntegrationTaskSpec: TaskSpecification = {
  taskId: 'ConfigureIntegrationTask',
  operationRef: 'IntegrationWriteProtocol',
  inputSchema: { capability: 'Integration Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureIntegrationTask

## Related artifacts
- [Protocol](../protocols/IntegrationWriteProtocol.md) · [Trigger(s)](../triggers/IntegrationWriteTrigger.md) · [Workflow](../workflows/IntegrationWriteWorkflow.md)
