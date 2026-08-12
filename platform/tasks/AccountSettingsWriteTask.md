# Task: AccountSettingsWriteTask

> Capability #66 — **Account Settings Write**

Atomic executable unit(s) for this capability.

### Task: UpdateAccountSettingTask

```typescript
// task: UpdateAccountSettingTask
const UpdateAccountSettingTaskSpec: TaskSpecification = {
  taskId: 'UpdateAccountSettingTask',
  operationRef: 'AccountSettingsWriteProtocol',
  inputSchema: { capability: 'Account Settings Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UpdateAccountSettingTask

## Related artifacts
- [Protocol](../protocols/AccountSettingsWriteProtocol.md) · [Trigger(s)](../triggers/AccountSettingsWriteTrigger.md) · [Workflow](../workflows/AccountSettingsWriteWorkflow.md)
