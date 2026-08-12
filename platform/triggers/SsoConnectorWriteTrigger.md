# Trigger: SsoConnectorWriteTrigger

> Capability #72 — **SSO Connector Write**

Event source(s) that initiate execution for this capability.

### Trigger: SSOConfigUpdatedTrigger

```typescript
// trigger: SSOConfigUpdatedTrigger
const SSOConfigUpdatedTriggerContract: TriggerContract = {
  triggerId: 'SSOConfigUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SSOConfigUpdatedTrigger' },
  actionTarget: 'ConfigureSSOConnectorTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/SsoConnectorWriteProtocol.md) · [Tasks](../tasks/SsoConnectorWriteTask.md) · [Workflow](../workflows/SsoConnectorWriteWorkflow.md)
