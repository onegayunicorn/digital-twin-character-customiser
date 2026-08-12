# Trigger: TwinEngineSyncTrigger

> Capability #132 — **Twin Engine Sync**

Event source(s) that initiate execution for this capability.

### Trigger: TwinStateChangedTrigger

```typescript
// trigger: TwinStateChangedTrigger
const TwinStateChangedTriggerContract: TriggerContract = {
  triggerId: 'TwinStateChangedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'on state update' },
  actionTarget: 'SyncTwinStateTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: HeartbeatTimeoutTrigger

```typescript
// trigger: HeartbeatTimeoutTrigger
const HeartbeatTimeoutTriggerContract: TriggerContract = {
  triggerId: 'HeartbeatTimeoutTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for HeartbeatTimeoutTrigger' },
  actionTarget: 'SyncTwinStateTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/TwinEngineSyncProtocol.md) · [Tasks](../tasks/TwinEngineSyncTask.md) · [Workflow](../workflows/TwinEngineSyncWorkflow.md)
