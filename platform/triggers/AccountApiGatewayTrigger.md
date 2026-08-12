# Trigger: AccountApiGatewayTrigger

> Capability #63 — **Account API Gateway**

Event source(s) that initiate execution for this capability.

### Trigger: APIRequestTrigger

```typescript
// trigger: APIRequestTrigger
const APIRequestTriggerContract: TriggerContract = {
  triggerId: 'APIRequestTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for APIRequestTrigger' },
  actionTarget: 'ConfigureAPIGatewayTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: GatewayConfigTrigger

```typescript
// trigger: GatewayConfigTrigger
const GatewayConfigTriggerContract: TriggerContract = {
  triggerId: 'GatewayConfigTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for GatewayConfigTrigger' },
  actionTarget: 'ConfigureAPIGatewayTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountApiGatewayProtocol.md) · [Tasks](../tasks/AccountApiGatewayTask.md) · [Workflow](../workflows/AccountApiGatewayWorkflow.md)
