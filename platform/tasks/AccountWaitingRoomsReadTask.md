# Task: AccountWaitingRoomsReadTask

> Capability #85 — **Account Waiting Rooms Read**

Atomic executable unit(s) for this capability.

### Task: ReadWaitingRoomMetricsTask

```typescript
// task: ReadWaitingRoomMetricsTask
const ReadWaitingRoomMetricsTaskSpec: TaskSpecification = {
  taskId: 'ReadWaitingRoomMetricsTask',
  operationRef: 'AccountWaitingRoomsReadProtocol',
  inputSchema: { capability: 'Account Waiting Rooms Read' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ReadWaitingRoomMetricsTask

## Related artifacts
- [Protocol](../protocols/AccountWaitingRoomsReadProtocol.md) · [Trigger(s)](../triggers/AccountWaitingRoomsReadTrigger.md) · [Workflow](../workflows/AccountWaitingRoomsReadWorkflow.md)
