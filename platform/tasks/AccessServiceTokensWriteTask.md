# Task: AccessServiceTokensWriteTask

> Capability #114 — **Access: Service Tokens Write**

Atomic executable unit(s) for this capability.

### Task: IssueServiceTokenTask

```typescript
// task: IssueServiceTokenTask
const IssueServiceTokenTaskSpec: TaskSpecification = {
  taskId: 'IssueServiceTokenTask',
  operationRef: 'AccessServiceTokensWriteProtocol',
  inputSchema: { capability: 'Access: Service Tokens Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute IssueServiceTokenTask

## Related artifacts
- [Protocol](../protocols/AccessServiceTokensWriteProtocol.md) · [Trigger(s)](../triggers/AccessServiceTokensWriteTrigger.md) · [Workflow](../workflows/AccessServiceTokensWriteWorkflow.md)
