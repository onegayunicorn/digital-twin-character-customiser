# Trigger: WorkersCiWriteTrigger

> Capability #10 — **Workers CI Write**

Event source(s) that initiate execution for this capability.

### Trigger: CommitPushedTrigger

```typescript
// trigger: CommitPushedTrigger
const CommitPushedTriggerContract: TriggerContract = {
  triggerId: 'CommitPushedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for CommitPushedTrigger' },
  actionTarget: 'RunWorkersCITask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: PullRequestTrigger

```typescript
// trigger: PullRequestTrigger
const PullRequestTriggerContract: TriggerContract = {
  triggerId: 'PullRequestTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for PullRequestTrigger' },
  actionTarget: 'RunWorkersCITask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: ScheduleTrigger

```typescript
// trigger: ScheduleTrigger
const ScheduleTriggerContract: TriggerContract = {
  triggerId: 'ScheduleTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ScheduleTrigger' },
  actionTarget: 'RunWorkersCITask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/WorkersCiWriteProtocol.md) · [Tasks](../tasks/WorkersCiWriteTask.md) · [Workflow](../workflows/WorkersCiWriteWorkflow.md)
