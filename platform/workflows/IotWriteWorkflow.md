# Workflow: IotWriteWorkflow

> Capability #48 — **IOT Write**

## Definition
```typescript
// workflow: IotWriteWorkflow
const IotWriteWorkflow: WorkflowDefinition = {
  workflowId: 'IotWriteWorkflow',
  version: '1.0.0',
  description: 'IOT Write — Register -> Auth -> Provision -> Monitor -> Update',
  trigger: { triggerId: 'DeviceConnectedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Auth'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Provision'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Monitor'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Update'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Register -> Auth -> Provision -> Monitor -> Update

## Related artifacts
- [Protocol](../protocols/IotWriteProtocol.md) · [Trigger(s)](../triggers/IotWriteTrigger.md) · [Tasks](../tasks/IotWriteTask.md)
