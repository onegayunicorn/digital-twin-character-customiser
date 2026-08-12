# Workflow: ZeroTrustWriteWorkflow

> Capability #128 — **Zero Trust Write**

## Definition
```typescript
// workflow: ZeroTrustWriteWorkflow
const ZeroTrustWriteWorkflow: WorkflowDefinition = {
  workflowId: 'ZeroTrustWriteWorkflow',
  version: '1.0.0',
  description: 'Zero Trust Write — Identify assets -> Classify -> Design policies -> Deploy -> Validate -> Iterate',
  trigger: { triggerId: 'ZeroTrustConfigTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Identify assets'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Classify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Design policies'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Deploy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Validate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
    name: 'Iterate'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Identify assets -> Classify -> Design policies -> Deploy -> Validate -> Iterate

## Related artifacts
- [Protocol](../protocols/ZeroTrustWriteProtocol.md) · [Trigger(s)](../triggers/ZeroTrustWriteTrigger.md) · [Tasks](../tasks/ZeroTrustWriteTask.md)
