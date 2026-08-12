# Workflow: MagicWanWriteWorkflow

> Capability #93 — **Magic WAN Write**

## Definition
```typescript
// workflow: MagicWanWriteWorkflow
const MagicWanWriteWorkflow: WorkflowDefinition = {
  workflowId: 'MagicWanWriteWorkflow',
  version: '1.0.0',
  description: 'Magic WAN Write — Create tunnels -> Establish -> Configure routing -> Activate',
  trigger: { triggerId: 'WANConnectionTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create tunnels'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Establish'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Configure routing'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
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
Create tunnels -> Establish -> Configure routing -> Activate

## Related artifacts
- [Protocol](../protocols/MagicWanWriteProtocol.md) · [Trigger(s)](../triggers/MagicWanWriteTrigger.md) · [Tasks](../tasks/MagicWanWriteTask.md)
