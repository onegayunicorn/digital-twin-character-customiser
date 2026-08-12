# Task: SelectConfigurationWriteTask

> Capability #61 — **Select Configuration Write**

Atomic executable unit(s) for this capability.

### Task: UpdateSelectConfigurationTask

```typescript
// task: UpdateSelectConfigurationTask
const UpdateSelectConfigurationTaskSpec: TaskSpecification = {
  taskId: 'UpdateSelectConfigurationTask',
  operationRef: 'SelectConfigurationWriteProtocol',
  inputSchema: { capability: 'Select Configuration Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UpdateSelectConfigurationTask

## Related artifacts
- [Protocol](../protocols/SelectConfigurationWriteProtocol.md) · [Trigger(s)](../triggers/SelectConfigurationWriteTrigger.md) · [Workflow](../workflows/SelectConfigurationWriteWorkflow.md)
