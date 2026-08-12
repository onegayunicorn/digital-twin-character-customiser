# Workflow: FlagshipWriteWorkflow

> Capability #28 — **Flagship Write**

## Definition
```typescript
// workflow: FlagshipWriteWorkflow
const FlagshipWriteWorkflow: WorkflowDefinition = {
  workflowId: 'FlagshipWriteWorkflow',
  version: '1.0.0',
  description: 'Flagship Write — Define -> Target -> Rollout -> Monitor -> Adjust',
  trigger: { triggerId: 'FlagChangedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Target'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Rollout'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Monitor'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Adjust'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define -> Target -> Rollout -> Monitor -> Adjust

## Related artifacts
- [Protocol](../protocols/FlagshipWriteProtocol.md) · [Trigger(s)](../triggers/FlagshipWriteTrigger.md) · [Tasks](../tasks/FlagshipWriteTask.md)
