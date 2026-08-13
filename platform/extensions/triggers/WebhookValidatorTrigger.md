# Trigger: WebhookValidatorTrigger

> Capability #166 — **Webhook Validator**

Event source(s) that initiate execution for this capability.

### Trigger: WebhookReceivedTrigger

```typescript
// trigger: WebhookReceivedTrigger
const WebhookReceivedTriggerContract: TriggerContract = {
  triggerId: 'WebhookReceivedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for WebhookReceivedTrigger' },
  actionTarget: 'ValidateSignatureTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WebhookValidatorProtocol.md) · [Tasks](../tasks/WebhookValidatorTask.md) · [Workflow](../workflows/WebhookValidatorWorkflow.md)
