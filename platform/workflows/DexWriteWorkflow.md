# Workflow: DexWriteWorkflow

> Capability #127 — **DEX Write**

## Definition
```typescript
// workflow: DexWriteWorkflow
const DexWriteWorkflow: WorkflowDefinition = {
  workflowId: 'DexWriteWorkflow',
  version: '1.0.0',
  description: 'DEX Write — Define tests -> Deploy -> Collect -> Analyze -> Alert -> Report',
  trigger: { triggerId: 'DEXTestTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define tests'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Collect'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Analyze'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Alert'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
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
Define tests -> Deploy -> Collect -> Analyze -> Alert -> Report

## Related artifacts
- [Protocol](../protocols/DexWriteProtocol.md) · [Trigger(s)](../triggers/DexWriteTrigger.md) · [Tasks](../tasks/DexWriteTask.md)
