# Workflow: JurisdictionEngineWorkflow

> Capability #155 — **Jurisdiction Engine**

## Definition
```typescript
// workflow: JurisdictionEngineWorkflow
const JurisdictionEngineWorkflow: WorkflowDefinition = {
  workflowId: 'JurisdictionEngineWorkflow',
  version: '1.0.0',
  description: 'Jurisdiction Engine — Classify -> Profile -> Check -> Warn -> Report',
  trigger: { triggerId: 'TransactionSubmittedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Classify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Profile'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Check'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Warn'
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
Classify -> Profile -> Check -> Warn -> Report

## Related artifacts
- [Protocol](../protocols/JurisdictionEngineProtocol.md) · [Trigger(s)](../triggers/JurisdictionEngineTrigger.md) · [Tasks](../tasks/JurisdictionEngineTask.md)
