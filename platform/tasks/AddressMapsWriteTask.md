# Task: AddressMapsWriteTask

> Capability #84 — **Address Maps Write**

Atomic executable unit(s) for this capability.

### Task: ManageAddressMapTask

```typescript
// task: ManageAddressMapTask
const ManageAddressMapTaskSpec: TaskSpecification = {
  taskId: 'ManageAddressMapTask',
  operationRef: 'AddressMapsWriteProtocol',
  inputSchema: { capability: 'Address Maps Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageAddressMapTask

## Related artifacts
- [Protocol](../protocols/AddressMapsWriteProtocol.md) · [Trigger(s)](../triggers/AddressMapsWriteTrigger.md) · [Workflow](../workflows/AddressMapsWriteWorkflow.md)
