# Task: DdosProtectionWriteTask

> Capability #43 — **DDoS Protection Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureDDoSProtectionTask

```typescript
// task: ConfigureDDoSProtectionTask
const ConfigureDDoSProtectionTaskSpec: TaskSpecification = {
  taskId: 'ConfigureDDoSProtectionTask',
  operationRef: 'DdosProtectionWriteProtocol',
  inputSchema: { capability: 'DDoS Protection Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureDDoSProtectionTask

## Related artifacts
- [Protocol](../protocols/DdosProtectionWriteProtocol.md) · [Trigger(s)](../triggers/DdosProtectionWriteTrigger.md) · [Workflow](../workflows/DdosProtectionWriteWorkflow.md)
