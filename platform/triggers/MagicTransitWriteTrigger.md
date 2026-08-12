# Trigger: MagicTransitWriteTrigger

> Capability #92 — **Magic Transit Write**

Event source(s) that initiate execution for this capability.

### Trigger: MagicTransitConfigTrigger

```typescript
// trigger: MagicTransitConfigTrigger
const MagicTransitConfigTriggerContract: TriggerContract = {
  triggerId: 'MagicTransitConfigTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MagicTransitConfigTrigger' },
  actionTarget: 'ProvisionMagicTransitTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MagicTransitWriteProtocol.md) · [Tasks](../tasks/MagicTransitWriteTask.md) · [Workflow](../workflows/MagicTransitWriteWorkflow.md)
