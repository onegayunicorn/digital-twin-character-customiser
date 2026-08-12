# Trigger: OneConnectorWarpWriteTrigger

> Capability #123 — **One Connector: WARP Write**

Event source(s) that initiate execution for this capability.

### Trigger: WARPConfigUpdatedTrigger

```typescript
// trigger: WARPConfigUpdatedTrigger
const WARPConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'WARPConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for WARPConfigUpdatedTrigger' },
  actionTarget: 'ConfigureWARPConnectorTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/OneConnectorWarpWriteProtocol.md) · [Tasks](../tasks/OneConnectorWarpWriteTask.md) · [Workflow](../workflows/OneConnectorWarpWriteWorkflow.md)
