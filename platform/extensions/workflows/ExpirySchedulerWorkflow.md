# Workflow: ExpirySchedulerWorkflow

> Capability #167 — **Expiry Scheduler**

## Definition
```typescript
// workflow: ExpirySchedulerWorkflow
const ExpirySchedulerWorkflow: WorkflowDefinition = {
  workflowId: 'ExpirySchedulerWorkflow',
  version: '1.0.0',
  description: 'Expiry Scheduler — Register -> Tick hourly -> Expire stale -> Notify',
  trigger: { triggerId: 'ExpiryTickTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Tick hourly'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Expire stale'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Notify'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Register -> Tick hourly -> Expire stale -> Notify

## Related artifacts
- [Protocol](../protocols/ExpirySchedulerProtocol.md) · [Trigger(s)](../triggers/ExpirySchedulerTrigger.md) · [Tasks](../tasks/ExpirySchedulerTask.md)
