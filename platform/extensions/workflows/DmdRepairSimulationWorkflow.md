# Workflow: DmdRepairSimulationWorkflow

> Capability #139 — **DMD Repair Simulation**

## Definition
```typescript
// workflow: DmdRepairSimulationWorkflow
const DmdRepairSimulationWorkflow: WorkflowDefinition = {
  workflowId: 'DmdRepairSimulationWorkflow',
  version: '1.0.0',
  description: 'DMD Repair Simulation — Classify -> Codon analysis -> Mechanism sim -> Disclaimer -> Report',
  trigger: { triggerId: 'MutationIngestedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Classify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Codon analysis'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Mechanism sim'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Disclaimer'
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
Classify -> Codon analysis -> Mechanism sim -> Disclaimer -> Report

## Related artifacts
- [Protocol](../protocols/DmdRepairSimulationProtocol.md) · [Trigger(s)](../triggers/DmdRepairSimulationTrigger.md) · [Tasks](../tasks/DmdRepairSimulationTask.md)
