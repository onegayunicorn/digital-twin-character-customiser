# Trigger: AiSearchWriteTrigger

> Capability #4 — **AI Search Write**

Event source(s) that initiate execution for this capability.

### Trigger: DocumentIngestedTrigger

```typescript
// trigger: DocumentIngestedTrigger
const DocumentIngestedTriggerContract: TriggerContract = {
  triggerId: 'DocumentIngestedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for DocumentIngestedTrigger' },
  actionTarget: 'ManageAISearchIndexTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: IndexUpdatedTrigger

```typescript
// trigger: IndexUpdatedTrigger
const IndexUpdatedTriggerContract: TriggerContract = {
  triggerId: 'IndexUpdatedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for IndexUpdatedTrigger' },
  actionTarget: 'ManageAISearchIndexTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AiSearchWriteProtocol.md) · [Tasks](../tasks/AiSearchWriteTask.md) · [Workflow](../workflows/AiSearchWriteWorkflow.md)
