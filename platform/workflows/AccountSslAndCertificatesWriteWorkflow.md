# Workflow: AccountSslAndCertificatesWriteWorkflow

> Capability #73 — **Account: SSL and Certificates Write**

## Definition
```typescript
// workflow: AccountSslAndCertificatesWriteWorkflow
const AccountSslAndCertificatesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccountSslAndCertificatesWriteWorkflow',
  version: '1.0.0',
  description: 'Account: SSL and Certificates Write — Request -> Validate -> Issue -> Deploy -> Renew -> Revoke',
  trigger: { triggerId: 'CertExpiryTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Request'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Issue'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Renew'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
    name: 'Revoke'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Request -> Validate -> Issue -> Deploy -> Renew -> Revoke

## Related artifacts
- [Protocol](../protocols/AccountSslAndCertificatesWriteProtocol.md) · [Trigger(s)](../triggers/AccountSslAndCertificatesWriteTrigger.md) · [Tasks](../tasks/AccountSslAndCertificatesWriteTask.md)
