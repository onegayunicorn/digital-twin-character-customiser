# Workflow: ConstellationWriteWorkflow

> Capability #27 — **Constellation Write**

## Definition
```typescript
// workflow: ConstellationWriteWorkflow
const ConstellationWriteWorkflow: WorkflowDefinition = {
  workflowId: 'ConstellationWriteWorkflow',
  version: '1.0.0',
  description: 'Constellation Write — Register node -> Sync state -> Reconcile -> Broadcast',
  trigger: { triggerId: 'NodeJoinTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register node'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Sync state'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Reconcile'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Broadcast'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Register node -> Sync state -> Reconcile -> Broadcast

## Related artifacts
- [Protocol](../protocols/ConstellationWriteProtocol.md) · [Trigger(s)](../triggers/ConstellationWriteTrigger.md) · [Tasks](../tasks/ConstellationWriteTask.md)
