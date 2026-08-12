# Workflow: FieldExtractorsWriteWorkflow

> Capability #44 — **Field Extractors Write**

## Definition
```typescript
// workflow: FieldExtractorsWriteWorkflow
const FieldExtractorsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'FieldExtractorsWriteWorkflow',
  version: '1.0.0',
  description: 'Field Extractors Write — Define pattern -> Test -> Attach to rule -> Deploy',
  trigger: { triggerId: 'ExtractorConfigTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define pattern'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Attach to rule'
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
Define pattern -> Test -> Attach to rule -> Deploy

## Related artifacts
- [Protocol](../protocols/FieldExtractorsWriteProtocol.md) · [Trigger(s)](../triggers/FieldExtractorsWriteTrigger.md) · [Tasks](../tasks/FieldExtractorsWriteTask.md)
