# Task: SsoConnectorWriteTask

> Capability #72 — **SSO Connector Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureSSOConnectorTask

```typescript
// task: ConfigureSSOConnectorTask
const ConfigureSSOConnectorTaskSpec: TaskSpecification = {
  taskId: 'ConfigureSSOConnectorTask',
  operationRef: 'SsoConnectorWriteProtocol',
  inputSchema: { capability: 'SSO Connector Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureSSOConnectorTask

## Related artifacts
- [Protocol](../protocols/SsoConnectorWriteProtocol.md) · [Trigger(s)](../triggers/SsoConnectorWriteTrigger.md) · [Workflow](../workflows/SsoConnectorWriteWorkflow.md)
