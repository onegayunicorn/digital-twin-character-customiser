# Workflow: ChamberWriteSecretsStoreWorkflow

> Capability #13 — **Chamber Write -> Secrets Store**

## Definition
```typescript
// workflow: ChamberWriteSecretsStoreWorkflow
const ChamberWriteSecretsStoreWorkflow: WorkflowDefinition = {
  workflowId: 'ChamberWriteSecretsStoreWorkflow',
  version: '1.0.0',
  description: 'Chamber Write -> Secrets Store — Create -> Encrypt -> Store -> Grant access -> Rotate',
  trigger: { triggerId: 'SecretRotatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Encrypt'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Store'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Grant access'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Rotate'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Create -> Encrypt -> Store -> Grant access -> Rotate

## Related artifacts
- [Protocol](../protocols/ChamberWriteSecretsStoreProtocol.md) · [Trigger(s)](../triggers/ChamberWriteSecretsStoreTrigger.md) · [Tasks](../tasks/ChamberWriteSecretsStoreTask.md)
