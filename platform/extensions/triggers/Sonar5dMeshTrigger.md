# Trigger: Sonar5dMeshTrigger

> Capability #141 — **Sonar 5D Mesh**

Event source(s) that initiate execution for this capability.

### Trigger: MeshRequestedTrigger

```typescript
// trigger: MeshRequestedTrigger
const MeshRequestedTriggerContract: TriggerContract = {
  triggerId: 'MeshRequestedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MeshRequestedTrigger' },
  actionTarget: 'GenerateMeshTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: SweepTrigger

```typescript
// trigger: SweepTrigger
const SweepTriggerContract: TriggerContract = {
  triggerId: 'SweepTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SweepTrigger' },
  actionTarget: 'GenerateMeshTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/Sonar5dMeshProtocol.md) · [Tasks](../tasks/Sonar5dMeshTask.md) · [Workflow](../workflows/Sonar5dMeshWorkflow.md)
