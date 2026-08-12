# Workflow: AccountApiTokensWriteWorkflow

> Capability #64 — **Account API Tokens Write**

## Definition
```typescript
// workflow: AccountApiTokensWriteWorkflow
const AccountApiTokensWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccountApiTokensWriteWorkflow',
  version: '1.0.0',
  description: 'Account API Tokens Write — Request -> Scope -> Create -> Issue -> Rotate -> Revoke',
  trigger: { triggerId: 'TokenCreatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Request'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Scope'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Create'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Issue'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Rotate'
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
Request -> Scope -> Create -> Issue -> Rotate -> Revoke

## Related artifacts
- [Protocol](../protocols/AccountApiTokensWriteProtocol.md) · [Trigger(s)](../triggers/AccountApiTokensWriteTrigger.md) · [Tasks](../tasks/AccountApiTokensWriteTask.md)
