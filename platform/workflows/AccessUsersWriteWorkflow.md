# Workflow: AccessUsersWriteWorkflow

> Capability #118 — **Access: Users Write**

## Definition
```typescript
// workflow: AccessUsersWriteWorkflow
const AccessUsersWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessUsersWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Users Write — Create -> Invite -> Enroll MFA -> Provision -> Deprovision',
  trigger: { triggerId: 'UserCreatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Invite'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Enroll MFA'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Provision'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Deprovision'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Create -> Invite -> Enroll MFA -> Provision -> Deprovision

## Related artifacts
- [Protocol](../protocols/AccessUsersWriteProtocol.md) · [Trigger(s)](../triggers/AccessUsersWriteTrigger.md) · [Tasks](../tasks/AccessUsersWriteTask.md)
