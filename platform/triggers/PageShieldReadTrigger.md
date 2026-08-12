# Trigger: PageShieldReadTrigger

> Capability #50 — **Page Shield Read**

Event source(s) that initiate execution for this capability.

### Trigger: ScriptIncludedTrigger

```typescript
// trigger: ScriptIncludedTrigger
const ScriptIncludedTriggerContract: TriggerContract = {
  triggerId: 'ScriptIncludedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ScriptIncludedTrigger' },
  actionTarget: 'ScanPageShieldTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: PageShieldAlertTrigger

```typescript
// trigger: PageShieldAlertTrigger
const PageShieldAlertTriggerContract: TriggerContract = {
  triggerId: 'PageShieldAlertTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PageShieldAlertTrigger' },
  actionTarget: 'ScanPageShieldTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/PageShieldReadProtocol.md) · [Tasks](../tasks/PageShieldReadTask.md) · [Workflow](../workflows/PageShieldReadWorkflow.md)
