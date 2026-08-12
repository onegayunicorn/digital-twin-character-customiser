# Task: AccountApiTokensWriteTask

> Capability #64 — **Account API Tokens Write**

Atomic executable unit(s) for this capability.

### Task: IssueAPITokenTask

```typescript
// task: IssueAPITokenTask
const IssueAPITokenTaskSpec: TaskSpecification = {
  taskId: 'IssueAPITokenTask',
  operationRef: 'AccountApiTokensWriteProtocol',
  inputSchema: { capability: 'Account API Tokens Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute IssueAPITokenTask

### Task: RevokeAPITokenTask

```typescript
// task: RevokeAPITokenTask
const RevokeAPITokenTaskSpec: TaskSpecification = {
  taskId: 'RevokeAPITokenTask',
  operationRef: 'AccountApiTokensWriteProtocol',
  inputSchema: { capability: 'Account API Tokens Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RevokeAPITokenTask

## Related artifacts
- [Protocol](../protocols/AccountApiTokensWriteProtocol.md) · [Trigger(s)](../triggers/AccountApiTokensWriteTrigger.md) · [Workflow](../workflows/AccountApiTokensWriteWorkflow.md)
