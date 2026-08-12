# Trigger: IntelWriteTrigger

> Capability #96 — **Intel Write**

Event source(s) that initiate execution for this capability.

### Trigger: IntelFeedUpdatedTrigger

```typescript
// trigger: IntelFeedUpdatedTrigger
const IntelFeedUpdatedTriggerContract: TriggerContract = {
  triggerId: 'IntelFeedUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for IntelFeedUpdatedTrigger' },
  actionTarget: 'UpdateThreatIntelTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/IntelWriteProtocol.md) · [Tasks](../tasks/IntelWriteTask.md) · [Workflow](../workflows/IntelWriteWorkflow.md)
