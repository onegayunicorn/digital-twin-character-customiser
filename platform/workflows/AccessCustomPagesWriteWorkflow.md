# Workflow: AccessCustomPagesWriteWorkflow

> Capability #103 — **Access: Custom Pages Write**

## Definition
```typescript
// workflow: AccessCustomPagesWriteWorkflow
const AccessCustomPagesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessCustomPagesWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Custom Pages Write — Design -> Upload -> Assign -> Activate',
  trigger: { triggerId: 'AccessPageRequestedTrigger' },
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
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Design -> Upload -> Assign -> Activate

## Related artifacts
- [Protocol](../protocols/AccessCustomPagesWriteProtocol.md) · [Trigger(s)](../triggers/AccessCustomPagesWriteTrigger.md) · [Tasks](../tasks/AccessCustomPagesWriteTask.md)
