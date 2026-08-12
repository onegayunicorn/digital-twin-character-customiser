# Workflow: FraudEventsWriteWorkflow

> Capability #45 — **Fraud Events Write**

## Definition
```typescript
// workflow: FraudEventsWriteWorkflow
const FraudEventsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'FraudEventsWriteWorkflow',
  version: '1.0.0',
  description: 'Fraud Events Write — Collect -> Score -> Flag -> Action -> Report',
  trigger: { triggerId: 'FraudEventDetectedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Collect'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Score'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Flag'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Action'
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
Collect -> Score -> Flag -> Action -> Report

## Related artifacts
- [Protocol](../protocols/FraudEventsWriteProtocol.md) · [Trigger(s)](../triggers/FraudEventsWriteTrigger.md) · [Tasks](../tasks/FraudEventsWriteTask.md)
