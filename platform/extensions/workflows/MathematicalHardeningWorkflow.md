# Workflow: MathematicalHardeningWorkflow

> Capability #151 — **Mathematical Hardening**

## Definition
```typescript
// workflow: MathematicalHardeningWorkflow
const MathematicalHardeningWorkflow: WorkflowDefinition = {
  workflowId: 'MathematicalHardeningWorkflow',
  version: '1.0.0',
  description: 'Mathematical Hardening — Analyze -> Condition -> Residual -> Grade -> Report',
  trigger: { triggerId: 'SimOutputReadyTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Analyze'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Condition'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Residual'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Grade'
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
Analyze -> Condition -> Residual -> Grade -> Report

## Related artifacts
- [Protocol](../protocols/MathematicalHardeningProtocol.md) · [Trigger(s)](../triggers/MathematicalHardeningTrigger.md) · [Tasks](../tasks/MathematicalHardeningTask.md)
