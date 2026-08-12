# Trigger: DdosBotnetFeedWriteTrigger

> Capability #42 — **DDoS Botnet Feed Write**

Event source(s) that initiate execution for this capability.

### Trigger: FeedUpdatedTrigger

```typescript
// trigger: FeedUpdatedTrigger
const FeedUpdatedTriggerContract: TriggerContract = {
  triggerId: 'FeedUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for FeedUpdatedTrigger' },
  actionTarget: 'IngestBotnetFeedTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ScheduleFeedSyncTrigger

```typescript
// trigger: ScheduleFeedSyncTrigger
const ScheduleFeedSyncTriggerContract: TriggerContract = {
  triggerId: 'ScheduleFeedSyncTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ScheduleFeedSyncTrigger' },
  actionTarget: 'IngestBotnetFeedTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/DdosBotnetFeedWriteProtocol.md) · [Tasks](../tasks/DdosBotnetFeedWriteTask.md) · [Workflow](../workflows/DdosBotnetFeedWriteWorkflow.md)
