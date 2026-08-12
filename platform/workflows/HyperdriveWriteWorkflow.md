# Workflow: HyperdriveWriteWorkflow

> Capability #11 — **Hyperdrive Write**

## Definition
```typescript
// workflow: HyperdriveWriteWorkflow
const HyperdriveWriteWorkflow: WorkflowDefinition = {
  workflowId: 'HyperdriveWriteWorkflow',
  version: '1.0.0',
  description: 'Hyperdrive Write — Register origin -> Set pool -> Apply caching -> Test connectivity',
  trigger: { triggerId: 'HyperdriveConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register origin'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Set pool'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Apply caching'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Test connectivity'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Register origin -> Set pool -> Apply caching -> Test connectivity

## Related artifacts
- [Protocol](../protocols/HyperdriveWriteProtocol.md) · [Trigger(s)](../triggers/HyperdriveWriteTrigger.md) · [Tasks](../tasks/HyperdriveWriteTask.md)
