# Trigger: AccountAbuseProtectionPiiReadTrigger

> Capability #35 — **Account Abuse Protection PII Read**

Event source(s) that initiate execution for this capability.

### Trigger: PIIAccessRequestTrigger

```typescript
// trigger: PIIAccessRequestTrigger
const PIIAccessRequestTriggerContract: TriggerContract = {
  triggerId: 'PIIAccessRequestTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PIIAccessRequestTrigger' },
  actionTarget: 'ReadAbusePIIRecordTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: AbuseReportTrigger

```typescript
// trigger: AbuseReportTrigger
const AbuseReportTriggerContract: TriggerContract = {
  triggerId: 'AbuseReportTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AbuseReportTrigger' },
  actionTarget: 'ReadAbusePIIRecordTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountAbuseProtectionPiiReadProtocol.md) · [Tasks](../tasks/AccountAbuseProtectionPiiReadTask.md) · [Workflow](../workflows/AccountAbuseProtectionPiiReadWorkflow.md)
