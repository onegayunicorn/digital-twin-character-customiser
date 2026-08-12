# Workflow: WorkersR2StorageWriteWorkflow

> Capability #17 — **Workers R2 Storage Write**

## Definition
```typescript
// workflow: WorkersR2StorageWriteWorkflow
const WorkersR2StorageWriteWorkflow: WorkflowDefinition = {
  workflowId: 'WorkersR2StorageWriteWorkflow',
  version: '1.0.0',
  description: 'Workers R2 Storage Write — Validate -> Upload -> Index -> Set lifecycle -> Purge cache',
  trigger: { triggerId: 'ObjectUploadedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Upload'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Index'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Set lifecycle'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Purge cache'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Validate -> Upload -> Index -> Set lifecycle -> Purge cache

## Related artifacts
- [Protocol](../protocols/WorkersR2StorageWriteProtocol.md) · [Trigger(s)](../triggers/WorkersR2StorageWriteTrigger.md) · [Tasks](../tasks/WorkersR2StorageWriteTask.md)
