# Trigger: AccessScimLogsReadTrigger

> Capability #115 — **Access: SCIM Logs Read**

Event source(s) that initiate execution for this capability.

### Trigger: SCIMSyncCompletedTrigger

```typescript
// trigger: SCIMSyncCompletedTrigger
const SCIMSyncCompletedTriggerContract: TriggerContract = {
  triggerId: 'SCIMSyncCompletedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SCIMSyncCompletedTrigger' },
  actionTarget: 'ReadSCIMLogTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessScimLogsReadProtocol.md) · [Tasks](../tasks/AccessScimLogsReadTask.md) · [Workflow](../workflows/AccessScimLogsReadWorkflow.md)
