# Trigger: OffgridSyncTrigger

> Capability #159 — **Off-grid Sync**

Event source(s) that initiate execution for this capability.

### Trigger: OfflineTransactionTrigger

```typescript
// trigger: OfflineTransactionTrigger
const OfflineTransactionTriggerContract: TriggerContract = {
  triggerId: 'OfflineTransactionTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for OfflineTransactionTrigger' },
  actionTarget: 'EnqueueOfflineTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: SyncOpportunityTrigger

```typescript
// trigger: SyncOpportunityTrigger
const SyncOpportunityTriggerContract: TriggerContract = {
  triggerId: 'SyncOpportunityTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SyncOpportunityTrigger' },
  actionTarget: 'EnqueueOfflineTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/OffgridSyncProtocol.md) · [Tasks](../tasks/OffgridSyncTask.md) · [Workflow](../workflows/OffgridSyncWorkflow.md)
