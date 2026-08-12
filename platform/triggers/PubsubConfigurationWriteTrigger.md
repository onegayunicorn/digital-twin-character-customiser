# Trigger: PubsubConfigurationWriteTrigger

> Capability #22 — **Pubsub Configuration Write**

Event source(s) that initiate execution for this capability.

### Trigger: PubsubConfigChangeTrigger

```typescript
// trigger: PubsubConfigChangeTrigger
const PubsubConfigChangeTriggerContract: TriggerContract = {
  triggerId: 'PubsubConfigChangeTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PubsubConfigChangeTrigger' },
  actionTarget: 'ConfigurePubsubTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/PubsubConfigurationWriteProtocol.md) · [Tasks](../tasks/PubsubConfigurationWriteTask.md) · [Workflow](../workflows/PubsubConfigurationWriteWorkflow.md)
