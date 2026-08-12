# Protocol: AccountAbuseProtectionPiiReadProtocol

> Capability #35 — **Account Abuse Protection PII Read** · Domain: Security & Edge · Access: `read`

## Purpose
PII access scope, redaction, audit, and legal holds for abuse protection.

## Interface contract
```typescript
// protocol: AccountAbuseProtectionPiiReadProtocol
interface AccountAbuseProtectionPiiReadProtocol extends BaseOperation {
  id: string;
  name: 'Account Abuse Protection PII Read';
  accessLevel: 'read';
  category: 'Security & Edge';
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
| Trigger(s) | [`PIIAccessRequestTrigger`](../triggers/AccountAbuseProtectionPiiReadTrigger.md), [`AbuseReportTrigger`](../triggers/AccountAbuseProtectionPiiReadTrigger.md) |
| Task(s) | [`ReadAbusePIIRecordTask`](../tasks/AccountAbuseProtectionPiiReadTask.md) |
| Workflow | [`AccountAbuseProtectionPiiReadWorkflow`](../workflows/AccountAbuseProtectionPiiReadWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Request -> Auth -> Redact -> Review -> Action -> Log
