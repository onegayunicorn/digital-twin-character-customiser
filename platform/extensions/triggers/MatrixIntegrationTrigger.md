# Trigger: MatrixIntegrationTrigger

> Capability #149 — **Matrix Integration**

Event source(s) that initiate execution for this capability.

### Trigger: InventoryUpdatedTrigger

```typescript
// trigger: InventoryUpdatedTrigger
const InventoryUpdatedTriggerContract: TriggerContract = {
  triggerId: 'InventoryUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for InventoryUpdatedTrigger' },
  actionTarget: 'BuildAdjacencyTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MatrixIntegrationProtocol.md) · [Tasks](../tasks/MatrixIntegrationTask.md) · [Workflow](../workflows/MatrixIntegrationWorkflow.md)
