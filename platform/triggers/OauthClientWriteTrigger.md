# Trigger: OauthClientWriteTrigger

> Capability #70 — **OAuth Client Write**

Event source(s) that initiate execution for this capability.

### Trigger: OAuthClientCreatedTrigger

```typescript
// trigger: OAuthClientCreatedTrigger
const OAuthClientCreatedTriggerContract: TriggerContract = {
  triggerId: 'OAuthClientCreatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for OAuthClientCreatedTrigger' },
  actionTarget: 'RegisterOAuthClientTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/OauthClientWriteProtocol.md) · [Tasks](../tasks/OauthClientWriteTask.md) · [Workflow](../workflows/OauthClientWriteWorkflow.md)
