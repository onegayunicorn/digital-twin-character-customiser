# Trigger: ProcurementEngineTrigger

> Capability #158 — **Procurement Engine**

Event source(s) that initiate execution for this capability.

### Trigger: TenderOpenedTrigger

```typescript
// trigger: TenderOpenedTrigger
const TenderOpenedTriggerContract: TriggerContract = {
  triggerId: 'TenderOpenedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TenderOpenedTrigger' },
  actionTarget: 'EvaluateBidsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: InvoiceSubmittedTrigger

```typescript
// trigger: InvoiceSubmittedTrigger
const InvoiceSubmittedTriggerContract: TriggerContract = {
  triggerId: 'InvoiceSubmittedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for InvoiceSubmittedTrigger' },
  actionTarget: 'EvaluateBidsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ProcurementEngineProtocol.md) · [Tasks](../tasks/ProcurementEngineTask.md) · [Workflow](../workflows/ProcurementEngineWorkflow.md)
