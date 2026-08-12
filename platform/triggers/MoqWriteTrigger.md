# Trigger: MoqWriteTrigger

> Capability #81 — **MoQ Write**

Event source(s) that initiate execution for this capability.

### Trigger: MoQStreamStartTrigger

```typescript
// trigger: MoQStreamStartTrigger
const MoQStreamStartTriggerContract: TriggerContract = {
  triggerId: 'MoQStreamStartTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MoQStreamStartTrigger' },
  actionTarget: 'ConfigureMoQEndpointTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MoqWriteProtocol.md) · [Tasks](../tasks/MoqWriteTask.md) · [Workflow](../workflows/MoqWriteWorkflow.md)
