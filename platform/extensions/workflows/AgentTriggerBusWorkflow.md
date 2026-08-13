# Workflow: AgentTriggerBusWorkflow

> Capability #168 — **Agent Trigger Bus**

## Definition
```typescript
// workflow: AgentTriggerBusWorkflow
const AgentTriggerBusWorkflow: WorkflowDefinition = {
  workflowId: 'AgentTriggerBusWorkflow',
  version: '1.0.0',
  description: 'Agent Trigger Bus — Event -> Route -> Wake agents -> Collect results -> Log',
  trigger: { triggerId: 'AnyPlatformEventTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Event'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Route'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Wake agents'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Collect results'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step5'
    name: 'Log'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Event -> Route -> Wake agents -> Collect results -> Log

## Related artifacts
- [Protocol](../protocols/AgentTriggerBusProtocol.md) · [Trigger(s)](../triggers/AgentTriggerBusTrigger.md) · [Tasks](../tasks/AgentTriggerBusTask.md)
