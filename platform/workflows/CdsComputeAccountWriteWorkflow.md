# Workflow: CdsComputeAccountWriteWorkflow

> Capability #121 — **CDS Compute Account Write**

## Definition
```typescript
// workflow: CdsComputeAccountWriteWorkflow
const CdsComputeAccountWriteWorkflow: WorkflowDefinition = {
  workflowId: 'CdsComputeAccountWriteWorkflow',
  version: '1.0.0',
  description: 'CDS Compute Account Write — Package -> Deploy -> Schedule -> Execute -> Collect results',
  trigger: { triggerId: 'CDSJobTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Package'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Schedule'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Execute'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Collect results'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Package -> Deploy -> Schedule -> Execute -> Collect results

## Related artifacts
- [Protocol](../protocols/CdsComputeAccountWriteProtocol.md) · [Trigger(s)](../triggers/CdsComputeAccountWriteTrigger.md) · [Tasks](../tasks/CdsComputeAccountWriteTask.md)
