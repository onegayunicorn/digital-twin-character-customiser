# Workflow: RadarReadWorkflow

> Capability #97 — **Radar Read**

## Definition
```typescript
// workflow: RadarReadWorkflow
const RadarReadWorkflow: WorkflowDefinition = {
  workflowId: 'RadarReadWorkflow',
  version: '1.0.0',
  description: 'Radar Read — Query -> Analyze -> Visualize -> Report',
  trigger: { triggerId: 'RadarDataUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Query'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Analyze'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Visualize'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
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
Query -> Analyze -> Visualize -> Report

## Related artifacts
- [Protocol](../protocols/RadarReadProtocol.md) · [Trigger(s)](../triggers/RadarReadTrigger.md) · [Tasks](../tasks/RadarReadTask.md)
