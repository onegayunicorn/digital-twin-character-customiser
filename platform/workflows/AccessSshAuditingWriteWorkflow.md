# Workflow: AccessSshAuditingWriteWorkflow

> Capability #116 — **Access: SSH Auditing Write**

## Definition
```typescript
// workflow: AccessSshAuditingWriteWorkflow
const AccessSshAuditingWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessSshAuditingWriteWorkflow',
  version: '1.0.0',
  description: 'Access: SSH Auditing Write — Enable -> Capture -> Store -> Review -> Archive',
  trigger: { triggerId: 'SSHSessionStartTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Enable'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Capture'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Store'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Review'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Archive'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Enable -> Capture -> Store -> Review -> Archive

## Related artifacts
- [Protocol](../protocols/AccessSshAuditingWriteProtocol.md) · [Trigger(s)](../triggers/AccessSshAuditingWriteTrigger.md) · [Tasks](../tasks/AccessSshAuditingWriteTask.md)
