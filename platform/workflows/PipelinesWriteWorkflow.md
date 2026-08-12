# Workflow: PipelinesWriteWorkflow

> Capability #12 — **Pipelines Write**

## Definition
```typescript
// workflow: PipelinesWriteWorkflow
const PipelinesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'PipelinesWriteWorkflow',
  version: '1.0.0',
  description: 'Pipelines Write — Define schema -> Build stages -> Connect sources/sinks -> Activate',
  trigger: { triggerId: 'PipelineEventTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define schema'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Build stages'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Connect sources/sinks'
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
Define schema -> Build stages -> Connect sources/sinks -> Activate

## Related artifacts
- [Protocol](../protocols/PipelinesWriteProtocol.md) · [Trigger(s)](../triggers/PipelinesWriteTrigger.md) · [Tasks](../tasks/PipelinesWriteTask.md)
