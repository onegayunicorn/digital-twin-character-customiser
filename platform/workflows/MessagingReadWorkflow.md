# Workflow: MessagingReadWorkflow

> Capability #21 — **Messaging Read**

## Definition
```typescript
// workflow: MessagingReadWorkflow
const MessagingReadWorkflow: WorkflowDefinition = {
  workflowId: 'MessagingReadWorkflow',
  version: '1.0.0',
  description: 'Messaging Read — Pull -> Validate -> Process -> Ack -> Commit offset',
  trigger: { triggerId: 'MessageAvailableTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Pull'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Process'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Ack'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Commit offset'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Pull -> Validate -> Process -> Ack -> Commit offset

## Related artifacts
- [Protocol](../protocols/MessagingReadProtocol.md) · [Trigger(s)](../triggers/MessagingReadTrigger.md) · [Tasks](../tasks/MessagingReadTask.md)
