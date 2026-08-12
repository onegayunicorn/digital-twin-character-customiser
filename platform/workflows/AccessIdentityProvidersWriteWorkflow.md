# Workflow: AccessIdentityProvidersWriteWorkflow

> Capability #104 — **Access: Identity Providers Write**

## Definition
```typescript
// workflow: AccessIdentityProvidersWriteWorkflow
const AccessIdentityProvidersWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessIdentityProvidersWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Identity Providers Write — Register -> Configure -> Map attributes -> Test -> Enable',
  trigger: { triggerId: 'IdPConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Configure'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Map attributes'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Enable'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Register -> Configure -> Map attributes -> Test -> Enable

## Related artifacts
- [Protocol](../protocols/AccessIdentityProvidersWriteProtocol.md) · [Trigger(s)](../triggers/AccessIdentityProvidersWriteTrigger.md) · [Tasks](../tasks/AccessIdentityProvidersWriteTask.md)
