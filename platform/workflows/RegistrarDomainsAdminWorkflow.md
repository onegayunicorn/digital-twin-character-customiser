# Workflow: RegistrarDomainsAdminWorkflow

> Capability #33 — **Registrar Domains Admin**

## Definition
```typescript
// workflow: RegistrarDomainsAdminWorkflow
const RegistrarDomainsAdminWorkflow: WorkflowDefinition = {
  workflowId: 'RegistrarDomainsAdminWorkflow',
  version: '1.0.0',
  description: 'Registrar Domains Admin — Check availability -> Register -> Configure DNS -> Activate',
  trigger: { triggerId: 'DomainEventTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Check availability'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Register'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Configure DNS'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Activate'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Check availability -> Register -> Configure DNS -> Activate

## Related artifacts
- [Protocol](../protocols/RegistrarDomainsAdminProtocol.md) · [Trigger(s)](../triggers/RegistrarDomainsAdminTrigger.md) · [Tasks](../tasks/RegistrarDomainsAdminTask.md)
