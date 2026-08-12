# Workflow: PubsubConfigurationWriteWorkflow

> Capability #22 — **Pubsub Configuration Write**

## Definition
```typescript
// workflow: PubsubConfigurationWriteWorkflow
const PubsubConfigurationWriteWorkflow: WorkflowDefinition = {
  workflowId: 'PubsubConfigurationWriteWorkflow',
  version: '1.0.0',
  description: 'Pubsub Configuration Write — Create topic -> Create sub -> Set DLQ -> Attach policy -> Deploy',
  trigger: { triggerId: 'PubsubConfigChangeTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create topic'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Create sub'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Set DLQ'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Attach policy'
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
Create topic -> Create sub -> Set DLQ -> Attach policy -> Deploy

## Related artifacts
- [Protocol](../protocols/PubsubConfigurationWriteProtocol.md) · [Trigger(s)](../triggers/PubsubConfigurationWriteTrigger.md) · [Tasks](../tasks/PubsubConfigurationWriteTask.md)
