# Trigger: AccountRulesetsWriteTrigger

> Capability #58 — **Account Rulesets Write**

Event source(s) that initiate execution for this capability.

### Trigger: RulesetDeployedTrigger

```typescript
// trigger: RulesetDeployedTrigger
const RulesetDeployedTriggerContract: TriggerContract = {
  triggerId: 'RulesetDeployedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for RulesetDeployedTrigger' },
  actionTarget: 'DeployRulesetTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountRulesetsWriteProtocol.md) · [Tasks](../tasks/AccountRulesetsWriteTask.md) · [Workflow](../workflows/AccountRulesetsWriteWorkflow.md)
