# Workflow: SelectConfigurationWriteWorkflow

> Capability #61 — **Select Configuration Write**

## Definition
```typescript
// workflow: SelectConfigurationWriteWorkflow
const SelectConfigurationWriteWorkflow: WorkflowDefinition = {
  workflowId: 'SelectConfigurationWriteWorkflow',
  version: '1.0.0',
  description: 'Select Configuration Write — Define criteria -> Assign targets -> Validate -> Deploy',
  trigger: { triggerId: 'SelectConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define criteria'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Assign targets'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define criteria -> Assign targets -> Validate -> Deploy

## Related artifacts
- [Protocol](../protocols/SelectConfigurationWriteProtocol.md) · [Trigger(s)](../triggers/SelectConfigurationWriteTrigger.md) · [Tasks](../tasks/SelectConfigurationWriteTask.md)
