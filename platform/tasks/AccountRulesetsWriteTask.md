# Task: AccountRulesetsWriteTask

> Capability #58 — **Account Rulesets Write**

Atomic executable unit(s) for this capability.

### Task: DeployRulesetTask

```typescript
// task: DeployRulesetTask
const DeployRulesetTaskSpec: TaskSpecification = {
  taskId: 'DeployRulesetTask',
  operationRef: 'AccountRulesetsWriteProtocol',
  inputSchema: { capability: 'Account Rulesets Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute DeployRulesetTask

## Related artifacts
- [Protocol](../protocols/AccountRulesetsWriteProtocol.md) · [Trigger(s)](../triggers/AccountRulesetsWriteTrigger.md) · [Workflow](../workflows/AccountRulesetsWriteWorkflow.md)
