# Workflow: AccountCustomPagesWriteWorkflow

> Capability #56 — **Account Custom Pages Write**

## Definition
```typescript
// workflow: AccountCustomPagesWriteWorkflow
const AccountCustomPagesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccountCustomPagesWriteWorkflow',
  version: '1.0.0',
  description: 'Account Custom Pages Write — Design -> Upload -> Assign -> Activate -> Verify',
  trigger: { triggerId: 'CustomPageRequestedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Design'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Upload'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Assign'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Activate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Verify'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Design -> Upload -> Assign -> Activate -> Verify

## Related artifacts
- [Protocol](../protocols/AccountCustomPagesWriteProtocol.md) · [Trigger(s)](../triggers/AccountCustomPagesWriteTrigger.md) · [Tasks](../tasks/AccountCustomPagesWriteTask.md)
