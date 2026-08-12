# Protocol: WorkersScriptsWriteProtocol

> Capability #8 — **Workers Scripts Write** · Domain: Workers, Compute & Code · Access: `write`

## Purpose
Script upload, validation, bundling, and versioning for Workers.

## Interface contract
```typescript
// protocol: WorkersScriptsWriteProtocol
interface WorkersScriptsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Workers Scripts Write';
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
| Trigger(s) | [`ScriptUploadedTrigger`](../triggers/WorkersScriptsWriteTrigger.md), [`GitPushTrigger`](../triggers/WorkersScriptsWriteTrigger.md) |
| Task(s) | [`UploadUpdateWorkerScriptTask`](../tasks/WorkersScriptsWriteTask.md) |
| Workflow | [`WorkersScriptsWriteWorkflow`](../workflows/WorkersScriptsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Validate -> Build -> Upload -> Activate -> Test
