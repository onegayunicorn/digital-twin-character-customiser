# Protocol: AccessUsersWriteProtocol

> Capability #118 — **Access: Users Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
User records, profile, status, MFA, and devices.

## Interface contract
```typescript
// protocol: AccessUsersWriteProtocol
interface AccessUsersWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: Users Write';
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
| Trigger(s) | [`UserCreatedTrigger`](../triggers/AccessUsersWriteTrigger.md), [`UserLoginTrigger`](../triggers/AccessUsersWriteTrigger.md) |
| Task(s) | [`ManageAccessUserTask`](../tasks/AccessUsersWriteTask.md) |
| Workflow | [`AccessUsersWriteWorkflow`](../workflows/AccessUsersWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create -> Invite -> Enroll MFA -> Provision -> Deprovision
