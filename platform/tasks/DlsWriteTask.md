# Task: DlsWriteTask

> Capability #126 — **DLS: Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureDLSPolicyTask

```typescript
// task: ConfigureDLSPolicyTask
const ConfigureDLSPolicyTaskSpec: TaskSpecification = {
  taskId: 'ConfigureDLSPolicyTask',
  operationRef: 'DlsWriteProtocol',
  inputSchema: { capability: 'DLS: Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureDLSPolicyTask

## Related artifacts
- [Protocol](../protocols/DlsWriteProtocol.md) · [Trigger(s)](../triggers/DlsWriteTrigger.md) · [Workflow](../workflows/DlsWriteWorkflow.md)
