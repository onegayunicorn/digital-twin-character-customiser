# Task: AccountWafWriteTask

> Capability #38 — **Account WAF Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureWAFTask

```typescript
// task: ConfigureWAFTask
const ConfigureWAFTaskSpec: TaskSpecification = {
  taskId: 'ConfigureWAFTask',
  operationRef: 'AccountWafWriteProtocol',
  inputSchema: { capability: 'Account WAF Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureWAFTask

## Related artifacts
- [Protocol](../protocols/AccountWafWriteProtocol.md) · [Trigger(s)](../triggers/AccountWafWriteTrigger.md) · [Workflow](../workflows/AccountWafWriteWorkflow.md)
