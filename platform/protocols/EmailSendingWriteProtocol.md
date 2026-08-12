# Protocol: EmailSendingWriteProtocol

> Capability #78 — **Email Sending Write** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
DKIM/SPF/DMARC, templates, batch, limits, and tracking for email sending.

## Interface contract
```typescript
// protocol: EmailSendingWriteProtocol
interface EmailSendingWriteProtocol extends BaseOperation {
  id: string;
  name: 'Email Sending Write';
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
| Trigger(s) | [`EmailSendTrigger`](../triggers/EmailSendingWriteTrigger.md), [`DeliveryEventTrigger`](../triggers/EmailSendingWriteTrigger.md) |
| Task(s) | [`SendEmailTask`](../tasks/EmailSendingWriteTask.md), [`ConfigureEmailSenderTask`](../tasks/EmailSendingWriteTask.md) |
| Workflow | [`EmailSendingWriteWorkflow`](../workflows/EmailSendingWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Compose -> Validate -> Queue -> Send -> Track -> Retry
