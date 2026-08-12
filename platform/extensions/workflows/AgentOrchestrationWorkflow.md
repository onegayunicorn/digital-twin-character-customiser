# Workflow: AgentOrchestrationWorkflow

> Capability #133 — **Agent Orchestration**

## Definition
```typescript
// workflow: AgentOrchestrationWorkflow
const AgentOrchestrationWorkflow: WorkflowDefinition = {
  workflowId: 'AgentOrchestrationWorkflow',
  version: '1.0.0',
  description: 'Agent Orchestration — Enqueue -> Schedule -> Execute -> Audit',
  trigger: { triggerId: 'TaskQueuedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Enqueue'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Schedule'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Execute'
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
Enqueue -> Schedule -> Execute -> Audit

## Related artifacts
- [Protocol](../protocols/AgentOrchestrationProtocol.md) · [Trigger(s)](../triggers/AgentOrchestrationTrigger.md) · [Tasks](../tasks/AgentOrchestrationTask.md)
