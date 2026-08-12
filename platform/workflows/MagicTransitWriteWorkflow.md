# Workflow: MagicTransitWriteWorkflow

> Capability #92 — **Magic Transit Write**

## Definition
```typescript
// workflow: MagicTransitWriteWorkflow
const MagicTransitWriteWorkflow: WorkflowDefinition = {
  workflowId: 'MagicTransitWriteWorkflow',
  version: '1.0.0',
  description: 'Magic Transit Write — Announce prefix -> Configure -> Activate -> Verify traffic',
  trigger: { triggerId: 'MagicTransitConfigTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Announce prefix'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Configure'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Activate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Verify traffic'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Announce prefix -> Configure -> Activate -> Verify traffic

## Related artifacts
- [Protocol](../protocols/MagicTransitWriteProtocol.md) · [Trigger(s)](../triggers/MagicTransitWriteTrigger.md) · [Tasks](../tasks/MagicTransitWriteTask.md)
