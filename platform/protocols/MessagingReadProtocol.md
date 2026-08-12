# Protocol: MessagingReadProtocol

> Capability #21 — **Messaging Read** · Domain: Messaging, PubSub & Queues · Access: `read`

## Purpose
Topic consumption, offset management, filtering, and acknowledgement for messaging.

## Interface contract
```typescript
// protocol: MessagingReadProtocol
interface MessagingReadProtocol extends BaseOperation {
  id: string;
  name: 'Messaging Read';
  accessLevel: 'read';
  category: 'Messaging, PubSub & Queues';
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
| Trigger(s) | [`MessageAvailableTrigger`](../triggers/MessagingReadTrigger.md), [`MessageReceivedTrigger`](../triggers/MessagingReadTrigger.md) |
| Task(s) | [`ReadMessageTask`](../tasks/MessagingReadTask.md), [`PollMessagesTask`](../tasks/MessagingReadTask.md) |
| Workflow | [`MessagingReadWorkflow`](../workflows/MessagingReadWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Pull -> Validate -> Process -> Ack -> Commit offset
