# Workflow: EmailRoutingAddressesWriteWorkflow

> Capability #76 — **Email Routing Addresses Write**

## Definition
```typescript
// workflow: EmailRoutingAddressesWriteWorkflow
const EmailRoutingAddressesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'EmailRoutingAddressesWriteWorkflow',
  version: '1.0.0',
  description: 'Email Routing Addresses Write — Create -> Verify DNS -> Activate -> Test',
  trigger: { triggerId: 'EmailAddressCreatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Create'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Verify DNS'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Activate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Create -> Verify DNS -> Activate -> Test

## Related artifacts
- [Protocol](../protocols/EmailRoutingAddressesWriteProtocol.md) · [Trigger(s)](../triggers/EmailRoutingAddressesWriteTrigger.md) · [Tasks](../tasks/EmailRoutingAddressesWriteTask.md)
