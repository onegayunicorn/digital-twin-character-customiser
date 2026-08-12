# Trigger: FraudFeedbackWriteTrigger

> Capability #46 — **Fraud Feedback Write**

Event source(s) that initiate execution for this capability.

### Trigger: FraudFeedbackSubmittedTrigger

```typescript
// trigger: FraudFeedbackSubmittedTrigger
const FraudFeedbackSubmittedTriggerContract: TriggerContract = {
  triggerId: 'FraudFeedbackSubmittedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for FraudFeedbackSubmittedTrigger' },
  actionTarget: 'SubmitFraudFeedbackTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/FraudFeedbackWriteProtocol.md) · [Tasks](../tasks/FraudFeedbackWriteTask.md) · [Workflow](../workflows/FraudFeedbackWriteWorkflow.md)
