# Trigger: MatrixEvolutionTrigger

> Capability #150 — **Matrix Evolution**

Event source(s) that initiate execution for this capability.

### Trigger: EvolutionRequestedTrigger

```typescript
// trigger: EvolutionRequestedTrigger
const EvolutionRequestedTriggerContract: TriggerContract = {
  triggerId: 'EvolutionRequestedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for EvolutionRequestedTrigger' },
  actionTarget: 'EvolveMatrixTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MatrixEvolutionProtocol.md) · [Tasks](../tasks/MatrixEvolutionTask.md) · [Workflow](../workflows/MatrixEvolutionWorkflow.md)
