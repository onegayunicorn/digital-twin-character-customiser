# Protocol: AccountSecurityCenterInsightsWriteProtocol

> Capability #37 — **Account Security Center Insights Write** · Domain: Security & Edge · Access: `write`

## Purpose
Findings, risks, recommendations, and reports for Security Center.

## Interface contract
```typescript
// protocol: AccountSecurityCenterInsightsWriteProtocol
interface AccountSecurityCenterInsightsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Account Security Center Insights Write';
  accessLevel: 'write';
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
| Trigger(s) | [`SecurityScanCompleteTrigger`](../triggers/AccountSecurityCenterInsightsWriteTrigger.md), [`InsightGeneratedTrigger`](../triggers/AccountSecurityCenterInsightsWriteTrigger.md) |
| Task(s) | [`UpdateSecurityInsightTask`](../tasks/AccountSecurityCenterInsightsWriteTask.md) |
| Workflow | [`AccountSecurityCenterInsightsWriteWorkflow`](../workflows/AccountSecurityCenterInsightsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Scan -> Analyze -> Generate insight -> Prioritize -> Notify
