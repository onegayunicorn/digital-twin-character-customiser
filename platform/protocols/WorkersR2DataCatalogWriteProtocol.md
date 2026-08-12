# Protocol: WorkersR2DataCatalogWriteProtocol

> Capability #19 — **Workers R2 Data Catalog Write** · Domain: Storage & Data · Access: `write`

## Purpose
Dataset metadata, schema registry, and partition information for the R2 catalog.

## Interface contract
```typescript
// protocol: WorkersR2DataCatalogWriteProtocol
interface WorkersR2DataCatalogWriteProtocol extends BaseOperation {
  id: string;
  name: 'Workers R2 Data Catalog Write';
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
| Trigger(s) | [`CatalogEntryUpdatedTrigger`](../triggers/WorkersR2DataCatalogWriteTrigger.md) |
| Task(s) | [`UpdateR2DataCatalogTask`](../tasks/WorkersR2DataCatalogWriteTask.md) |
| Workflow | [`WorkersR2DataCatalogWriteWorkflow`](../workflows/WorkersR2DataCatalogWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register schema -> Index -> Tag -> Publish
