# Task: AccountCustomErrorRulesWriteTask

> Capability #55 — **Account Custom Error Rules Write**

Atomic executable unit(s) for this capability.

### Task: CreateCustomErrorRuleTask

```typescript
// task: CreateCustomErrorRuleTask
const CreateCustomErrorRuleTaskSpec: TaskSpecification = {
  taskId: 'CreateCustomErrorRuleTask',
  operationRef: 'AccountCustomErrorRulesWriteProtocol',
  inputSchema: { capability: 'Account Custom Error Rules Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute CreateCustomErrorRuleTask

## Related artifacts
- [Protocol](../protocols/AccountCustomErrorRulesWriteProtocol.md) · [Trigger(s)](../triggers/AccountCustomErrorRulesWriteTrigger.md) · [Workflow](../workflows/AccountCustomErrorRulesWriteWorkflow.md)
