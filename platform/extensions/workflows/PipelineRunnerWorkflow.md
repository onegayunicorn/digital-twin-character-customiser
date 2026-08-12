# Workflow: PipelineRunnerWorkflow

> Capability #153 — **Pipeline Runner**

## Definition
```typescript
// workflow: PipelineRunnerWorkflow
const PipelineRunnerWorkflow: WorkflowDefinition = {
  workflowId: 'PipelineRunnerWorkflow',
  version: '1.0.0',
  description: 'Pipeline Runner — Validate -> Enqueue steps -> Dispatch -> Audit -> Report',
  trigger: { triggerId: 'PipelineSubmittedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Enqueue steps'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Dispatch'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Audit'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
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
Validate -> Enqueue steps -> Dispatch -> Audit -> Report

## Related artifacts
- [Protocol](../protocols/PipelineRunnerProtocol.md) · [Trigger(s)](../triggers/PipelineRunnerTrigger.md) · [Tasks](../tasks/PipelineRunnerTask.md)
