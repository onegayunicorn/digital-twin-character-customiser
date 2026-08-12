# Trigger: GenesisOptimizerTrigger

> Capability #142 — **Genesis Optimizer**

Event source(s) that initiate execution for this capability.

### Trigger: OptimizationRequestedTrigger

```typescript
// trigger: OptimizationRequestedTrigger
const OptimizationRequestedTriggerContract: TriggerContract = {
  triggerId: 'OptimizationRequestedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for OptimizationRequestedTrigger' },
  actionTarget: 'RunGaTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/GenesisOptimizerProtocol.md) · [Tasks](../tasks/GenesisOptimizerTask.md) · [Workflow](../workflows/GenesisOptimizerWorkflow.md)
