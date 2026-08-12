# Trigger: AccessAuditLogsReadTrigger

> Capability #101 — **Access: Audit Logs Read**

Event source(s) that initiate execution for this capability.

### Trigger: AuditLogGeneratedTrigger

```typescript
// trigger: AuditLogGeneratedTrigger
const AuditLogGeneratedTriggerContract: TriggerContract = {
  triggerId: 'AuditLogGeneratedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AuditLogGeneratedTrigger' },
  actionTarget: 'ReadAccessAuditLogTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessAuditLogsReadProtocol.md) · [Tasks](../tasks/AccessAuditLogsReadTask.md) · [Workflow](../workflows/AccessAuditLogsReadWorkflow.md)
