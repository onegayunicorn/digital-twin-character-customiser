# Workflow: AccessPolicyTestWriteWorkflow

> Capability #111 — **Access: Policy Test Write**

## Definition
```typescript
// workflow: AccessPolicyTestWriteWorkflow
const AccessPolicyTestWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessPolicyTestWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Policy Test Write — Select context -> Run simulation -> Compare -> Report -> Adjust',
  trigger: { triggerId: 'PolicyTestRunTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Select context'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Run simulation'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Compare'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Report'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Adjust'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Select context -> Run simulation -> Compare -> Report -> Adjust

## Related artifacts
- [Protocol](../protocols/AccessPolicyTestWriteProtocol.md) · [Trigger(s)](../triggers/AccessPolicyTestWriteTrigger.md) · [Tasks](../tasks/AccessPolicyTestWriteTask.md)
