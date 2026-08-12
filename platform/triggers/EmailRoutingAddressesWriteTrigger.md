# Trigger: EmailRoutingAddressesWriteTrigger

> Capability #76 — **Email Routing Addresses Write**

Event source(s) that initiate execution for this capability.

### Trigger: EmailAddressCreatedTrigger

```typescript
// trigger: EmailAddressCreatedTrigger
const EmailAddressCreatedTriggerContract: TriggerContract = {
  triggerId: 'EmailAddressCreatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for EmailAddressCreatedTrigger' },
  actionTarget: 'ManageEmailRoutingAddressTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/EmailRoutingAddressesWriteProtocol.md) · [Tasks](../tasks/EmailRoutingAddressesWriteTask.md) · [Workflow](../workflows/EmailRoutingAddressesWriteWorkflow.md)
