# Workflow: ImagesWriteWorkflow

> Capability #80 — **Images Write**

## Definition
```typescript
// workflow: ImagesWriteWorkflow
const ImagesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'ImagesWriteWorkflow',
  version: '1.0.0',
  description: 'Images Write — Upload -> Validate -> Transform -> Store -> Deliver',
  trigger: { triggerId: 'ImageUploadedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Upload'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Transform'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Store'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Deliver'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Upload -> Validate -> Transform -> Store -> Deliver

## Related artifacts
- [Protocol](../protocols/ImagesWriteProtocol.md) · [Trigger(s)](../triggers/ImagesWriteTrigger.md) · [Tasks](../tasks/ImagesWriteTask.md)
