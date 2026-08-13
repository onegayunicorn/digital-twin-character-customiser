# Workflow: ProcurementEngineWorkflow

> Capability #158 — **Procurement Engine**

## Definition
```typescript
// workflow: ProcurementEngineWorkflow
const ProcurementEngineWorkflow: WorkflowDefinition = {
  workflowId: 'ProcurementEngineWorkflow',
  version: '1.0.0',
  description: 'Procurement Engine — Tender -> Bids -> Evaluate -> PO -> GRN -> Invoice -> Match -> Pay',
  trigger: { triggerId: 'TenderOpenedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Tender'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Bids'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Evaluate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'PO'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'GRN'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
    name: 'Invoice'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step7'
    name: 'Match'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step8'
    name: 'Pay'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Tender -> Bids -> Evaluate -> PO -> GRN -> Invoice -> Match -> Pay

## Related artifacts
- [Protocol](../protocols/ProcurementEngineProtocol.md) · [Trigger(s)](../triggers/ProcurementEngineTrigger.md) · [Tasks](../tasks/ProcurementEngineTask.md)
