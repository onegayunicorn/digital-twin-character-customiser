# Workflow: ZeroTrustSeatsWriteWorkflow

> Capability #130 — **Zero Trust: Seats Write**

## Definition
```typescript
// workflow: ZeroTrustSeatsWriteWorkflow
const ZeroTrustSeatsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'ZeroTrustSeatsWriteWorkflow',
  version: '1.0.0',
  description: 'Zero Trust: Seats Write — Assign -> Enable -> Sync -> Reclaim -> Report',
  trigger: { triggerId: 'SeatAssignmentTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Assign'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Enable'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Sync'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Reclaim'
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
Assign -> Enable -> Sync -> Reclaim -> Report

## Related artifacts
- [Protocol](../protocols/ZeroTrustSeatsWriteProtocol.md) · [Trigger(s)](../triggers/ZeroTrustSeatsWriteTrigger.md) · [Tasks](../tasks/ZeroTrustSeatsWriteTask.md)
