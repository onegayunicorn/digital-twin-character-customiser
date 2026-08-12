# Task: IpPrefixesWriteTask

> Capability #88 — **IP Prefixes: Write**

Atomic executable unit(s) for this capability.

### Task: ManageIPPrefixTask

```typescript
// task: ManageIPPrefixTask
const ManageIPPrefixTaskSpec: TaskSpecification = {
  taskId: 'ManageIPPrefixTask',
  operationRef: 'IpPrefixesWriteProtocol',
  inputSchema: { capability: 'IP Prefixes: Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageIPPrefixTask

## Related artifacts
- [Protocol](../protocols/IpPrefixesWriteProtocol.md) · [Trigger(s)](../triggers/IpPrefixesWriteTrigger.md) · [Workflow](../workflows/IpPrefixesWriteWorkflow.md)
