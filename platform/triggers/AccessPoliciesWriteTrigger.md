# Trigger: AccessPoliciesWriteTrigger

> Capability #110 — **Access: Policies Write**

Event source(s) that initiate execution for this capability.

### Trigger: AccessPolicyTrigger

```typescript
// trigger: AccessPolicyTrigger
const AccessPolicyTriggerContract: TriggerContract = {
  triggerId: 'AccessPolicyTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AccessPolicyTrigger' },
  actionTarget: 'CreateAccessPolicyTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessPoliciesWriteProtocol.md) · [Tasks](../tasks/AccessPoliciesWriteTask.md) · [Workflow](../workflows/AccessPoliciesWriteWorkflow.md)
