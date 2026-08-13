# Trigger: JurisdictionEngineTrigger

> Capability #155 — **Jurisdiction Engine**

Event source(s) that initiate execution for this capability.

### Trigger: TransactionSubmittedTrigger

```typescript
// trigger: TransactionSubmittedTrigger
const TransactionSubmittedTriggerContract: TriggerContract = {
  triggerId: 'TransactionSubmittedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TransactionSubmittedTrigger' },
  actionTarget: 'ClassifyJurisdictionTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/JurisdictionEngineProtocol.md) · [Tasks](../tasks/JurisdictionEngineTask.md) · [Workflow](../workflows/JurisdictionEngineWorkflow.md)
