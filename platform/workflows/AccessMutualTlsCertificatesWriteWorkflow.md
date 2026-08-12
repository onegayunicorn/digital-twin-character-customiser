# Workflow: AccessMutualTlsCertificatesWriteWorkflow

> Capability #107 — **Access: Mutual TLS Certificates Write**

## Definition
```typescript
// workflow: AccessMutualTlsCertificatesWriteWorkflow
const AccessMutualTlsCertificatesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessMutualTlsCertificatesWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Mutual TLS Certificates Write — Upload CA -> Require cert -> Validate -> Enforce',
  trigger: { triggerId: 'MTLSCertUploadedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Upload CA'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Require cert'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Enforce'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Upload CA -> Require cert -> Validate -> Enforce

## Related artifacts
- [Protocol](../protocols/AccessMutualTlsCertificatesWriteProtocol.md) · [Trigger(s)](../triggers/AccessMutualTlsCertificatesWriteTrigger.md) · [Tasks](../tasks/AccessMutualTlsCertificatesWriteTask.md)
