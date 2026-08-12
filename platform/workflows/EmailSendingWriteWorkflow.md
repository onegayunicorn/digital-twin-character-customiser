# Workflow: EmailSendingWriteWorkflow

> Capability #78 — **Email Sending Write**

## Definition
```typescript
// workflow: EmailSendingWriteWorkflow
const EmailSendingWriteWorkflow: WorkflowDefinition = {
  workflowId: 'EmailSendingWriteWorkflow',
  version: '1.0.0',
  description: 'Email Sending Write — Compose -> Validate -> Queue -> Send -> Track -> Retry',
  trigger: { triggerId: 'EmailSendTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Compose'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Queue'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Send'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Track'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
    name: 'Retry'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Compose -> Validate -> Queue -> Send -> Track -> Retry

## Related artifacts
- [Protocol](../protocols/EmailSendingWriteProtocol.md) · [Trigger(s)](../triggers/EmailSendingWriteTrigger.md) · [Tasks](../tasks/EmailSendingWriteTask.md)
