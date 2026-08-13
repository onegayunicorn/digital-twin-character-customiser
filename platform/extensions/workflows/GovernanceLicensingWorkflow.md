# Workflow: GovernanceLicensingWorkflow

> Capability #165 — **Governance & Licensing**

## Definition
```typescript
// workflow: GovernanceLicensingWorkflow
const GovernanceLicensingWorkflow: WorkflowDefinition = {
  workflowId: 'GovernanceLicensingWorkflow',
  version: '1.0.0',
  description: 'Governance & Licensing — Propose -> Vote -> Approve -> License -> Monetize -> Audit',
  trigger: { triggerId: 'ProposalSubmittedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Propose'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Vote'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Approve'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'License'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Monetize'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
    name: 'Audit'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Propose -> Vote -> Approve -> License -> Monetize -> Audit

## Related artifacts
- [Protocol](../protocols/GovernanceLicensingProtocol.md) · [Trigger(s)](../triggers/GovernanceLicensingTrigger.md) · [Tasks](../tasks/GovernanceLicensingTask.md)
