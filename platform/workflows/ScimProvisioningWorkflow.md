# Workflow: ScimProvisioningWorkflow

> Capability #71 — **SCIM Provisioning**

## Definition
```typescript
// workflow: ScimProvisioningWorkflow
const ScimProvisioningWorkflow: WorkflowDefinition = {
  workflowId: 'ScimProvisioningWorkflow',
  version: '1.0.0',
  description: 'SCIM Provisioning — Pull from IdP -> Map -> Create/Update -> Deprovision -> Report',
  trigger: { triggerId: 'SCIMSyncTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Pull from IdP'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Map'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Create/Update'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deprovision'
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
Pull from IdP -> Map -> Create/Update -> Deprovision -> Report

## Related artifacts
- [Protocol](../protocols/ScimProvisioningProtocol.md) · [Trigger(s)](../triggers/ScimProvisioningTrigger.md) · [Tasks](../tasks/ScimProvisioningTask.md)
