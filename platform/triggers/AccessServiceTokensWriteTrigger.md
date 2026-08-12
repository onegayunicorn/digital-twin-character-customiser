# Trigger: AccessServiceTokensWriteTrigger

> Capability #114 — **Access: Service Tokens Write**

Event source(s) that initiate execution for this capability.

### Trigger: ServiceTokenCreatedTrigger

```typescript
// trigger: ServiceTokenCreatedTrigger
const ServiceTokenCreatedTriggerContract: TriggerContract = {
  triggerId: 'ServiceTokenCreatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ServiceTokenCreatedTrigger' },
  actionTarget: 'IssueServiceTokenTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessServiceTokensWriteProtocol.md) · [Tasks](../tasks/AccessServiceTokensWriteTask.md) · [Workflow](../workflows/AccessServiceTokensWriteWorkflow.md)
