# Workflow: MoqWriteWorkflow

> Capability #81 — **MoQ Write**

## Definition
```typescript
// workflow: MoqWriteWorkflow
const MoqWriteWorkflow: WorkflowDefinition = {
  workflowId: 'MoqWriteWorkflow',
  version: '1.0.0',
  description: 'MoQ Write — Ingest -> Transcode -> Distribute -> Playback -> Monitor',
  trigger: { triggerId: 'MoQStreamStartTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Ingest'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Transcode'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Distribute'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Playback'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Monitor'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Ingest -> Transcode -> Distribute -> Playback -> Monitor

## Related artifacts
- [Protocol](../protocols/MoqWriteProtocol.md) · [Trigger(s)](../triggers/MoqWriteTrigger.md) · [Tasks](../tasks/MoqWriteTask.md)
