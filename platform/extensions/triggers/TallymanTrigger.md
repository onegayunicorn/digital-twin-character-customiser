# Trigger: TallymanTrigger

> Capability #147 — **Tallyman**

Event source(s) that initiate execution for this capability.

### Trigger: TallyRequestTrigger

```typescript
// trigger: TallyRequestTrigger
const TallyRequestTriggerContract: TriggerContract = {
  triggerId: 'TallyRequestTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TallyRequestTrigger' },
  actionTarget: 'AggregateMetricsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/TallymanProtocol.md) · [Tasks](../tasks/TallymanTask.md) · [Workflow](../workflows/TallymanWorkflow.md)
