# Protocol: AccessSshAuditingWriteProtocol

> Capability #116 — **Access: SSH Auditing Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Session logs, commands, file transfers, and keylogging for SSH auditing.

## Interface contract
```typescript
// protocol: AccessSshAuditingWriteProtocol
interface AccessSshAuditingWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: SSH Auditing Write';
  accessLevel: 'write';
  category: 'Access & Zero Trust';
  serviceDomain: string;
  enabled: boolean;
  auditLogging: boolean;
  rateLimit?: RateLimit;
  // capability-specific contract fields
}
```

## Related artifacts
| Type | File |
|---|---|
| Trigger(s) | [`SSHSessionStartTrigger`](../triggers/AccessSshAuditingWriteTrigger.md) |
| Task(s) | [`ConfigureSSHAuditingTask`](../tasks/AccessSshAuditingWriteTask.md) |
| Workflow | [`AccessSshAuditingWriteWorkflow`](../workflows/AccessSshAuditingWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Enable -> Capture -> Store -> Review -> Archive
