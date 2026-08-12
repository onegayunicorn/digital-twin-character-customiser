# Trigger: WatcherTrigger

> Capability #146 — **Watcher**

Event source(s) that initiate execution for this capability.

### Trigger: HealthCheckTrigger

```typescript
// trigger: HealthCheckTrigger
const HealthCheckTriggerContract: TriggerContract = {
  triggerId: 'HealthCheckTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for HealthCheckTrigger' },
  actionTarget: 'ScanHeartbeatsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: SpecDriftTrigger

```typescript
// trigger: SpecDriftTrigger
const SpecDriftTriggerContract: TriggerContract = {
  triggerId: 'SpecDriftTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SpecDriftTrigger' },
  actionTarget: 'ScanHeartbeatsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WatcherProtocol.md) · [Tasks](../tasks/WatcherTask.md) · [Workflow](../workflows/WatcherWorkflow.md)
