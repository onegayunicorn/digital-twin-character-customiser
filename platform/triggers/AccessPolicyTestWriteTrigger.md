# Trigger: AccessPolicyTestWriteTrigger

> Capability #111 — **Access: Policy Test Write**

Event source(s) that initiate execution for this capability.

### Trigger: PolicyTestRunTrigger

```typescript
// trigger: PolicyTestRunTrigger
const PolicyTestRunTriggerContract: TriggerContract = {
  triggerId: 'PolicyTestRunTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PolicyTestRunTrigger' },
  actionTarget: 'TestAccessPolicyTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessPolicyTestWriteProtocol.md) · [Tasks](../tasks/AccessPolicyTestWriteTask.md) · [Workflow](../workflows/AccessPolicyTestWriteWorkflow.md)
