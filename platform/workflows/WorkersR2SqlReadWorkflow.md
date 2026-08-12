# Workflow: WorkersR2SqlReadWorkflow

> Capability #18 — **Workers R2 SQL Read**

## Definition
```typescript
// workflow: WorkersR2SqlReadWorkflow
const WorkersR2SqlReadWorkflow: WorkflowDefinition = {
  workflowId: 'WorkersR2SqlReadWorkflow',
  version: '1.0.0',
  description: 'Workers R2 SQL Read — Auth -> Parse -> Plan -> Execute -> Return results',
  trigger: { triggerId: 'R2SQLQueryTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Auth'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Parse'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Plan'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Execute'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Return results'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Auth -> Parse -> Plan -> Execute -> Return results

## Related artifacts
- [Protocol](../protocols/WorkersR2SqlReadProtocol.md) · [Trigger(s)](../triggers/WorkersR2SqlReadTrigger.md) · [Tasks](../tasks/WorkersR2SqlReadTask.md)
