# Trigger: AccountDnsSettingsWriteTrigger

> Capability #30 — **Account DNS Settings Write**

Event source(s) that initiate execution for this capability.

### Trigger: DNSConfigChangeTrigger

```typescript
// trigger: DNSConfigChangeTrigger
const DNSConfigChangeTriggerContract: TriggerContract = {
  triggerId: 'DNSConfigChangeTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DNSConfigChangeTrigger' },
  actionTarget: 'UpdateDNSSettingTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountDnsSettingsWriteProtocol.md) · [Tasks](../tasks/AccountDnsSettingsWriteTask.md) · [Workflow](../workflows/AccountDnsSettingsWriteWorkflow.md)
