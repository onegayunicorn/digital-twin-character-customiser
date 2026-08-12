# Workflow: ApplicationSecurityReportsReadWorkflow

> Capability #40 — **Application Security Reports Read**

## Definition
```typescript
// workflow: ApplicationSecurityReportsReadWorkflow
const ApplicationSecurityReportsReadWorkflow: WorkflowDefinition = {
  workflowId: 'ApplicationSecurityReportsReadWorkflow',
  version: '1.0.0',
  description: 'Application Security Reports Read — Collect data -> Analyze -> Generate -> Distribute -> Archive',
  trigger: { triggerId: 'ReportGeneratedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Collect data'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Analyze'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Generate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Distribute'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Archive'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Collect data -> Analyze -> Generate -> Distribute -> Archive

## Related artifacts
- [Protocol](../protocols/ApplicationSecurityReportsReadProtocol.md) · [Trigger(s)](../triggers/ApplicationSecurityReportsReadTrigger.md) · [Tasks](../tasks/ApplicationSecurityReportsReadTask.md)
