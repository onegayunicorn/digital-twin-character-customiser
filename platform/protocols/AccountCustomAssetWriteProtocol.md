# Protocol: AccountCustomAssetWriteProtocol

> Capability #65 — **Account Custom Asset Write** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
Uploaded assets, hashes, cache control, and distribution for custom assets.

## Interface contract
```typescript
// protocol: AccountCustomAssetWriteProtocol
interface AccountCustomAssetWriteProtocol extends BaseOperation {
  id: string;
  name: 'Account Custom Asset Write';
  accessLevel: 'write';
  category: 'Account, Auth, Email & Billing';
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
| Trigger(s) | [`AssetUploadedTrigger`](../triggers/AccountCustomAssetWriteTrigger.md) |
| Task(s) | [`UploadCustomAssetTask`](../tasks/AccountCustomAssetWriteTask.md) |
| Workflow | [`AccountCustomAssetWriteWorkflow`](../workflows/AccountCustomAssetWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Upload -> Validate -> Hash -> Distribute -> Purge cache
