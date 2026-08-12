# Protocol: CloudEmailSecurityWriteProtocol

> Capability #74 — **Cloud Email Security: Write** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
Anti-spam, DLP, phishing, and attachment scanning for email security.

## Interface contract
```typescript
// protocol: CloudEmailSecurityWriteProtocol
interface CloudEmailSecurityWriteProtocol extends BaseOperation {
  id: string;
  name: 'Cloud Email Security: Write';
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
| Trigger(s) | [`EmailReceivedTrigger`](../triggers/CloudEmailSecurityWriteTrigger.md), [`SecurityAlertTrigger`](../triggers/CloudEmailSecurityWriteTrigger.md) |
| Task(s) | [`ConfigureEmailSecurityPolicyTask`](../tasks/CloudEmailSecurityWriteTask.md) |
| Workflow | [`CloudEmailSecurityWriteWorkflow`](../workflows/CloudEmailSecurityWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Scan -> Classify -> Filter -> Quarantine -> Notify
