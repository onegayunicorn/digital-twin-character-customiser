# Workflow: AccountSettingsWriteWorkflow

> Capability #66 — **Account Settings Write**

## Definition
```typescript
// workflow: AccountSettingsWriteWorkflow
const AccountSettingsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccountSettingsWriteWorkflow',
  version: '1.0.0',
  description: 'Account Settings Write — Modify -> Validate -> Apply -> Sync -> Audit',
  trigger: { triggerId: 'AccountSettingsUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Modify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Apply'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Sync'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Audit'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Modify -> Validate -> Apply -> Sync -> Audit

## Related artifacts
- [Protocol](../protocols/AccountSettingsWriteProtocol.md) · [Trigger(s)](../triggers/AccountSettingsWriteTrigger.md) · [Tasks](../tasks/AccountSettingsWriteTask.md)
