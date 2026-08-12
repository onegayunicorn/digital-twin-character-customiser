# Protocol: ZeroTrustSeatsWriteProtocol

> Capability #130 — **Zero Trust: Seats Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
License assignment, user count, billing, and enable/disable for seats.

## Interface contract
```typescript
// protocol: ZeroTrustSeatsWriteProtocol
interface ZeroTrustSeatsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Zero Trust: Seats Write';
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
| Trigger(s) | [`SeatAssignmentTrigger`](../triggers/ZeroTrustSeatsWriteTrigger.md) |
| Task(s) | [`ManageZeroTrustSeatTask`](../tasks/ZeroTrustSeatsWriteTask.md) |
| Workflow | [`ZeroTrustSeatsWriteWorkflow`](../workflows/ZeroTrustSeatsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Assign -> Enable -> Sync -> Reclaim -> Report
