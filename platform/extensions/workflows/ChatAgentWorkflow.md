# Workflow: ChatAgentWorkflow

> Capability #148 — **Chat Agent**

## Definition
```typescript
// workflow: ChatAgentWorkflow
const ChatAgentWorkflow: WorkflowDefinition = {
  workflowId: 'ChatAgentWorkflow',
  version: '1.0.0',
  description: 'Chat Agent — Parse -> Classify -> Route/Refuse -> Reply',
  trigger: { triggerId: 'MessageReceivedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Parse'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Classify'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Route/Refuse'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Reply'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Parse -> Classify -> Route/Refuse -> Reply

## Related artifacts
- [Protocol](../protocols/ChatAgentProtocol.md) · [Trigger(s)](../triggers/ChatAgentTrigger.md) · [Tasks](../tasks/ChatAgentTask.md)
