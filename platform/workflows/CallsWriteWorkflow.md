# Workflow: CallsWriteWorkflow

> Capability #79 — **Calls Write**

## Definition
```typescript
// workflow: CallsWriteWorkflow
const CallsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'CallsWriteWorkflow',
  version: '1.0.0',
  description: 'Calls Write — Create room -> Join -> Negotiate media -> Stream -> Record -> End',
  trigger: { triggerId: 'CallInitiatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create room'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Join'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Negotiate media'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Stream'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Record'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
    name: 'End'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Create room -> Join -> Negotiate media -> Stream -> Record -> End

## Related artifacts
- [Protocol](../protocols/CallsWriteProtocol.md) · [Trigger(s)](../triggers/CallsWriteTrigger.md) · [Tasks](../tasks/CallsWriteTask.md)
