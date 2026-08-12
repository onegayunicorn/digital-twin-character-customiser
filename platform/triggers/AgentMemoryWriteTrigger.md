# Trigger: AgentMemoryWriteTrigger

> Capability #1 — **Agent Memory Write**

Event source(s) that initiate execution for this capability.

### Trigger: AgentMemoryUpdatedTrigger

```typescript
// trigger: AgentMemoryUpdatedTrigger
const AgentMemoryUpdatedTriggerContract: TriggerContract = {
  triggerId: 'AgentMemoryUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'on memory entry created/updated/expired' },
  actionTarget: 'WriteAgentMemoryTask (persist/modify agent memory records)',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AgentMemoryWriteProtocol.md) · [Tasks](../tasks/AgentMemoryWriteTask.md) · [Workflow](../workflows/AgentMemoryWriteWorkflow.md)
