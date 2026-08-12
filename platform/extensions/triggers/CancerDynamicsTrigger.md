# Trigger: CancerDynamicsTrigger

> Capability #140 — **Cancer Dynamics**

Event source(s) that initiate execution for this capability.

### Trigger: TherapyScenarioTrigger

```typescript
// trigger: TherapyScenarioTrigger
const TherapyScenarioTriggerContract: TriggerContract = {
  triggerId: 'TherapyScenarioTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TherapyScenarioTrigger' },
  actionTarget: 'RunGrowthSimTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/CancerDynamicsProtocol.md) · [Tasks](../tasks/CancerDynamicsTask.md) · [Workflow](../workflows/CancerDynamicsWorkflow.md)
