# Workflow: AccessTagsWriteWorkflow

> Capability #117 — **Access: Tags Write**

## Definition
```typescript
// workflow: AccessTagsWriteWorkflow
const AccessTagsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessTagsWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Tags Write — Define -> Assign -> Enforce -> Report',
  trigger: { triggerId: 'AccessTagUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Assign'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Enforce'
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
Define -> Assign -> Enforce -> Report

## Related artifacts
- [Protocol](../protocols/AccessTagsWriteProtocol.md) · [Trigger(s)](../triggers/AccessTagsWriteTrigger.md) · [Tasks](../tasks/AccessTagsWriteTask.md)
