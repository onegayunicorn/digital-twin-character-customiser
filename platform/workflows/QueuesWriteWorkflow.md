# Workflow: QueuesWriteWorkflow

> Capability #23 — **Queues Write**

## Definition
```typescript
// workflow: QueuesWriteWorkflow
const QueuesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'QueuesWriteWorkflow',
  version: '1.0.0',
  description: 'Queues Write — Send -> Batch -> Deliver -> Process -> Ack/Retry',
  trigger: { triggerId: 'QueueMessageEnqueueTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Send'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Batch'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Deliver'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Process'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Ack/Retry'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Send -> Batch -> Deliver -> Process -> Ack/Retry

## Related artifacts
- [Protocol](../protocols/QueuesWriteProtocol.md) · [Trigger(s)](../triggers/QueuesWriteTrigger.md) · [Tasks](../tasks/QueuesWriteTask.md)
