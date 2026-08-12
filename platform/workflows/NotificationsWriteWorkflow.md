# Workflow: NotificationsWriteWorkflow

> Capability #69 — **Notifications Write**

## Definition
```typescript
// workflow: NotificationsWriteWorkflow
const NotificationsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'NotificationsWriteWorkflow',
  version: '1.0.0',
  description: 'Notifications Write — Define channel -> Set rules -> Template -> Test -> Activate',
  trigger: { triggerId: 'NotificationEventTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define channel'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Set rules'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Template'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
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
Define channel -> Set rules -> Template -> Test -> Activate

## Related artifacts
- [Protocol](../protocols/NotificationsWriteProtocol.md) · [Trigger(s)](../triggers/NotificationsWriteTrigger.md) · [Tasks](../tasks/NotificationsWriteTask.md)
