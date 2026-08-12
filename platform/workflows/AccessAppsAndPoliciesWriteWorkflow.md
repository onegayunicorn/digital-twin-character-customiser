# Workflow: AccessAppsAndPoliciesWriteWorkflow

> Capability #99 — **Access: Apps and Policies Write**

## Definition
```typescript
// workflow: AccessAppsAndPoliciesWriteWorkflow
const AccessAppsAndPoliciesWriteWorkflow: WorkflowDefinition = {
  workflowId: 'AccessAppsAndPoliciesWriteWorkflow',
  version: '1.0.0',
  description: 'Access: Apps and Policies Write — Define app -> Create policy -> Assign -> Test -> Activate',
  trigger: { triggerId: 'AccessPolicyUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Define app'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Create policy'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Assign'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Test'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Activate'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Define app -> Create policy -> Assign -> Test -> Activate

## Related artifacts
- [Protocol](../protocols/AccessAppsAndPoliciesWriteProtocol.md) · [Trigger(s)](../triggers/AccessAppsAndPoliciesWriteTrigger.md) · [Tasks](../tasks/AccessAppsAndPoliciesWriteTask.md)
