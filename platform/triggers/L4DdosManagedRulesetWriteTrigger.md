# Trigger: L4DdosManagedRulesetWriteTrigger

> Capability #49 — **L4 DDoS Managed Ruleset Write**

Event source(s) that initiate execution for this capability.

### Trigger: L4DDoSRulesetUpdatedTrigger

```typescript
// trigger: L4DDoSRulesetUpdatedTrigger
const L4DDoSRulesetUpdatedTriggerContract: TriggerContract = {
  triggerId: 'L4DDoSRulesetUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for L4DDoSRulesetUpdatedTrigger' },
  actionTarget: 'DeployL4DDoSRulesetTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/L4DdosManagedRulesetWriteProtocol.md) · [Tasks](../tasks/L4DdosManagedRulesetWriteTask.md) · [Workflow](../workflows/L4DdosManagedRulesetWriteWorkflow.md)
