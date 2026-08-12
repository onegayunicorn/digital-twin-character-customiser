# Trigger: CrystalNucleationSimTrigger

> Capability #135 — **Crystal Nucleation Sim**

Event source(s) that initiate execution for this capability.

### Trigger: SimulationStepTrigger

```typescript
// trigger: SimulationStepTrigger
const SimulationStepTriggerContract: TriggerContract = {
  triggerId: 'SimulationStepTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SimulationStepTrigger' },
  actionTarget: 'NucleateCrystalTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: StabilizationTrigger

```typescript
// trigger: StabilizationTrigger
const StabilizationTriggerContract: TriggerContract = {
  triggerId: 'StabilizationTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for StabilizationTrigger' },
  actionTarget: 'NucleateCrystalTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/CrystalNucleationSimProtocol.md) · [Tasks](../tasks/CrystalNucleationSimTask.md) · [Workflow](../workflows/CrystalNucleationSimWorkflow.md)
