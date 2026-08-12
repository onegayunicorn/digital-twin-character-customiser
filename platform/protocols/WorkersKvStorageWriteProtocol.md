# Protocol: WorkersKvStorageWriteProtocol

> Capability #16 — **Workers KV Storage Write** · Domain: Storage & Data · Access: `write`

## Purpose
Key scope, TTL, atomic ops, bulk upload, and replication for Workers KV.

## Interface contract
```typescript
// protocol: WorkersKvStorageWriteProtocol
interface WorkersKvStorageWriteProtocol extends BaseOperation {
  id: string;
  name: 'Workers KV Storage Write';
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
| Trigger(s) | [`KVKeyWrittenTrigger`](../triggers/WorkersKvStorageWriteTrigger.md), [`KVExpiryTrigger`](../triggers/WorkersKvStorageWriteTrigger.md) |
| Task(s) | [`WriteKVEntryTask`](../tasks/WorkersKvStorageWriteTask.md), [`BulkWriteKVTask`](../tasks/WorkersKvStorageWriteTask.md) |
| Workflow | [`WorkersKvStorageWriteWorkflow`](../workflows/WorkersKvStorageWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Validate keys -> Batch -> Write -> Replicate -> Verify
