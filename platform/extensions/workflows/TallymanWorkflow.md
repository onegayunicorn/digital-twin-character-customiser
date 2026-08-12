# Workflow: TallymanWorkflow

> Capability #147 — **Tallyman**

## Definition
```typescript
// workflow: TallymanWorkflow
const TallymanWorkflow: WorkflowDefinition = {
  workflowId: 'TallymanWorkflow',
  version: '1.0.0',
  description: 'Tallyman — Collect metrics -> Aggregate -> Flag -> Report',
  trigger: { triggerId: 'TallyRequestTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Collect metrics'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Aggregate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Flag'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Report'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Collect metrics -> Aggregate -> Flag -> Report

## Related artifacts
- [Protocol](../protocols/TallymanProtocol.md) · [Trigger(s)](../triggers/TallymanTrigger.md) · [Tasks](../tasks/TallymanTask.md)
