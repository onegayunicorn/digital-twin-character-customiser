# Trigger: AccountCustomErrorRulesWriteTrigger

> Capability #55 — **Account Custom Error Rules Write**

Event source(s) that initiate execution for this capability.

### Trigger: ErrorResponseTrigger

```typescript
// trigger: ErrorResponseTrigger
const ErrorResponseTriggerContract: TriggerContract = {
  triggerId: 'ErrorResponseTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ErrorResponseTrigger' },
  actionTarget: 'CreateCustomErrorRuleTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: RuleConfigTrigger

```typescript
// trigger: RuleConfigTrigger
const RuleConfigTriggerContract: TriggerContract = {
  triggerId: 'RuleConfigTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for RuleConfigTrigger' },
  actionTarget: 'CreateCustomErrorRuleTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountCustomErrorRulesWriteProtocol.md) · [Tasks](../tasks/AccountCustomErrorRulesWriteTask.md) · [Workflow](../workflows/AccountCustomErrorRulesWriteWorkflow.md)
