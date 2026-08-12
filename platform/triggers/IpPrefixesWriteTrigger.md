# Trigger: IpPrefixesWriteTrigger

> Capability #88 — **IP Prefixes: Write**

Event source(s) that initiate execution for this capability.

### Trigger: PrefixAnnouncementTrigger

```typescript
// trigger: PrefixAnnouncementTrigger
const PrefixAnnouncementTriggerContract: TriggerContract = {
  triggerId: 'PrefixAnnouncementTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PrefixAnnouncementTrigger' },
  actionTarget: 'ManageIPPrefixTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/IpPrefixesWriteProtocol.md) · [Tasks](../tasks/IpPrefixesWriteTask.md) · [Workflow](../workflows/IpPrefixesWriteWorkflow.md)
