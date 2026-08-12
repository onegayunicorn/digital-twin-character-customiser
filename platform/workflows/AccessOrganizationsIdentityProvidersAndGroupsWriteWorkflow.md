# Workflow: AccessOrganizationsIdentityProvidersAndGroupsWriteWorkflow

> Capability #109 — **Access: Organizations, Identity Providers, and Groups Write**

## Definition
```typescript
// workflow: AccessOrganizationsIdentityProvidersAndGroupsWriteWorkflow
const AccessOrganizationsIdentityProvidersAndGroupsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessOrganizationsIdentityProvidersAndGroupsWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Organizations, Identity Providers, and Groups Write — Sync IdP -> Map groups -> Assign org -> Provision users',
  trigger: { triggerId: 'OrgStructureUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Sync IdP'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Map groups'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Assign org'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Provision users'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Sync IdP -> Map groups -> Assign org -> Provision users

## Related artifacts
- [Protocol](../protocols/AccessOrganizationsIdentityProvidersAndGroupsWriteProtocol.md) · [Trigger(s)](../triggers/AccessOrganizationsIdentityProvidersAndGroupsWriteTrigger.md) · [Tasks](../tasks/AccessOrganizationsIdentityProvidersAndGroupsWriteTask.md)
