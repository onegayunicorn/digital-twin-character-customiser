# Protocol: AccountAnalyticsReadProtocol

> Capability #98 — **Account Analytics Read** · Domain: Access & Zero Trust · Access: `read`

## Purpose
Usage, traffic, performance, errors, and reports for account analytics.

## Interface contract
```typescript
// protocol: AccountAnalyticsReadProtocol
interface AccountAnalyticsReadProtocol extends BaseOperation {
  id: string;
  name: 'Account Analytics Read';
  accessLevel: 'read';
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
| Trigger(s) | [`AnalyticsReportTrigger`](../triggers/AccountAnalyticsReadTrigger.md), [`ScheduleTrigger`](../triggers/AccountAnalyticsReadTrigger.md) |
| Task(s) | [`QueryAnalyticsTask`](../tasks/AccountAnalyticsReadTask.md) |
| Workflow | [`AccountAnalyticsReadWorkflow`](../workflows/AccountAnalyticsReadWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Select metrics -> Query -> Aggregate -> Generate -> Distribute
