# Trigger: DmdRepairSimulationTrigger

> Capability #139 — **DMD Repair Simulation**

Event source(s) that initiate execution for this capability.

### Trigger: MutationIngestedTrigger

```typescript
// trigger: MutationIngestedTrigger
const MutationIngestedTriggerContract: TriggerContract = {
  triggerId: 'MutationIngestedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MutationIngestedTrigger' },
  actionTarget: 'ClassifyMutationTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/DmdRepairSimulationProtocol.md) · [Tasks](../tasks/DmdRepairSimulationTask.md) · [Workflow](../workflows/DmdRepairSimulationWorkflow.md)
