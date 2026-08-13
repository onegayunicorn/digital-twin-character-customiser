# Workflow: SupplyChainProvenanceWorkflow

> Capability #161 — **Supply Chain Provenance**

## Definition
```typescript
// workflow: SupplyChainProvenanceWorkflow
const SupplyChainProvenanceWorkflow: WorkflowDefinition = {
  workflowId: 'SupplyChainProvenanceWorkflow',
  version: '1.0.0',
  description: 'Supply Chain Provenance — Register SKU -> Serialise -> Track -> Verify chain -> Report',
  trigger: { triggerId: 'UnitSerialisedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register SKU'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Serialise'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Track'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Verify chain'
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
Register SKU -> Serialise -> Track -> Verify chain -> Report

## Related artifacts
- [Protocol](../protocols/SupplyChainProvenanceProtocol.md) · [Trigger(s)](../triggers/SupplyChainProvenanceTrigger.md) · [Tasks](../tasks/SupplyChainProvenanceTask.md)
