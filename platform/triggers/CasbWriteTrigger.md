# Trigger: CasbWriteTrigger

> Capability #120 — **CASB Write**

Event source(s) that initiate execution for this capability.

### Trigger: CASBConfigUpdatedTrigger

```typescript
// trigger: CASBConfigUpdatedTrigger
const CASBConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'CASBConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for CASBConfigUpdatedTrigger' },
  actionTarget: 'ConfigureCASBIntegrationTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/CasbWriteProtocol.md) · [Tasks](../tasks/CasbWriteTask.md) · [Workflow](../workflows/CasbWriteWorkflow.md)
