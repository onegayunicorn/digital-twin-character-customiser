# Workflow: MatrixIntegrationWorkflow

> Capability #149 — **Matrix Integration**

## Definition
```typescript
// workflow: MatrixIntegrationWorkflow
const MatrixIntegrationWorkflow: WorkflowDefinition = {
  workflowId: 'MatrixIntegrationWorkflow',
  version: '1.0.0',
  description: 'Matrix Integration — Load inventory -> Build matrix -> Metrics -> Report',
  trigger: { triggerId: 'InventoryUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Load inventory'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Build matrix'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Metrics'
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
Load inventory -> Build matrix -> Metrics -> Report

## Related artifacts
- [Protocol](../protocols/MatrixIntegrationProtocol.md) · [Trigger(s)](../triggers/MatrixIntegrationTrigger.md) · [Tasks](../tasks/MatrixIntegrationTask.md)
