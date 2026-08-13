# Workflow: OffgridSyncWorkflow

> Capability #159 — **Off-grid Sync**

## Definition
```typescript
// workflow: OffgridSyncWorkflow
const OffgridSyncWorkflow: WorkflowDefinition = {
  workflowId: 'OffgridSyncWorkflow',
  version: '1.0.0',
  description: 'Off-grid Sync — Queue -> Sync -> Merge -> Reconcile -> Report',
  trigger: { triggerId: 'OfflineTransactionTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Queue'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Sync'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Merge'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Reconcile'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
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
Queue -> Sync -> Merge -> Reconcile -> Report

## Related artifacts
- [Protocol](../protocols/OffgridSyncProtocol.md) · [Trigger(s)](../triggers/OffgridSyncTrigger.md) · [Tasks](../tasks/OffgridSyncTask.md)
