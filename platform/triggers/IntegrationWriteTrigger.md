# Trigger: IntegrationWriteTrigger

> Capability #68 — **Integration Write**

Event source(s) that initiate execution for this capability.

### Trigger: IntegrationConnectedTrigger

```typescript
// trigger: IntegrationConnectedTrigger
const IntegrationConnectedTriggerContract: TriggerContract = {
  triggerId: 'IntegrationConnectedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for IntegrationConnectedTrigger' },
  actionTarget: 'ConfigureIntegrationTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/IntegrationWriteProtocol.md) · [Tasks](../tasks/IntegrationWriteTask.md) · [Workflow](../workflows/IntegrationWriteWorkflow.md)
