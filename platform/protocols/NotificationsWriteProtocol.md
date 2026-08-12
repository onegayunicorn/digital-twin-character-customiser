# Protocol: NotificationsWriteProtocol

> Capability #69 — **Notifications Write** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
Channels, recipients, templates, triggers, and frequency for notifications.

## Interface contract
```typescript
// protocol: NotificationsWriteProtocol
interface NotificationsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Notifications Write';
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
| Trigger(s) | [`NotificationEventTrigger`](../triggers/NotificationsWriteTrigger.md) |
| Task(s) | [`ConfigureNotificationTask`](../tasks/NotificationsWriteTask.md) |
| Workflow | [`NotificationsWriteWorkflow`](../workflows/NotificationsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define channel -> Set rules -> Template -> Test -> Activate
