# Trigger: DlsWriteTrigger

> Capability #126 — **DLS: Write**

Event source(s) that initiate execution for this capability.

### Trigger: DLPRuleUpdatedTrigger

```typescript
// trigger: DLPRuleUpdatedTrigger
const DLPRuleUpdatedTriggerContract: TriggerContract = {
  triggerId: 'DLPRuleUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DLPRuleUpdatedTrigger' },
  actionTarget: 'ConfigureDLSPolicyTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: SensitiveDataDetectedTrigger

```typescript
// trigger: SensitiveDataDetectedTrigger
const SensitiveDataDetectedTriggerContract: TriggerContract = {
  triggerId: 'SensitiveDataDetectedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SensitiveDataDetectedTrigger' },
  actionTarget: 'ConfigureDLSPolicyTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/DlsWriteProtocol.md) · [Tasks](../tasks/DlsWriteTask.md) · [Workflow](../workflows/DlsWriteWorkflow.md)
