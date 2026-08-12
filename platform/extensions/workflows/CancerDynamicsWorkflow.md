# Workflow: CancerDynamicsWorkflow

> Capability #140 — **Cancer Dynamics**

## Definition
```typescript
// workflow: CancerDynamicsWorkflow
const CancerDynamicsWorkflow: WorkflowDefinition = {
  workflowId: 'CancerDynamicsWorkflow',
  version: '1.0.0',
  description: 'Cancer Dynamics — Init -> Grow -> Treat -> Detect rebound -> Report',
  trigger: { triggerId: 'TherapyScenarioTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Init'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Grow'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Treat'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Detect rebound'
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
Init -> Grow -> Treat -> Detect rebound -> Report

## Related artifacts
- [Protocol](../protocols/CancerDynamicsProtocol.md) · [Trigger(s)](../triggers/CancerDynamicsTrigger.md) · [Tasks](../tasks/CancerDynamicsTask.md)
