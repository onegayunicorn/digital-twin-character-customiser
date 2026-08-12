# Trigger: OneConnectorsWriteTrigger

> Capability #124 — **One Connectors Write**

Event source(s) that initiate execution for this capability.

### Trigger: ConnectorRegisteredTrigger

```typescript
// trigger: ConnectorRegisteredTrigger
const ConnectorRegisteredTriggerContract: TriggerContract = {
  triggerId: 'ConnectorRegisteredTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ConnectorRegisteredTrigger' },
  actionTarget: 'ManageOneConnectorTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/OneConnectorsWriteProtocol.md) · [Tasks](../tasks/OneConnectorsWriteTask.md) · [Workflow](../workflows/OneConnectorsWriteWorkflow.md)
