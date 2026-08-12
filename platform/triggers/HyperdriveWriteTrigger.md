# Trigger: HyperdriveWriteTrigger

> Capability #11 — **Hyperdrive Write**

Event source(s) that initiate execution for this capability.

### Trigger: HyperdriveConfigUpdatedTrigger

```typescript
// trigger: HyperdriveConfigUpdatedTrigger
const HyperdriveConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'HyperdriveConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for HyperdriveConfigUpdatedTrigger' },
  actionTarget: 'ConfigureHyperdriveTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/HyperdriveWriteProtocol.md) · [Tasks](../tasks/HyperdriveWriteTask.md) · [Workflow](../workflows/HyperdriveWriteWorkflow.md)
