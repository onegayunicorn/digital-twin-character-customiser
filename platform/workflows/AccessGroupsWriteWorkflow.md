# Workflow: AccessGroupsWriteWorkflow

> Capability #105 — **Access: Groups Write**

## Definition
```typescript
// workflow: AccessGroupsWriteWorkflow
const AccessGroupsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessGroupsWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Groups Write — Create -> Add members -> Assign policies -> Sync',
  trigger: { triggerId: 'GroupMembershipChangedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Add members'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Assign policies'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Sync'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Create -> Add members -> Assign policies -> Sync

## Related artifacts
- [Protocol](../protocols/AccessGroupsWriteProtocol.md) · [Trigger(s)](../triggers/AccessGroupsWriteTrigger.md) · [Tasks](../tasks/AccessGroupsWriteTask.md)
