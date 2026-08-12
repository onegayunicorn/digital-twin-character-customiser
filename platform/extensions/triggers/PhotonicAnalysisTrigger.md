# Trigger: PhotonicAnalysisTrigger

> Capability #136 — **Photonic Analysis**

Event source(s) that initiate execution for this capability.

### Trigger: MeasurementIngestedTrigger

```typescript
// trigger: MeasurementIngestedTrigger
const MeasurementIngestedTriggerContract: TriggerContract = {
  triggerId: 'MeasurementIngestedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MeasurementIngestedTrigger' },
  actionTarget: 'AnalyzeClassicalTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/PhotonicAnalysisProtocol.md) · [Tasks](../tasks/PhotonicAnalysisTask.md) · [Workflow](../workflows/PhotonicAnalysisWorkflow.md)
