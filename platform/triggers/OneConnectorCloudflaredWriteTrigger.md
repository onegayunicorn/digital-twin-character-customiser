# Trigger: OneConnectorCloudflaredWriteTrigger

> Capability #122 — **One Connector: cloudflared Write**

Event source(s) that initiate execution for this capability.

### Trigger: CloudflaredConfigUpdatedTrigger

```typescript
// trigger: CloudflaredConfigUpdatedTrigger
const CloudflaredConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'CloudflaredConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for CloudflaredConfigUpdatedTrigger' },
  actionTarget: 'ConfigureCloudflaredTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/OneConnectorCloudflaredWriteProtocol.md) · [Tasks](../tasks/OneConnectorCloudflaredWriteTask.md) · [Workflow](../workflows/OneConnectorCloudflaredWriteWorkflow.md)
