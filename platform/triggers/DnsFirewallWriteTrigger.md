# Trigger: DnsFirewallWriteTrigger

> Capability #31 — **DNS Firewall Write**

Event source(s) that initiate execution for this capability.

### Trigger: DNSQueryTrigger

```typescript
// trigger: DNSQueryTrigger
const DNSQueryTriggerContract: TriggerContract = {
  triggerId: 'DNSQueryTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DNSQueryTrigger' },
  actionTarget: 'ManageDNSFirewallRuleTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: DNSFirewallRuleChangeTrigger

```typescript
// trigger: DNSFirewallRuleChangeTrigger
const DNSFirewallRuleChangeTriggerContract: TriggerContract = {
  triggerId: 'DNSFirewallRuleChangeTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DNSFirewallRuleChangeTrigger' },
  actionTarget: 'ManageDNSFirewallRuleTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/DnsFirewallWriteProtocol.md) · [Tasks](../tasks/DnsFirewallWriteTask.md) · [Workflow](../workflows/DnsFirewallWriteWorkflow.md)
