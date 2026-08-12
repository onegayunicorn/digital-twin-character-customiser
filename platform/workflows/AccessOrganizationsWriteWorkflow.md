# Workflow: AccessOrganizationsWriteWorkflow

> Capability #108 — **Access: Organizations Write**

## Definition
```typescript
// workflow: AccessOrganizationsWriteWorkflow
const AccessOrganizationsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessOrganizationsWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Organizations Write — Create -> Configure domains -> Invite admins -> Setup IdP',
  trigger: { triggerId: 'OrganizationCreatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Configure domains'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Invite admins'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Setup IdP'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Create -> Configure domains -> Invite admins -> Setup IdP

## Related artifacts
- [Protocol](../protocols/AccessOrganizationsWriteProtocol.md) · [Trigger(s)](../triggers/AccessOrganizationsWriteTrigger.md) · [Tasks](../tasks/AccessOrganizationsWriteTask.md)
