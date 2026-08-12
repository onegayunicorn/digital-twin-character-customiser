# Trigger: DdosProtectionWriteTrigger

> Capability #43 — **DDoS Protection Write**

Event source(s) that initiate execution for this capability.

### Trigger: DDoSEventDetectedTrigger

```typescript
// trigger: DDoSEventDetectedTrigger
const DDoSEventDetectedTriggerContract: TriggerContract = {
  triggerId: 'DDoSEventDetectedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DDoSEventDetectedTrigger' },
  actionTarget: 'ConfigureDDoSProtectionTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/DdosProtectionWriteProtocol.md) · [Tasks](../tasks/DdosProtectionWriteTask.md) · [Workflow](../workflows/DdosProtectionWriteWorkflow.md)
