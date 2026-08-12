# Workflow: WorkersObservabilityTelemetryWriteWorkflow

> Capability #25 — **Workers Observability Telemetry Write**

## Definition
```typescript
// workflow: WorkersObservabilityTelemetryWriteWorkflow
const WorkersObservabilityTelemetryWriteWorkflow: WorkflowDefinition = {
  workflowId: 'WorkersObservabilityTelemetryWriteWorkflow',
  version: '1.0.0',
  description: 'Workers Observability Telemetry Write — Instrument -> Collect -> Sample -> Export -> Store',
  trigger: { triggerId: 'TelemetryIngestTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Instrument'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Collect'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Sample'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Export'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Store'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Instrument -> Collect -> Sample -> Export -> Store

## Related artifacts
- [Protocol](../protocols/WorkersObservabilityTelemetryWriteProtocol.md) · [Trigger(s)](../triggers/WorkersObservabilityTelemetryWriteTrigger.md) · [Tasks](../tasks/WorkersObservabilityTelemetryWriteTask.md)
