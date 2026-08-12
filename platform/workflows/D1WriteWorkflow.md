# Workflow: D1WriteWorkflow

> Capability #15 — **D1 Write**

## Definition
```typescript
// workflow: D1WriteWorkflow
const D1WriteWorkflow: WorkflowDefinition = {
  workflowId: 'D1WriteWorkflow',
  version: '1.0.0',
  description: 'D1 Write — Validate SQL -> Backup -> Apply migration -> Verify',
  trigger: { triggerId: 'MigrationTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Validate SQL'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Backup'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Apply migration'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Verify'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Validate SQL -> Backup -> Apply migration -> Verify

## Related artifacts
- [Protocol](../protocols/D1WriteProtocol.md) · [Trigger(s)](../triggers/D1WriteTrigger.md) · [Tasks](../tasks/D1WriteTask.md)
