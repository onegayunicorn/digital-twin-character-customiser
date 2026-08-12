# Task: ZeroTrustSeatsWriteTask

> Capability #130 — **Zero Trust: Seats Write**

Atomic executable unit(s) for this capability.

### Task: ManageZeroTrustSeatTask

```typescript
// task: ManageZeroTrustSeatTask
const ManageZeroTrustSeatTaskSpec: TaskSpecification = {
  taskId: 'ManageZeroTrustSeatTask',
  operationRef: 'ZeroTrustSeatsWriteProtocol',
  inputSchema: { capability: 'Zero Trust: Seats Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageZeroTrustSeatTask

## Related artifacts
- [Protocol](../protocols/ZeroTrustSeatsWriteProtocol.md) · [Trigger(s)](../triggers/ZeroTrustSeatsWriteTrigger.md) · [Workflow](../workflows/ZeroTrustSeatsWriteWorkflow.md)
