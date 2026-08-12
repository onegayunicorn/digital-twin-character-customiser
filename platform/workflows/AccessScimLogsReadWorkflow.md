# Workflow: AccessScimLogsReadWorkflow

> Capability #115 — **Access: SCIM Logs Read**

## Definition
```typescript
// workflow: AccessScimLogsReadWorkflow
const AccessScimLogsReadWorkflow: WorkflowDefinition = {
  workflowId: 'AccessScimLogsReadWorkflow',
  version: '1.0.0',
  description: 'Access: SCIM Logs Read — Collect -> Review -> Troubleshoot -> Report',
  trigger: { triggerId: 'SCIMSyncCompletedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Collect'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Review'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Troubleshoot'
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
Collect -> Review -> Troubleshoot -> Report

## Related artifacts
- [Protocol](../protocols/AccessScimLogsReadProtocol.md) · [Trigger(s)](../triggers/AccessScimLogsReadTrigger.md) · [Tasks](../tasks/AccessScimLogsReadTask.md)
