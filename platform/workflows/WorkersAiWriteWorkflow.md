# Workflow: WorkersAiWriteWorkflow

> Capability #7 — **Workers AI Write**

## Definition
```typescript
// workflow: WorkersAiWriteWorkflow
const WorkersAiWriteWorkflow: WorkflowDefinition = {
  workflowId: 'WorkersAiWriteWorkflow',
  version: '1.0.0',
  description: 'Workers AI Write — Select model -> Bind worker -> Set limits -> Deploy endpoint',
  trigger: { triggerId: 'AIInferenceRequestTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Select model'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Bind worker'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Set limits'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deploy endpoint'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Select model -> Bind worker -> Set limits -> Deploy endpoint

## Related artifacts
- [Protocol](../protocols/WorkersAiWriteProtocol.md) · [Trigger(s)](../triggers/WorkersAiWriteTrigger.md) · [Tasks](../tasks/WorkersAiWriteTask.md)
