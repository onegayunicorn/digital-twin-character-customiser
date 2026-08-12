# Trigger: LoadBalancersAccountWriteTrigger

> Capability #83 — **Load Balancers Account Write**

Event source(s) that initiate execution for this capability.

### Trigger: LoadBalancerConfigTrigger

```typescript
// trigger: LoadBalancerConfigTrigger
const LoadBalancerConfigTriggerContract: TriggerContract = {
  triggerId: 'LoadBalancerConfigTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for LoadBalancerConfigTrigger' },
  actionTarget: 'ConfigureLoadBalancerTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: PoolHealthChangeTrigger

```typescript
// trigger: PoolHealthChangeTrigger
const PoolHealthChangeTriggerContract: TriggerContract = {
  triggerId: 'PoolHealthChangeTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PoolHealthChangeTrigger' },
  actionTarget: 'ConfigureLoadBalancerTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/LoadBalancersAccountWriteProtocol.md) · [Tasks](../tasks/LoadBalancersAccountWriteTask.md) · [Workflow](../workflows/LoadBalancersAccountWriteWorkflow.md)
