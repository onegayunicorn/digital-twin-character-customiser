# Workflow: TrustAndSafetyWriteWorkflow

> Capability #52 — **Trust and Safety Write**

## Definition
```typescript
// workflow: TrustAndSafetyWriteWorkflow
const TrustAndSafetyWriteWorkflow: WorkflowDefinition = {
  workflowId: 'TrustAndSafetyWriteWorkflow',
  version: '1.0.0',
  description: 'Trust and Safety Write — Review -> Classify -> Action -> Notify -> Log',
  trigger: { triggerId: 'ContentReportedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Review'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Classify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Action'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Notify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Log'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Review -> Classify -> Action -> Notify -> Log

## Related artifacts
- [Protocol](../protocols/TrustAndSafetyWriteProtocol.md) · [Trigger(s)](../triggers/TrustAndSafetyWriteTrigger.md) · [Tasks](../tasks/TrustAndSafetyWriteTask.md)
