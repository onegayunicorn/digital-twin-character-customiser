# Trigger: EmailRoutingAccountRulesReadTrigger

> Capability #75 — **Email Routing Account Rules Read**

Event source(s) that initiate execution for this capability.

### Trigger: EmailRoutingConfigTrigger

```typescript
// trigger: EmailRoutingConfigTrigger
const EmailRoutingConfigTriggerContract: TriggerContract = {
  triggerId: 'EmailRoutingConfigTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for EmailRoutingConfigTrigger' },
  actionTarget: 'ReadEmailRoutingRuleTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/EmailRoutingAccountRulesReadProtocol.md) · [Tasks](../tasks/EmailRoutingAccountRulesReadTask.md) · [Workflow](../workflows/EmailRoutingAccountRulesReadWorkflow.md)
