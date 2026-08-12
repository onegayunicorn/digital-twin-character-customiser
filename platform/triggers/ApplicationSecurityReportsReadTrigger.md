# Trigger: ApplicationSecurityReportsReadTrigger

> Capability #40 — **Application Security Reports Read**

Event source(s) that initiate execution for this capability.

### Trigger: ReportGeneratedTrigger

```typescript
// trigger: ReportGeneratedTrigger
const ReportGeneratedTriggerContract: TriggerContract = {
  triggerId: 'ReportGeneratedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ReportGeneratedTrigger' },
  actionTarget: 'GenerateAppSecReportTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ScheduleReportTrigger

```typescript
// trigger: ScheduleReportTrigger
const ScheduleReportTriggerContract: TriggerContract = {
  triggerId: 'ScheduleReportTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ScheduleReportTrigger' },
  actionTarget: 'GenerateAppSecReportTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ApplicationSecurityReportsReadProtocol.md) · [Tasks](../tasks/ApplicationSecurityReportsReadTask.md) · [Workflow](../workflows/ApplicationSecurityReportsReadWorkflow.md)
