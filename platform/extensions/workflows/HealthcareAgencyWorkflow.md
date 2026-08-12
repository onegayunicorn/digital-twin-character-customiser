# Workflow: HealthcareAgencyWorkflow

> Capability #143 — **Healthcare Agency**

## Definition
```typescript
// workflow: HealthcareAgencyWorkflow
const HealthcareAgencyWorkflow: WorkflowDefinition = {
  workflowId: 'HealthcareAgencyWorkflow',
  version: '1.0.0',
  description: 'Healthcare Agency — Dispatch -> Execute -> Guardrail check -> Audit -> Report',
  trigger: { triggerId: 'AgencyRequestTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Dispatch'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Execute'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Guardrail check'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Audit'
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
Dispatch -> Execute -> Guardrail check -> Audit -> Report

## Related artifacts
- [Protocol](../protocols/HealthcareAgencyProtocol.md) · [Trigger(s)](../triggers/HealthcareAgencyTrigger.md) · [Tasks](../tasks/HealthcareAgencyTask.md)
