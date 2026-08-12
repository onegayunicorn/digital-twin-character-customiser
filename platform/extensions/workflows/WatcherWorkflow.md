# Workflow: WatcherWorkflow

> Capability #146 — **Watcher**

## Definition
```typescript
// workflow: WatcherWorkflow
const WatcherWorkflow: WorkflowDefinition = {
  workflowId: 'WatcherWorkflow',
  version: '1.0.0',
  description: 'Watcher — Collect -> Compare -> Flag -> Report',
  trigger: { triggerId: 'HealthCheckTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Collect'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Compare'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Flag'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
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
Collect -> Compare -> Flag -> Report

## Related artifacts
- [Protocol](../protocols/WatcherProtocol.md) · [Trigger(s)](../triggers/WatcherTrigger.md) · [Tasks](../tasks/WatcherTask.md)
