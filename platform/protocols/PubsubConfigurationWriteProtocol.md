# Protocol: PubsubConfigurationWriteProtocol

> Capability #22 — **Pubsub Configuration Write** · Domain: Messaging, PubSub & Queues · Access: `write`

## Purpose
Topics, subscriptions, dead-letter, retries, and auth for Pub/Sub.

## Interface contract
```typescript
// protocol: PubsubConfigurationWriteProtocol
interface PubsubConfigurationWriteProtocol extends BaseOperation {
  id: string;
  name: 'Pubsub Configuration Write';
  accessLevel: 'write';
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
| Trigger(s) | [`PubsubConfigChangeTrigger`](../triggers/PubsubConfigurationWriteTrigger.md) |
| Task(s) | [`ConfigurePubsubTask`](../tasks/PubsubConfigurationWriteTask.md) |
| Workflow | [`PubsubConfigurationWriteWorkflow`](../workflows/PubsubConfigurationWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create topic -> Create sub -> Set DLQ -> Attach policy -> Deploy
