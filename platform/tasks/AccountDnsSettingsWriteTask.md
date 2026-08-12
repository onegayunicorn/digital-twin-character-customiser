# Task: AccountDnsSettingsWriteTask

> Capability #30 — **Account DNS Settings Write**

Atomic executable unit(s) for this capability.

### Task: UpdateDNSSettingTask

```typescript
// task: UpdateDNSSettingTask
const UpdateDNSSettingTaskSpec: TaskSpecification = {
  taskId: 'UpdateDNSSettingTask',
  operationRef: 'AccountDnsSettingsWriteProtocol',
  inputSchema: { capability: 'Account DNS Settings Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UpdateDNSSettingTask

## Related artifacts
- [Protocol](../protocols/AccountDnsSettingsWriteProtocol.md) · [Trigger(s)](../triggers/AccountDnsSettingsWriteTrigger.md) · [Workflow](../workflows/AccountDnsSettingsWriteWorkflow.md)
