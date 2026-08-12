# Workflow: IntegrationWriteWorkflow

> Capability #68 — **Integration Write**

## Definition
```typescript
// workflow: IntegrationWriteWorkflow
const IntegrationWriteWorkflow: WorkflowDefinition = {
  workflowId: 'IntegrationWriteWorkflow',
  version: '1.0.0',
  description: 'Integration Write — Select -> Auth -> Configure -> Test -> Activate',
  trigger: { triggerId: 'IntegrationConnectedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Select'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Auth'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Configure'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Activate'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Select -> Auth -> Configure -> Test -> Activate

## Related artifacts
- [Protocol](../protocols/IntegrationWriteProtocol.md) · [Trigger(s)](../triggers/IntegrationWriteTrigger.md) · [Tasks](../tasks/IntegrationWriteTask.md)
