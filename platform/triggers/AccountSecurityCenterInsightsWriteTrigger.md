# Trigger: AccountSecurityCenterInsightsWriteTrigger

> Capability #37 — **Account Security Center Insights Write**

Event source(s) that initiate execution for this capability.

### Trigger: SecurityScanCompleteTrigger

```typescript
// trigger: SecurityScanCompleteTrigger
const SecurityScanCompleteTriggerContract: TriggerContract = {
  triggerId: 'SecurityScanCompleteTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SecurityScanCompleteTrigger' },
  actionTarget: 'UpdateSecurityInsightTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: InsightGeneratedTrigger

```typescript
// trigger: InsightGeneratedTrigger
const InsightGeneratedTriggerContract: TriggerContract = {
  triggerId: 'InsightGeneratedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for InsightGeneratedTrigger' },
  actionTarget: 'UpdateSecurityInsightTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountSecurityCenterInsightsWriteProtocol.md) · [Tasks](../tasks/AccountSecurityCenterInsightsWriteTask.md) · [Workflow](../workflows/AccountSecurityCenterInsightsWriteWorkflow.md)
