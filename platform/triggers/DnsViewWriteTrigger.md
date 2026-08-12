# Trigger: DnsViewWriteTrigger

> Capability #32 — **DNS View Write**

Event source(s) that initiate execution for this capability.

### Trigger: DNSViewConfigTrigger

```typescript
// trigger: DNSViewConfigTrigger
const DNSViewConfigTriggerContract: TriggerContract = {
  triggerId: 'DNSViewConfigTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DNSViewConfigTrigger' },
  actionTarget: 'ConfigureDNSViewTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/DnsViewWriteProtocol.md) · [Tasks](../tasks/DnsViewWriteTask.md) · [Workflow](../workflows/DnsViewWriteWorkflow.md)
