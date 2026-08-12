# Protocol: ApplicationSecurityReportsReadProtocol

> Capability #40 — **Application Security Reports Read** · Domain: Security & Edge · Access: `read`

## Purpose
Vulnerabilities, attack stats, and endpoint risk reporting.

## Interface contract
```typescript
// protocol: ApplicationSecurityReportsReadProtocol
interface ApplicationSecurityReportsReadProtocol extends BaseOperation {
  id: string;
  name: 'Application Security Reports Read';
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
| Trigger(s) | [`ReportGeneratedTrigger`](../triggers/ApplicationSecurityReportsReadTrigger.md), [`ScheduleReportTrigger`](../triggers/ApplicationSecurityReportsReadTrigger.md) |
| Task(s) | [`GenerateAppSecReportTask`](../tasks/ApplicationSecurityReportsReadTask.md) |
| Workflow | [`ApplicationSecurityReportsReadWorkflow`](../workflows/ApplicationSecurityReportsReadWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Collect data -> Analyze -> Generate -> Distribute -> Archive
