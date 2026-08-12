# Workflow: PhotonicAnalysisWorkflow

> Capability #136 — **Photonic Analysis**

## Definition
```typescript
// workflow: PhotonicAnalysisWorkflow
const PhotonicAnalysisWorkflow: WorkflowDefinition = {
  workflowId: 'PhotonicAnalysisWorkflow',
  version: '1.0.0',
  description: 'Photonic Analysis — Ingest -> Classical metrics -> Quantum verify -> Verdict -> Report',
  trigger: { triggerId: 'MeasurementIngestedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Ingest'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Classical metrics'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Quantum verify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Verdict'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Report'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Ingest -> Classical metrics -> Quantum verify -> Verdict -> Report

## Related artifacts
- [Protocol](../protocols/PhotonicAnalysisProtocol.md) · [Trigger(s)](../triggers/PhotonicAnalysisTrigger.md) · [Tasks](../tasks/PhotonicAnalysisTask.md)
