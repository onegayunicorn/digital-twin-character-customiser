# Trigger: FlagshipWriteTrigger

> Capability #28 — **Flagship Write**

Event source(s) that initiate execution for this capability.

### Trigger: FlagChangedTrigger

```typescript
// trigger: FlagChangedTrigger
const FlagChangedTriggerContract: TriggerContract = {
  triggerId: 'FlagChangedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for FlagChangedTrigger' },
  actionTarget: 'ManageFeatureFlagTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ScheduleFlagTrigger

```typescript
// trigger: ScheduleFlagTrigger
const ScheduleFlagTriggerContract: TriggerContract = {
  triggerId: 'ScheduleFlagTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ScheduleFlagTrigger' },
  actionTarget: 'ManageFeatureFlagTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/FlagshipWriteProtocol.md) · [Tasks](../tasks/FlagshipWriteTask.md) · [Workflow](../workflows/FlagshipWriteWorkflow.md)
