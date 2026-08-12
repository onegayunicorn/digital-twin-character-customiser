# Workflow: ArtifactsWriteWorkflow

> Capability #62 — **Artifacts Write**

## Definition
```typescript
// workflow: ArtifactsWriteWorkflow
const ArtifactsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'ArtifactsWriteWorkflow',
  version: '1.0.0',
  description: 'Artifacts Write — Build -> Sign -> Upload -> Index -> Distribute',
  trigger: { triggerId: 'ArtifactUploadedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Build'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Sign'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Upload'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Index'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Distribute'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Build -> Sign -> Upload -> Index -> Distribute

## Related artifacts
- [Protocol](../protocols/ArtifactsWriteProtocol.md) · [Trigger(s)](../triggers/ArtifactsWriteTrigger.md) · [Tasks](../tasks/ArtifactsWriteTask.md)
