# Trigger: SelectConfigurationWriteTrigger

> Capability #61 — **Select Configuration Write**

Event source(s) that initiate execution for this capability.

### Trigger: SelectConfigUpdatedTrigger

```typescript
// trigger: SelectConfigUpdatedTrigger
const SelectConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'SelectConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SelectConfigUpdatedTrigger' },
  actionTarget: 'UpdateSelectConfigurationTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/SelectConfigurationWriteProtocol.md) · [Tasks](../tasks/SelectConfigurationWriteTask.md) · [Workflow](../workflows/SelectConfigurationWriteWorkflow.md)
