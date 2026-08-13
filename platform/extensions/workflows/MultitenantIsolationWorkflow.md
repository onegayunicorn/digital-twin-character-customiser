# Workflow: MultitenantIsolationWorkflow

> Capability #164 — **Multi-Tenant Isolation**

## Definition
```typescript
// workflow: MultitenantIsolationWorkflow
const MultitenantIsolationWorkflow: WorkflowDefinition = {
  workflowId: 'MultitenantIsolationWorkflow',
  version: '1.0.0',
  description: 'Multi-Tenant Isolation — Register -> Derive keys -> Bind DID -> Isolate state -> Verify',
  trigger: { triggerId: 'TenantCreatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Derive keys'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Bind DID'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Isolate state'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Verify'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Register -> Derive keys -> Bind DID -> Isolate state -> Verify

## Related artifacts
- [Protocol](../protocols/MultitenantIsolationProtocol.md) · [Trigger(s)](../triggers/MultitenantIsolationTrigger.md) · [Tasks](../tasks/MultitenantIsolationTask.md)
