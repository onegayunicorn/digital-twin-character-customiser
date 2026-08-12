# Trigger: WorkersR2DataCatalogWriteTrigger

> Capability #19 — **Workers R2 Data Catalog Write**

Event source(s) that initiate execution for this capability.

### Trigger: CatalogEntryUpdatedTrigger

```typescript
// trigger: CatalogEntryUpdatedTrigger
const CatalogEntryUpdatedTriggerContract: TriggerContract = {
  triggerId: 'CatalogEntryUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for CatalogEntryUpdatedTrigger' },
  actionTarget: 'UpdateR2DataCatalogTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WorkersR2DataCatalogWriteProtocol.md) · [Tasks](../tasks/WorkersR2DataCatalogWriteTask.md) · [Workflow](../workflows/WorkersR2DataCatalogWriteWorkflow.md)
