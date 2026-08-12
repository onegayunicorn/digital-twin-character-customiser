# Trigger: GovernanceOrchestratorTrigger

> Capability #144 — **Governance Orchestrator**

Event source(s) that initiate execution for this capability.

### Trigger: BatchReceivedTrigger

```typescript
// trigger: BatchReceivedTrigger
const BatchReceivedTriggerContract: TriggerContract = {
  triggerId: 'BatchReceivedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for BatchReceivedTrigger' },
  actionTarget: 'RouteBatchTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/GovernanceOrchestratorProtocol.md) · [Tasks](../tasks/GovernanceOrchestratorTask.md) · [Workflow](../workflows/GovernanceOrchestratorWorkflow.md)
