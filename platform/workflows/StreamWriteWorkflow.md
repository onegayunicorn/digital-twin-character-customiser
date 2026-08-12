# Workflow: StreamWriteWorkflow

> Capability #82 — **Stream Write**

## Definition
```typescript
// workflow: StreamWriteWorkflow
const StreamWriteWorkflow: WorkflowDefinition = {
  workflowId: 'StreamWriteWorkflow',
  version: '1.0.0',
  description: 'Stream Write — Create -> Ingest -> Transcode -> Publish -> View -> Archive',
  trigger: { triggerId: 'StreamStartedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Ingest'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Transcode'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Publish'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'View'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
    name: 'Archive'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Create -> Ingest -> Transcode -> Publish -> View -> Archive

## Related artifacts
- [Protocol](../protocols/StreamWriteProtocol.md) · [Trigger(s)](../triggers/StreamWriteTrigger.md) · [Tasks](../tasks/StreamWriteTask.md)
