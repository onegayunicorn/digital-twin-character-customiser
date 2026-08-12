# Workflow: RepoSandboxWorkflow

> Capability #152 — **Repo Sandbox**

## Definition
```typescript
// workflow: RepoSandboxWorkflow
const RepoSandboxWorkflow: WorkflowDefinition = {
  workflowId: 'RepoSandboxWorkflow',
  version: '1.0.0',
  description: 'Repo Sandbox — Load repo -> Generate sandbox -> Agent -> Verify -> Report',
  trigger: { triggerId: 'RepoInventoriedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Load repo'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Generate sandbox'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Agent'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Verify'
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
Load repo -> Generate sandbox -> Agent -> Verify -> Report

## Related artifacts
- [Protocol](../protocols/RepoSandboxProtocol.md) · [Trigger(s)](../triggers/RepoSandboxTrigger.md) · [Tasks](../tasks/RepoSandboxTask.md)
