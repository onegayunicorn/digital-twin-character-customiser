# Task: AccountRuleListsWriteTask

> Capability #57 — **Account Rule Lists Write**

Atomic executable unit(s) for this capability.

### Task: ManageRuleListTask

```typescript
// task: ManageRuleListTask
const ManageRuleListTaskSpec: TaskSpecification = {
  taskId: 'ManageRuleListTask',
  operationRef: 'AccountRuleListsWriteProtocol',
  inputSchema: { capability: 'Account Rule Lists Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageRuleListTask

## Related artifacts
- [Protocol](../protocols/AccountRuleListsWriteProtocol.md) · [Trigger(s)](../triggers/AccountRuleListsWriteTrigger.md) · [Workflow](../workflows/AccountRuleListsWriteWorkflow.md)
