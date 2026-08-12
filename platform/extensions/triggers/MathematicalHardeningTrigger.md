# Trigger: MathematicalHardeningTrigger

> Capability #151 — **Mathematical Hardening**

Event source(s) that initiate execution for this capability.

### Trigger: SimOutputReadyTrigger

```typescript
// trigger: SimOutputReadyTrigger
const SimOutputReadyTriggerContract: TriggerContract = {
  triggerId: 'SimOutputReadyTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SimOutputReadyTrigger' },
  actionTarget: 'EstimateConditionTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MathematicalHardeningProtocol.md) · [Tasks](../tasks/MathematicalHardeningTask.md) · [Workflow](../workflows/MathematicalHardeningWorkflow.md)
