# Trigger: FraudEventsWriteTrigger

> Capability #45 — **Fraud Events Write**

Event source(s) that initiate execution for this capability.

### Trigger: FraudEventDetectedTrigger

```typescript
// trigger: FraudEventDetectedTrigger
const FraudEventDetectedTriggerContract: TriggerContract = {
  triggerId: 'FraudEventDetectedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for FraudEventDetectedTrigger' },
  actionTarget: 'LogFraudEventTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/FraudEventsWriteProtocol.md) · [Tasks](../tasks/FraudEventsWriteTask.md) · [Workflow](../workflows/FraudEventsWriteWorkflow.md)
