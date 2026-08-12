# Trigger: RadarReadTrigger

> Capability #97 — **Radar Read**

Event source(s) that initiate execution for this capability.

### Trigger: RadarDataUpdatedTrigger

```typescript
// trigger: RadarDataUpdatedTrigger
const RadarDataUpdatedTriggerContract: TriggerContract = {
  triggerId: 'RadarDataUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for RadarDataUpdatedTrigger' },
  actionTarget: 'ReadRadarDataTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/RadarReadProtocol.md) · [Tasks](../tasks/RadarReadTask.md) · [Workflow](../workflows/RadarReadWorkflow.md)
