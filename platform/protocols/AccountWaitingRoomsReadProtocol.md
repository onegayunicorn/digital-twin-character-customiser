# Protocol: AccountWaitingRoomsReadProtocol

> Capability #85 — **Account Waiting Rooms Read** · Domain: Load Balancing & Traffic · Access: `read`

## Purpose
Queue stats, active users, wait time, and history for waiting rooms.

## Interface contract
```typescript
// protocol: AccountWaitingRoomsReadProtocol
interface AccountWaitingRoomsReadProtocol extends BaseOperation {
  id: string;
  name: 'Account Waiting Rooms Read';
  accessLevel: 'read';
  category: 'Load Balancing & Traffic';
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
| Trigger(s) | [`WaitingRoomEventTrigger`](../triggers/AccountWaitingRoomsReadTrigger.md) |
| Task(s) | [`ReadWaitingRoomMetricsTask`](../tasks/AccountWaitingRoomsReadTask.md) |
| Workflow | [`AccountWaitingRoomsReadWorkflow`](../workflows/AccountWaitingRoomsReadWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Poll -> Calculate -> Report -> Alert
