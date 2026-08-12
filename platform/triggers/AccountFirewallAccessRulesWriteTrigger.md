# Trigger: AccountFirewallAccessRulesWriteTrigger

> Capability #36 — **Account Firewall Access Rules Write**

Event source(s) that initiate execution for this capability.

### Trigger: FirewallRuleChangeTrigger

```typescript
// trigger: FirewallRuleChangeTrigger
const FirewallRuleChangeTriggerContract: TriggerContract = {
  triggerId: 'FirewallRuleChangeTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for FirewallRuleChangeTrigger' },
  actionTarget: 'CreateFirewallRuleTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: AttackDetectedTrigger

```typescript
// trigger: AttackDetectedTrigger
const AttackDetectedTriggerContract: TriggerContract = {
  triggerId: 'AttackDetectedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for AttackDetectedTrigger' },
  actionTarget: 'CreateFirewallRuleTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountFirewallAccessRulesWriteProtocol.md) · [Tasks](../tasks/AccountFirewallAccessRulesWriteTask.md) · [Workflow](../workflows/AccountFirewallAccessRulesWriteWorkflow.md)
