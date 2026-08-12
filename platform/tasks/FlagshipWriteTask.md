# Task: FlagshipWriteTask

> Capability #28 — **Flagship Write**

Atomic executable unit(s) for this capability.

### Task: ManageFeatureFlagTask

```typescript
// task: ManageFeatureFlagTask
const ManageFeatureFlagTaskSpec: TaskSpecification = {
  taskId: 'ManageFeatureFlagTask',
  operationRef: 'FlagshipWriteProtocol',
  inputSchema: { capability: 'Flagship Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageFeatureFlagTask

## Related artifacts
- [Protocol](../protocols/FlagshipWriteProtocol.md) · [Trigger(s)](../triggers/FlagshipWriteTrigger.md) · [Workflow](../workflows/FlagshipWriteWorkflow.md)
