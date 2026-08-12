# Trigger: D1WriteTrigger

> Capability #15 — **D1 Write**

Event source(s) that initiate execution for this capability.

### Trigger: MigrationTrigger

```typescript
// trigger: MigrationTrigger
const MigrationTriggerContract: TriggerContract = {
  triggerId: 'MigrationTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MigrationTrigger' },
  actionTarget: 'ExecuteD1QueryTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: WriteQueryTrigger

```typescript
// trigger: WriteQueryTrigger
const WriteQueryTriggerContract: TriggerContract = {
  triggerId: 'WriteQueryTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for WriteQueryTrigger' },
  actionTarget: 'ExecuteD1QueryTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/D1WriteProtocol.md) · [Tasks](../tasks/D1WriteTask.md) · [Workflow](../workflows/D1WriteWorkflow.md)
