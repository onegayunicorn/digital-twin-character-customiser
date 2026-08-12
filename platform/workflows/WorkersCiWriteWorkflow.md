# Workflow: WorkersCiWriteWorkflow

> Capability #10 — **Workers CI Write**

## Definition
```typescript
// workflow: WorkersCiWriteWorkflow
const WorkersCiWriteWorkflow: WorkflowDefinition = {
  workflowId: 'WorkersCiWriteWorkflow',
  version: '1.0.0',
  description: 'Workers CI Write — Lint -> Test -> Build -> Scan -> Deploy',
  trigger: { triggerId: 'CommitPushedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Lint'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Build'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Scan'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Lint -> Test -> Build -> Scan -> Deploy

## Related artifacts
- [Protocol](../protocols/WorkersCiWriteProtocol.md) · [Trigger(s)](../triggers/WorkersCiWriteTrigger.md) · [Tasks](../tasks/WorkersCiWriteTask.md)
