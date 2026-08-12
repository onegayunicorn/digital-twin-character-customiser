# Trigger: AccessPopulationWriteTrigger

> Capability #112 — **Access: Population Write**

Event source(s) that initiate execution for this capability.

### Trigger: PopulationUpdatedTrigger

```typescript
// trigger: PopulationUpdatedTrigger
const PopulationUpdatedTriggerContract: TriggerContract = {
  triggerId: 'PopulationUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PopulationUpdatedTrigger' },
  actionTarget: 'ManageAccessPopulationTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessPopulationWriteProtocol.md) · [Tasks](../tasks/AccessPopulationWriteTask.md) · [Workflow](../workflows/AccessPopulationWriteWorkflow.md)
