# Protocol: OffgridSyncProtocol

> Capability #159 — **Off-grid Sync** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Offline transaction queue, store-and-forward, local ledger, eventual-consistency merge, disaster mode.

## Interface contract
```typescript
// protocol: OffgridSyncProtocol
interface OffgridSyncProtocol extends BaseOperation {
  id: string;
  name: 'Off-grid Sync';
  accessLevel: 'write';
  category: 'Access & Zero Trust';
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
| Trigger(s) | [`OfflineTransactionTrigger`](../triggers/OffgridSyncTrigger.md), [`SyncOpportunityTrigger`](../triggers/OffgridSyncTrigger.md) |
| Task(s) | [`EnqueueOfflineTask`](../tasks/OffgridSyncTask.md), [`MergeLedgerTask`](../tasks/OffgridSyncTask.md), [`EnterDisasterModeTask`](../tasks/OffgridSyncTask.md) |
| Workflow | [`OffgridSyncWorkflow`](../workflows/OffgridSyncWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Queue -> Sync -> Merge -> Reconcile -> Report
