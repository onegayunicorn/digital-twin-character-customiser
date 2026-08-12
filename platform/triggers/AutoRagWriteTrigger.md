# Trigger: AutoRagWriteTrigger

> Capability #5 — **Auto Rag Write**

Event source(s) that initiate execution for this capability.

### Trigger: NewDataSourceDetectedTrigger

```typescript
// trigger: NewDataSourceDetectedTrigger
const NewDataSourceDetectedTriggerContract: TriggerContract = {
  triggerId: 'NewDataSourceDetectedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for NewDataSourceDetectedTrigger' },
  actionTarget: 'ConfigureAutoRAGTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ScheduleRAGUpdateTrigger

```typescript
// trigger: ScheduleRAGUpdateTrigger
const ScheduleRAGUpdateTriggerContract: TriggerContract = {
  triggerId: 'ScheduleRAGUpdateTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ScheduleRAGUpdateTrigger' },
  actionTarget: 'ConfigureAutoRAGTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AutoRagWriteProtocol.md) · [Tasks](../tasks/AutoRagWriteTask.md) · [Workflow](../workflows/AutoRagWriteWorkflow.md)
