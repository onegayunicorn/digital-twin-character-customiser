# Workflow: AccessSamlCertificatesWriteWorkflow

> Capability #113 — **Access: SAML Certificates Write**

## Definition
```typescript
// workflow: AccessSamlCertificatesWriteWorkflow
const AccessSamlCertificatesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessSamlCertificatesWriteWorkflow',
  version: '1.0.0',
  description: 'Access: SAML Certificates Write — Generate -> Upload -> Update IdP -> Rollover -> Revoke old',
  trigger: { triggerId: 'SAMLCertExpiryTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Generate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Upload'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Update IdP'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Rollover'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Revoke old'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Generate -> Upload -> Update IdP -> Rollover -> Revoke old

## Related artifacts
- [Protocol](../protocols/AccessSamlCertificatesWriteProtocol.md) · [Trigger(s)](../triggers/AccessSamlCertificatesWriteTrigger.md) · [Tasks](../tasks/AccessSamlCertificatesWriteTask.md)
