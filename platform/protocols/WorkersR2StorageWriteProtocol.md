# Protocol: WorkersR2StorageWriteProtocol

> Capability #17 — **Workers R2 Storage Write** · Domain: Storage & Data · Access: `write`

## Purpose
Bucket, object, ACL, lifecycle, and multipart upload management for R2.

## Interface contract
```typescript
// protocol: WorkersR2StorageWriteProtocol
interface WorkersR2StorageWriteProtocol extends BaseOperation {
  id: string;
  name: 'Workers R2 Storage Write';
  accessLevel: 'write';
  category: 'Storage & Data';
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
| Trigger(s) | [`ObjectUploadedTrigger`](../triggers/WorkersR2StorageWriteTrigger.md), [`BucketConfigTrigger`](../triggers/WorkersR2StorageWriteTrigger.md) |
| Task(s) | [`UploadR2ObjectTask`](../tasks/WorkersR2StorageWriteTask.md), [`ManageR2BucketTask`](../tasks/WorkersR2StorageWriteTask.md) |
| Workflow | [`WorkersR2StorageWriteWorkflow`](../workflows/WorkersR2StorageWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Validate -> Upload -> Index -> Set lifecycle -> Purge cache
