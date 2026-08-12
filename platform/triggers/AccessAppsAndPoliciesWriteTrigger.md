# Trigger: AccessAppsAndPoliciesWriteTrigger

> Capability #99 — **Access: Apps and Policies Write**

Event source(s) that initiate execution for this capability.

### Trigger: AccessPolicyUpdatedTrigger

```typescript
// trigger: AccessPolicyUpdatedTrigger
const AccessPolicyUpdatedTriggerContract: TriggerContract = {
  triggerId: 'AccessPolicyUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AccessPolicyUpdatedTrigger' },
  actionTarget: 'ManageAccessAppAndPolicyTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessAppsAndPoliciesWriteProtocol.md) · [Tasks](../tasks/AccessAppsAndPoliciesWriteTask.md) · [Workflow](../workflows/AccessAppsAndPoliciesWriteWorkflow.md)
