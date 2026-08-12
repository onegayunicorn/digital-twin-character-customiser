# Trigger: AccountWaitingRoomsReadTrigger

> Capability #85 — **Account Waiting Rooms Read**

Event source(s) that initiate execution for this capability.

### Trigger: WaitingRoomEventTrigger

```typescript
// trigger: WaitingRoomEventTrigger
const WaitingRoomEventTriggerContract: TriggerContract = {
  triggerId: 'WaitingRoomEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for WaitingRoomEventTrigger' },
  actionTarget: 'ReadWaitingRoomMetricsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountWaitingRoomsReadProtocol.md) · [Tasks](../tasks/AccountWaitingRoomsReadTask.md) · [Workflow](../workflows/AccountWaitingRoomsReadWorkflow.md)
