# Workflow: CrystalNucleationSimWorkflow

> Capability #135 — **Crystal Nucleation Sim**

## Definition
```typescript
// workflow: CrystalNucleationSimWorkflow
const CrystalNucleationSimWorkflow: WorkflowDefinition = {
  workflowId: 'CrystalNucleationSimWorkflow',
  version: '1.0.0',
  description: 'Crystal Nucleation Sim — Init -> Nucleate -> Grow -> Feedback -> Stabilize',
  trigger: { triggerId: 'SimulationStepTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Init'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Nucleate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Grow'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Feedback'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Stabilize'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Init -> Nucleate -> Grow -> Feedback -> Stabilize

## Related artifacts
- [Protocol](../protocols/CrystalNucleationSimProtocol.md) · [Trigger(s)](../triggers/CrystalNucleationSimTrigger.md) · [Tasks](../tasks/CrystalNucleationSimTask.md)
