# Workflow: TwinEngineSyncWorkflow

> Capability #132 — **Twin Engine Sync**

## Definition
```typescript
// workflow: TwinEngineSyncWorkflow
const TwinEngineSyncWorkflow: WorkflowDefinition = {
  workflowId: 'TwinEngineSyncWorkflow',
  version: '1.0.0',
  description: 'Twin Engine Sync — Capture -> Version -> Broadcast -> Reconcile -> Verify',
  trigger: { triggerId: 'TwinStateChangedTrigger (on state update)' },
  steps: [
  - stepId: 'step1'
    name: 'Capture'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Version'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Broadcast'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Reconcile'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Verify'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Capture -> Version -> Broadcast -> Reconcile -> Verify

## Related artifacts
- [Protocol](../protocols/TwinEngineSyncProtocol.md) · [Trigger(s)](../triggers/TwinEngineSyncTrigger.md) · [Tasks](../tasks/TwinEngineSyncTask.md)
