# Trigger: AgentOrchestrationTrigger

> Capability #133 — **Agent Orchestration**

Event source(s) that initiate execution for this capability.

### Trigger: TaskQueuedTrigger

```typescript
// trigger: TaskQueuedTrigger
const TaskQueuedTriggerContract: TriggerContract = {
  triggerId: 'TaskQueuedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for TaskQueuedTrigger' },
  actionTarget: 'DispatchTaskTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: AgentReadyTrigger

```typescript
// trigger: AgentReadyTrigger
const AgentReadyTriggerContract: TriggerContract = {
  triggerId: 'AgentReadyTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AgentReadyTrigger' },
  actionTarget: 'DispatchTaskTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AgentOrchestrationProtocol.md) · [Tasks](../tasks/AgentOrchestrationTask.md) · [Workflow](../workflows/AgentOrchestrationWorkflow.md)
