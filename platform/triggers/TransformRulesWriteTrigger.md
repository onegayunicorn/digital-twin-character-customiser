# Trigger: TransformRulesWriteTrigger

> Capability #59 — **Transform Rules Write**

Event source(s) that initiate execution for this capability.

### Trigger: TransformRuleUpdatedTrigger

```typescript
// trigger: TransformRuleUpdatedTrigger
const TransformRuleUpdatedTriggerContract: TriggerContract = {
  triggerId: 'TransformRuleUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TransformRuleUpdatedTrigger' },
  actionTarget: 'CreateTransformRuleTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/TransformRulesWriteProtocol.md) · [Tasks](../tasks/TransformRulesWriteTask.md) · [Workflow](../workflows/TransformRulesWriteWorkflow.md)
