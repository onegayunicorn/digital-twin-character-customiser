# Workflow: AccessDevicePostureWriteWorkflow

> Capability #102 — **Access: Device Posture Write**

## Definition
```typescript
// workflow: AccessDevicePostureWriteWorkflow
const AccessDevicePostureWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessDevicePostureWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Device Posture Write — Define checks -> Collect -> Evaluate -> Allow/Block',
  trigger: { triggerId: 'DevicePostureUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define checks'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Collect'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Evaluate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Allow/Block'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define checks -> Collect -> Evaluate -> Allow/Block

## Related artifacts
- [Protocol](../protocols/AccessDevicePostureWriteProtocol.md) · [Trigger(s)](../triggers/AccessDevicePostureWriteTrigger.md) · [Tasks](../tasks/AccessDevicePostureWriteTask.md)
