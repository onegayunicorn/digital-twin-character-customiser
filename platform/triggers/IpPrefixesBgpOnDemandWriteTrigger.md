# Trigger: IpPrefixesBgpOnDemandWriteTrigger

> Capability #89 — **IP Prefixes: BGP On Demand Write**

Event source(s) that initiate execution for this capability.

### Trigger: BGPTriggerEventTrigger

```typescript
// trigger: BGPTriggerEventTrigger
const BGPTriggerEventTriggerContract: TriggerContract = {
  triggerId: 'BGPTriggerEventTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for BGPTriggerEventTrigger' },
  actionTarget: 'ControlBGPAnnouncementTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/IpPrefixesBgpOnDemandWriteProtocol.md) · [Tasks](../tasks/IpPrefixesBgpOnDemandWriteTask.md) · [Workflow](../workflows/IpPrefixesBgpOnDemandWriteWorkflow.md)
