# Trigger: AccessSshAuditingWriteTrigger

> Capability #116 — **Access: SSH Auditing Write**

Event source(s) that initiate execution for this capability.

### Trigger: SSHSessionStartTrigger

```typescript
// trigger: SSHSessionStartTrigger
const SSHSessionStartTriggerContract: TriggerContract = {
  triggerId: 'SSHSessionStartTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SSHSessionStartTrigger' },
  actionTarget: 'ConfigureSSHAuditingTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessSshAuditingWriteProtocol.md) · [Tasks](../tasks/AccessSshAuditingWriteTask.md) · [Workflow](../workflows/AccessSshAuditingWriteWorkflow.md)
