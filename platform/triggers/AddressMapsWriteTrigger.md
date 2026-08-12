# Trigger: AddressMapsWriteTrigger

> Capability #84 — **Address Maps Write**

Event source(s) that initiate execution for this capability.

### Trigger: AddressMapUpdatedTrigger

```typescript
// trigger: AddressMapUpdatedTrigger
const AddressMapUpdatedTriggerContract: TriggerContract = {
  triggerId: 'AddressMapUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AddressMapUpdatedTrigger' },
  actionTarget: 'ManageAddressMapTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AddressMapsWriteProtocol.md) · [Tasks](../tasks/AddressMapsWriteTask.md) · [Workflow](../workflows/AddressMapsWriteWorkflow.md)
