# Workflow: ZeroTrustPiiReadWorkflow

> Capability #131 — **Zero Trust: PII Read**

## Definition
```typescript
// workflow: ZeroTrustPiiReadWorkflow
const ZeroTrustPiiReadWorkflow: WorkflowDefinition = {
  workflowId: 'ZeroTrustPiiReadWorkflow',
  version: '1.0.0',
  description: 'Zero Trust: PII Read — Request -> Auth -> Minimize -> Access -> Export/Delete -> Audit',
  trigger: { triggerId: 'PIIAccessRequestTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Request'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Auth'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Minimize'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Access'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Export/Delete'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step6'
    name: 'Audit'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Request -> Auth -> Minimize -> Access -> Export/Delete -> Audit

## Related artifacts
- [Protocol](../protocols/ZeroTrustPiiReadProtocol.md) · [Trigger(s)](../triggers/ZeroTrustPiiReadTrigger.md) · [Tasks](../tasks/ZeroTrustPiiReadTask.md)
