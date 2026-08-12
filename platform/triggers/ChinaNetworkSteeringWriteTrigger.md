# Trigger: ChinaNetworkSteeringWriteTrigger

> Capability #86 — **China Network Steering Write**

Event source(s) that initiate execution for this capability.

### Trigger: SteeringConfigUpdatedTrigger

```typescript
// trigger: SteeringConfigUpdatedTrigger
const SteeringConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'SteeringConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SteeringConfigUpdatedTrigger' },
  actionTarget: 'ConfigureChinaSteeringTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ChinaNetworkSteeringWriteProtocol.md) · [Tasks](../tasks/ChinaNetworkSteeringWriteTask.md) · [Workflow](../workflows/ChinaNetworkSteeringWriteWorkflow.md)
