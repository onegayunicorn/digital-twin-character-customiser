# Protocol: AccountSettingsWriteProtocol

> Capability #66 — **Account Settings Write** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
Account-level defaults, preferences, and feature toggles.

## Interface contract
```typescript
// protocol: AccountSettingsWriteProtocol
interface AccountSettingsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Account Settings Write';
  accessLevel: 'write';
  category: 'Account, Auth, Email & Billing';
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
| Trigger(s) | [`AccountSettingsUpdatedTrigger`](../triggers/AccountSettingsWriteTrigger.md) |
| Task(s) | [`UpdateAccountSettingTask`](../tasks/AccountSettingsWriteTask.md) |
| Workflow | [`AccountSettingsWriteWorkflow`](../workflows/AccountSettingsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Modify -> Validate -> Apply -> Sync -> Audit
