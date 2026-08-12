# Protocol: WorkersCiWriteProtocol

> Capability #10 — **Workers CI Write** · Domain: Workers, Compute & Code · Access: `write`

## Purpose
Build pipelines, test runners, and deploy gates for continuous integration.

## Interface contract
```typescript
// protocol: WorkersCiWriteProtocol
interface WorkersCiWriteProtocol extends BaseOperation {
  id: string;
  name: 'Workers CI Write';
  accessLevel: 'write';
  category: 'Workers, Compute & Code';
  serviceDomain: string;
  enabled: boolean;
  auditLogging: boolean;
  rateLimit?: RateLimit;
  // capability-specific contract fields
}
```

## Related artifacts
| Type | File |
|---|---|
| Trigger(s) | [`CommitPushedTrigger`](../triggers/WorkersCiWriteTrigger.md), [`PullRequestTrigger`](../triggers/WorkersCiWriteTrigger.md), [`ScheduleTrigger`](../triggers/WorkersCiWriteTrigger.md) |
| Task(s) | [`RunWorkersCITask`](../tasks/WorkersCiWriteTask.md) |
| Workflow | [`WorkersCiWriteWorkflow`](../workflows/WorkersCiWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Lint -> Test -> Build -> Scan -> Deploy
