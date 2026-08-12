# Workflow: GovernanceOrchestratorWorkflow

> Capability #144 — **Governance Orchestrator**

## Definition
```typescript
// workflow: GovernanceOrchestratorWorkflow
const GovernanceOrchestratorWorkflow: WorkflowDefinition = {
  workflowId: 'GovernanceOrchestratorWorkflow',
  version: '1.0.0',
  description: 'Governance Orchestrator — Ingest -> Route -> Dispatch -> Audit',
  trigger: { triggerId: 'BatchReceivedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Ingest'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Route'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Dispatch'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
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
Ingest -> Route -> Dispatch -> Audit

## Related artifacts
- [Protocol](../protocols/GovernanceOrchestratorProtocol.md) · [Trigger(s)](../triggers/GovernanceOrchestratorTrigger.md) · [Tasks](../tasks/GovernanceOrchestratorTask.md)
