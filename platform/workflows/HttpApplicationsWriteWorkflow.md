# Workflow: HttpApplicationsWriteWorkflow

> Capability #47 — **HTTP Applications Write**

## Definition
```typescript
// workflow: HttpApplicationsWriteWorkflow
const HttpApplicationsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'HttpApplicationsWriteWorkflow',
  version: '1.0.0',
  description: 'HTTP Applications Write — Define origin -> Set routing -> Configure headers -> Deploy -> Test',
  trigger: { triggerId: 'HTTPAppConfigTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define origin'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Set routing'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Configure headers'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
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
Define origin -> Set routing -> Configure headers -> Deploy -> Test

## Related artifacts
- [Protocol](../protocols/HttpApplicationsWriteProtocol.md) · [Trigger(s)](../triggers/HttpApplicationsWriteTrigger.md) · [Tasks](../tasks/HttpApplicationsWriteTask.md)
