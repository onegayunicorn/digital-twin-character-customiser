# Workflow: AccessPopulationWriteWorkflow

> Capability #112 — **Access: Population Write**

## Definition
```typescript
// workflow: AccessPopulationWriteWorkflow
const AccessPopulationWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessPopulationWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Population Write — Sync source -> Filter -> Store -> Update policies',
  trigger: { triggerId: 'PopulationUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Sync source'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Filter'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Store'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Update policies'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Sync source -> Filter -> Store -> Update policies

## Related artifacts
- [Protocol](../protocols/AccessPopulationWriteProtocol.md) · [Trigger(s)](../triggers/AccessPopulationWriteTrigger.md) · [Tasks](../tasks/AccessPopulationWriteTask.md)
