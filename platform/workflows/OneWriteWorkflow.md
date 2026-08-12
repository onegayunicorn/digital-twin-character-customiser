# Workflow: OneWriteWorkflow

> Capability #41 — **One Write**

## Definition
```typescript
// workflow: OneWriteWorkflow
const OneWriteWorkflow: WorkflowDefinition = {
  workflowId: 'OneWriteWorkflow',
  version: '1.0.0',
  description: 'One Write — Update -> Sync across services -> Validate -> Notify',
  trigger: { triggerId: 'OneConfigChangeTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Update'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Sync across services'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Notify'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Update -> Sync across services -> Validate -> Notify

## Related artifacts
- [Protocol](../protocols/OneWriteProtocol.md) · [Trigger(s)](../triggers/OneWriteTrigger.md) · [Tasks](../tasks/OneWriteTask.md)
