# Workflow: MassUrlRedirectsWriteWorkflow

> Capability #60 — **Mass URL Redirects Write**

## Definition
```typescript
// workflow: MassUrlRedirectsWriteWorkflow
const MassUrlRedirectsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'MassUrlRedirectsWriteWorkflow',
  version: '1.0.0',
  description: 'Mass URL Redirects Write — Import CSV -> Validate -> Deploy -> Test -> Verify',
  trigger: { triggerId: 'RedirectConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Import CSV'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Verify'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Import CSV -> Validate -> Deploy -> Test -> Verify

## Related artifacts
- [Protocol](../protocols/MassUrlRedirectsWriteProtocol.md) · [Trigger(s)](../triggers/MassUrlRedirectsWriteTrigger.md) · [Tasks](../tasks/MassUrlRedirectsWriteTask.md)
