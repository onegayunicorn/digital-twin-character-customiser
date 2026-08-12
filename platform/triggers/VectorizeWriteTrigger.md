# Trigger: VectorizeWriteTrigger

> Capability #20 — **Vectorize Write**

Event source(s) that initiate execution for this capability.

### Trigger: VectorBatchTrigger

```typescript
// trigger: VectorBatchTrigger
const VectorBatchTriggerContract: TriggerContract = {
  triggerId: 'VectorBatchTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for VectorBatchTrigger' },
  actionTarget: 'IngestVectorsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: EmbeddingGeneratedTrigger

```typescript
// trigger: EmbeddingGeneratedTrigger
const EmbeddingGeneratedTriggerContract: TriggerContract = {
  triggerId: 'EmbeddingGeneratedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for EmbeddingGeneratedTrigger' },
  actionTarget: 'IngestVectorsTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/VectorizeWriteProtocol.md) · [Tasks](../tasks/VectorizeWriteTask.md) · [Workflow](../workflows/VectorizeWriteWorkflow.md)
