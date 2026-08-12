# Trigger: FieldExtractorsWriteTrigger

> Capability #44 — **Field Extractors Write**

Event source(s) that initiate execution for this capability.

### Trigger: ExtractorConfigTrigger

```typescript
// trigger: ExtractorConfigTrigger
const ExtractorConfigTriggerContract: TriggerContract = {
  triggerId: 'ExtractorConfigTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ExtractorConfigTrigger' },
  actionTarget: 'CreateFieldExtractorTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/FieldExtractorsWriteProtocol.md) · [Tasks](../tasks/FieldExtractorsWriteTask.md) · [Workflow](../workflows/FieldExtractorsWriteWorkflow.md)
