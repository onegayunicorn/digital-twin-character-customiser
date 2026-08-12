# Trigger: OneNetworksWriteTrigger

> Capability #125 — **One Networks Write**

Event source(s) that initiate execution for this capability.

### Trigger: NetworkConfigUpdatedTrigger

```typescript
// trigger: NetworkConfigUpdatedTrigger
const NetworkConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'NetworkConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for NetworkConfigUpdatedTrigger' },
  actionTarget: 'ManageOneNetworkTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/OneNetworksWriteProtocol.md) · [Tasks](../tasks/OneNetworksWriteTask.md) · [Workflow](../workflows/OneNetworksWriteWorkflow.md)
