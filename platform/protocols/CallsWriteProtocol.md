# Protocol: CallsWriteProtocol

> Capability #79 — **Calls Write** · Domain: Media & Streaming · Access: `write`

## Purpose
WebRTC rooms, participants, recording, and quality for Calls.

## Interface contract
```typescript
// protocol: CallsWriteProtocol
interface CallsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Calls Write';
  accessLevel: 'write';
  category: 'Media & Streaming';
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
| Trigger(s) | [`CallInitiatedTrigger`](../triggers/CallsWriteTrigger.md), [`ParticipantJoinTrigger`](../triggers/CallsWriteTrigger.md) |
| Task(s) | [`ManageCallSessionTask`](../tasks/CallsWriteTask.md) |
| Workflow | [`CallsWriteWorkflow`](../workflows/CallsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create room -> Join -> Negotiate media -> Stream -> Record -> End
