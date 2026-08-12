# Workflow: AccessKeysWriteWorkflow

> Capability #106 — **Access: Keys Write**

## Definition
```typescript
// workflow: AccessKeysWriteWorkflow
const AccessKeysWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessKeysWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Keys Write — Create -> Scope -> Distribute -> Rotate -> Revoke',
  trigger: { triggerId: 'AccessKeyCreatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Scope'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Distribute'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Rotate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Revoke'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Create -> Scope -> Distribute -> Rotate -> Revoke

## Related artifacts
- [Protocol](../protocols/AccessKeysWriteProtocol.md) · [Trigger(s)](../triggers/AccessKeysWriteTrigger.md) · [Tasks](../tasks/AccessKeysWriteTask.md)
