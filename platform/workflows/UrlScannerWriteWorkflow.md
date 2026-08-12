# Workflow: UrlScannerWriteWorkflow

> Capability #54 — **URL Scanner Write**

## Definition
```typescript
// workflow: UrlScannerWriteWorkflow
const UrlScannerWriteWorkflow: WorkflowDefinition = {
  workflowId: 'UrlScannerWriteWorkflow',
  version: '1.0.0',
  description: 'URL Scanner Write — Submit -> Scan -> Analyze -> Score -> Flag/Report',
  trigger: { triggerId: 'URLSubmittedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Submit'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Scan'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Analyze'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Score'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Flag/Report'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Submit -> Scan -> Analyze -> Score -> Flag/Report

## Related artifacts
- [Protocol](../protocols/UrlScannerWriteProtocol.md) · [Trigger(s)](../triggers/UrlScannerWriteTrigger.md) · [Tasks](../tasks/UrlScannerWriteTask.md)
