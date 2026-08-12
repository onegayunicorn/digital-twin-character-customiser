# Workflow: AllowRequestTracerReadWorkflow

> Capability #39 — **Allow Request Tracer Read**

## Definition
```typescript
// workflow: AllowRequestTracerReadWorkflow
const AllowRequestTracerReadWorkflow: WorkflowDefinition = {
  workflowId: 'AllowRequestTracerReadWorkflow',
  version: '1.0.0',
  description: 'Allow Request Tracer Read — Capture -> Follow path -> Collect -> Analyze -> Report',
  trigger: { triggerId: 'TraceRequestTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Capture'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Follow path'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Collect'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Analyze'
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
Capture -> Follow path -> Collect -> Analyze -> Report

## Related artifacts
- [Protocol](../protocols/AllowRequestTracerReadProtocol.md) · [Trigger(s)](../triggers/AllowRequestTracerReadTrigger.md) · [Tasks](../tasks/AllowRequestTracerReadTask.md)
