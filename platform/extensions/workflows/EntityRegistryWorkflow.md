# Workflow: EntityRegistryWorkflow

> Capability #160 — **Entity Registry**

## Definition
```typescript
// workflow: EntityRegistryWorkflow
const EntityRegistryWorkflow: WorkflowDefinition = {
  workflowId: 'EntityRegistryWorkflow',
  version: '1.0.0',
  description: 'Entity Registry — Register -> Verify type -> Ownership -> Governance -> Report',
  trigger: { triggerId: 'EntityRegisteredTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Register'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Verify type'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Ownership'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Governance'
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
Register -> Verify type -> Ownership -> Governance -> Report

## Related artifacts
- [Protocol](../protocols/EntityRegistryProtocol.md) · [Trigger(s)](../triggers/EntityRegistryTrigger.md) · [Tasks](../tasks/EntityRegistryTask.md)
