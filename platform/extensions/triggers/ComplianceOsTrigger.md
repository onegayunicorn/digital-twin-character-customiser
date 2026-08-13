# Trigger: ComplianceOsTrigger

> Capability #156 — **Compliance OS**

Event source(s) that initiate execution for this capability.

### Trigger: FeatureEnableRequestTrigger

```typescript
// trigger: FeatureEnableRequestTrigger
const FeatureEnableRequestTriggerContract: TriggerContract = {
  triggerId: 'FeatureEnableRequestTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for FeatureEnableRequestTrigger' },
  actionTarget: 'RunGateChainTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ComplianceOsProtocol.md) · [Tasks](../tasks/ComplianceOsTask.md) · [Workflow](../workflows/ComplianceOsWorkflow.md)
