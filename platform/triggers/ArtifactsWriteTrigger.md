# Trigger: ArtifactsWriteTrigger

> Capability #62 — **Artifacts Write**

Event source(s) that initiate execution for this capability.

### Trigger: ArtifactUploadedTrigger

```typescript
// trigger: ArtifactUploadedTrigger
const ArtifactUploadedTriggerContract: TriggerContract = {
  triggerId: 'ArtifactUploadedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ArtifactUploadedTrigger' },
  actionTarget: 'UploadArtifactTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/ArtifactsWriteProtocol.md) · [Tasks](../tasks/ArtifactsWriteTask.md) · [Workflow](../workflows/ArtifactsWriteWorkflow.md)
