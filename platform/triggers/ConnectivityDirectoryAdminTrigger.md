# Trigger: ConnectivityDirectoryAdminTrigger

> Capability #87 — **Connectivity Directory Admin**

Event source(s) that initiate execution for this capability.

### Trigger: ConnectivityUpdatedTrigger

```typescript
// trigger: ConnectivityUpdatedTrigger
const ConnectivityUpdatedTriggerContract: TriggerContract = {
  triggerId: 'ConnectivityUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ConnectivityUpdatedTrigger' },
  actionTarget: 'ManageConnectivityDirectoryTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ConnectivityDirectoryAdminProtocol.md) · [Tasks](../tasks/ConnectivityDirectoryAdminTask.md) · [Workflow](../workflows/ConnectivityDirectoryAdminWorkflow.md)
