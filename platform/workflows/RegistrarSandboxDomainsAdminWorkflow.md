# Workflow: RegistrarSandboxDomainsAdminWorkflow

> Capability #34 — **Registrar Sandbox Domains Admin**

## Definition
```typescript
// workflow: RegistrarSandboxDomainsAdminWorkflow
const RegistrarSandboxDomainsAdminWorkflow: WorkflowDefinition = {
  workflowId: 'RegistrarSandboxDomainsAdminWorkflow',
  version: '1.0.0',
  description: 'Registrar Sandbox Domains Admin — Create -> Assign -> Test -> Expire -> Cleanup',
  trigger: { triggerId: 'SandboxDomainCreatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Assign'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Expire'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Cleanup'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Create -> Assign -> Test -> Expire -> Cleanup

## Related artifacts
- [Protocol](../protocols/RegistrarSandboxDomainsAdminProtocol.md) · [Trigger(s)](../triggers/RegistrarSandboxDomainsAdminTrigger.md) · [Tasks](../tasks/RegistrarSandboxDomainsAdminTask.md)
