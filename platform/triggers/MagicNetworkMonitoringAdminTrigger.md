# Trigger: MagicNetworkMonitoringAdminTrigger

> Capability #91 — **Magic Network Monitoring Admin**

Event source(s) that initiate execution for this capability.

### Trigger: NetworkAnomalyTrigger

```typescript
// trigger: NetworkAnomalyTrigger
const NetworkAnomalyTriggerContract: TriggerContract = {
  triggerId: 'NetworkAnomalyTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for NetworkAnomalyTrigger' },
  actionTarget: 'ManageNetworkMonitoringTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MagicNetworkMonitoringAdminProtocol.md) · [Tasks](../tasks/MagicNetworkMonitoringAdminTask.md) · [Workflow](../workflows/MagicNetworkMonitoringAdminWorkflow.md)
