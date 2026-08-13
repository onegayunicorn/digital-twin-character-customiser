# Workflow: IdentityPqcSigningWorkflow

> Capability #163 — **Identity & PQC Signing**

## Definition
```typescript
// workflow: IdentityPqcSigningWorkflow
const IdentityPqcSigningWorkflow: WorkflowDefinition = {
  workflowId: 'IdentityPqcSigningWorkflow',
  version: '1.0.0',
  description: 'Identity & PQC Signing — Create DID -> Bind -> Attest -> Sign -> Verify -> Report',
  trigger: { triggerId: 'DidVerifiedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create DID'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Bind'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Attest'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Sign'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Verify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
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
Create DID -> Bind -> Attest -> Sign -> Verify -> Report

## Related artifacts
- [Protocol](../protocols/IdentityPqcSigningProtocol.md) · [Trigger(s)](../triggers/IdentityPqcSigningTrigger.md) · [Tasks](../tasks/IdentityPqcSigningTask.md)
