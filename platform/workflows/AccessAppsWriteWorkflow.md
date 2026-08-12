# Workflow: AccessAppsWriteWorkflow

> Capability #100 — **Access: Apps Write**

## Definition
```typescript
// workflow: AccessAppsWriteWorkflow
const AccessAppsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessAppsWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Apps Write — Register -> Configure -> Attach policy -> Publish',
  trigger: { triggerId: 'AccessAppConfigTrigger' },
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
    name: 'Attach policy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Publish'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Register -> Configure -> Attach policy -> Publish

## Related artifacts
- [Protocol](../protocols/AccessAppsWriteProtocol.md) · [Trigger(s)](../triggers/AccessAppsWriteTrigger.md) · [Tasks](../tasks/AccessAppsWriteTask.md)
