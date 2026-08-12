# Workflow: WorkersObservabilityWriteWorkflow

> Capability #24 — **Workers Observability Write**

## Definition
```typescript
// workflow: WorkersObservabilityWriteWorkflow
const WorkersObservabilityWriteWorkflow: WorkflowDefinition = {
  workflowId: 'WorkersObservabilityWriteWorkflow',
  version: '1.0.0',
  description: 'Workers Observability Write — Define metrics -> Set retention -> Build dash -> Create alerts -> Deploy',
  trigger: { triggerId: 'MetricThresholdTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define metrics'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Set retention'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Build dash'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Create alerts'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
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
Define metrics -> Set retention -> Build dash -> Create alerts -> Deploy

## Related artifacts
- [Protocol](../protocols/WorkersObservabilityWriteProtocol.md) · [Trigger(s)](../triggers/WorkersObservabilityWriteTrigger.md) · [Tasks](../tasks/WorkersObservabilityWriteTask.md)
