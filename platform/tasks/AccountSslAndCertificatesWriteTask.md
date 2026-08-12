# Task: AccountSslAndCertificatesWriteTask

> Capability #73 — **Account: SSL and Certificates Write**

Atomic executable unit(s) for this capability.

### Task: IssueDeployCertificateTask

```typescript
// task: IssueDeployCertificateTask
const IssueDeployCertificateTaskSpec: TaskSpecification = {
  taskId: 'IssueDeployCertificateTask',
  operationRef: 'AccountSslAndCertificatesWriteProtocol',
  inputSchema: { capability: 'Account: SSL and Certificates Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute IssueDeployCertificateTask

## Related artifacts
- [Protocol](../protocols/AccountSslAndCertificatesWriteProtocol.md) · [Trigger(s)](../triggers/AccountSslAndCertificatesWriteTrigger.md) · [Workflow](../workflows/AccountSslAndCertificatesWriteWorkflow.md)
