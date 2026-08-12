# Trigger: RealtimeAdminTrigger

> Capability #26 — **Realtime Admin**

Event source(s) that initiate execution for this capability.

### Trigger: ClientConnectedTrigger

```typescript
// trigger: ClientConnectedTrigger
const ClientConnectedTriggerContract: TriggerContract = {
  triggerId: 'ClientConnectedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ClientConnectedTrigger' },
  actionTarget: 'ManageRealtimeSessionTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: RoomEventTrigger

```typescript
// trigger: RoomEventTrigger
const RoomEventTriggerContract: TriggerContract = {
  triggerId: 'RoomEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for RoomEventTrigger' },
  actionTarget: 'ManageRealtimeSessionTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/RealtimeAdminProtocol.md) · [Tasks](../tasks/RealtimeAdminTask.md) · [Workflow](../workflows/RealtimeAdminWorkflow.md)
