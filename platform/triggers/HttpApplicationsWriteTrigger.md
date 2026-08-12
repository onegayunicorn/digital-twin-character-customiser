# Trigger: HttpApplicationsWriteTrigger

> Capability #47 — **HTTP Applications Write**

Event source(s) that initiate execution for this capability.

### Trigger: HTTPAppConfigTrigger

```typescript
// trigger: HTTPAppConfigTrigger
const HTTPAppConfigTriggerContract: TriggerContract = {
  triggerId: 'HTTPAppConfigTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for HTTPAppConfigTrigger' },
  actionTarget: 'ManageHTTPApplicationTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/HttpApplicationsWriteProtocol.md) · [Tasks](../tasks/HttpApplicationsWriteTask.md) · [Workflow](../workflows/HttpApplicationsWriteWorkflow.md)
