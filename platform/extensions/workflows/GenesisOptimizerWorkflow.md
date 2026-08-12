# Workflow: GenesisOptimizerWorkflow

> Capability #142 — **Genesis Optimizer**

## Definition
```typescript
// workflow: GenesisOptimizerWorkflow
const GenesisOptimizerWorkflow: WorkflowDefinition = {
  workflowId: 'GenesisOptimizerWorkflow',
  version: '1.0.0',
  description: 'Genesis Optimizer — Init population -> Evolve -> SPSA refine -> Validate -> Report',
  trigger: { triggerId: 'OptimizationRequestedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Init population'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Evolve'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'SPSA refine'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Validate'
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
Init population -> Evolve -> SPSA refine -> Validate -> Report

## Related artifacts
- [Protocol](../protocols/GenesisOptimizerProtocol.md) · [Trigger(s)](../triggers/GenesisOptimizerTrigger.md) · [Tasks](../tasks/GenesisOptimizerTask.md)
