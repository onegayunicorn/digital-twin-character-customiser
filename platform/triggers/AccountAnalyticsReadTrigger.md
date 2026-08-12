# Trigger: AccountAnalyticsReadTrigger

> Capability #98 — **Account Analytics Read**

Event source(s) that initiate execution for this capability.

### Trigger: AnalyticsReportTrigger

```typescript
// trigger: AnalyticsReportTrigger
const AnalyticsReportTriggerContract: TriggerContract = {
  triggerId: 'AnalyticsReportTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AnalyticsReportTrigger' },
  actionTarget: 'QueryAnalyticsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ScheduleTrigger

```typescript
// trigger: ScheduleTrigger
const ScheduleTriggerContract: TriggerContract = {
  triggerId: 'ScheduleTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ScheduleTrigger' },
  actionTarget: 'QueryAnalyticsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountAnalyticsReadProtocol.md) · [Tasks](../tasks/AccountAnalyticsReadTask.md) · [Workflow](../workflows/AccountAnalyticsReadWorkflow.md)
