# Workflow: MedicalDecisionSupportWorkflow

> Capability #138 — **Medical Decision Support**

## Definition
```typescript
// workflow: MedicalDecisionSupportWorkflow
const MedicalDecisionSupportWorkflow: WorkflowDefinition = {
  workflowId: 'MedicalDecisionSupportWorkflow',
  version: '1.0.0',
  description: 'Medical Decision Support — Ingest -> Score -> Present -> Log -> Escalate',
  trigger: { triggerId: 'VitalsReceivedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Ingest'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Score'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Present'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Log'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Escalate'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Ingest -> Score -> Present -> Log -> Escalate

## Related artifacts
- [Protocol](../protocols/MedicalDecisionSupportProtocol.md) · [Trigger(s)](../triggers/MedicalDecisionSupportTrigger.md) · [Tasks](../tasks/MedicalDecisionSupportTask.md)
