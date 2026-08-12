# Trigger: MagicFirewallWriteTrigger

> Capability #90 — **Magic Firewall Write**

Event source(s) that initiate execution for this capability.

### Trigger: MagicFirewallRuleChangeTrigger

```typescript
// trigger: MagicFirewallRuleChangeTrigger
const MagicFirewallRuleChangeTriggerContract: TriggerContract = {
  triggerId: 'MagicFirewallRuleChangeTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MagicFirewallRuleChangeTrigger' },
  actionTarget: 'ConfigureMagicFirewallTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/MagicFirewallWriteProtocol.md) · [Tasks](../tasks/MagicFirewallWriteTask.md) · [Workflow](../workflows/MagicFirewallWriteWorkflow.md)
