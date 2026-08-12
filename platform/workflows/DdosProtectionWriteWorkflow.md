# Workflow: DdosProtectionWriteWorkflow

> Capability #43 — **DDoS Protection Write**

## Definition
```typescript
// workflow: DdosProtectionWriteWorkflow
const DdosProtectionWriteWorkflow: WorkflowDefinition = {
  workflowId: 'DdosProtectionWriteWorkflow',
  version: '1.0.0',
  description: 'DDoS Protection Write — Detect -> Classify -> Activate mitigation -> Monitor -> Release',
  trigger: { triggerId: 'DDoSEventDetectedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Detect'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Classify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Activate mitigation'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Monitor'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Release'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Detect -> Classify -> Activate mitigation -> Monitor -> Release

## Related artifacts
- [Protocol](../protocols/DdosProtectionWriteProtocol.md) · [Trigger(s)](../triggers/DdosProtectionWriteTrigger.md) · [Tasks](../tasks/DdosProtectionWriteTask.md)
