# Trigger: AccountWafWriteTrigger

> Capability #38 — **Account WAF Write**

Event source(s) that initiate execution for this capability.

### Trigger: WAFRuleUpdatedTrigger

```typescript
// trigger: WAFRuleUpdatedTrigger
const WAFRuleUpdatedTriggerContract: TriggerContract = {
  triggerId: 'WAFRuleUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for WAFRuleUpdatedTrigger' },
  actionTarget: 'ConfigureWAFTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: AttackDetectedTrigger

```typescript
// trigger: AttackDetectedTrigger
const AttackDetectedTriggerContract: TriggerContract = {
  triggerId: 'AttackDetectedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AttackDetectedTrigger' },
  actionTarget: 'ConfigureWAFTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountWafWriteProtocol.md) · [Tasks](../tasks/AccountWafWriteTask.md) · [Workflow](../workflows/AccountWafWriteWorkflow.md)
