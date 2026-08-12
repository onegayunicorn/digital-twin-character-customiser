# Workflow: AddressMapsWriteWorkflow

> Capability #84 — **Address Maps Write**

## Definition
```typescript
// workflow: AddressMapsWriteWorkflow
const AddressMapsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AddressMapsWriteWorkflow',
  version: '1.0.0',
  description: 'Address Maps Write — Define mappings -> Assign priority -> Validate -> Deploy',
  trigger: { triggerId: 'AddressMapUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define mappings'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Assign priority'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
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
Define mappings -> Assign priority -> Validate -> Deploy

## Related artifacts
- [Protocol](../protocols/AddressMapsWriteProtocol.md) · [Trigger(s)](../triggers/AddressMapsWriteTrigger.md) · [Tasks](../tasks/AddressMapsWriteTask.md)
