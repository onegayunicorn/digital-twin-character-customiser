# Task: EmailRoutingAddressesWriteTask

> Capability #76 — **Email Routing Addresses Write**

Atomic executable unit(s) for this capability.

### Task: ManageEmailRoutingAddressTask

```typescript
// task: ManageEmailRoutingAddressTask
const ManageEmailRoutingAddressTaskSpec: TaskSpecification = {
  taskId: 'ManageEmailRoutingAddressTask',
  operationRef: 'EmailRoutingAddressesWriteProtocol',
  inputSchema: { capability: 'Email Routing Addresses Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageEmailRoutingAddressTask

## Related artifacts
- [Protocol](../protocols/EmailRoutingAddressesWriteProtocol.md) · [Trigger(s)](../triggers/EmailRoutingAddressesWriteTrigger.md) · [Workflow](../workflows/EmailRoutingAddressesWriteWorkflow.md)
