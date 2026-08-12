# Trigger: AccountRuleListsWriteTrigger

> Capability #57 — **Account Rule Lists Write**

Event source(s) that initiate execution for this capability.

### Trigger: RuleListUpdatedTrigger

```typescript
// trigger: RuleListUpdatedTrigger
const RuleListUpdatedTriggerContract: TriggerContract = {
  triggerId: 'RuleListUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for RuleListUpdatedTrigger' },
  actionTarget: 'ManageRuleListTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountRuleListsWriteProtocol.md) · [Tasks](../tasks/AccountRuleListsWriteTask.md) · [Workflow](../workflows/AccountRuleListsWriteWorkflow.md)
