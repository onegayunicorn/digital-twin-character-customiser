# Protocol: DdosBotnetFeedWriteProtocol

> Capability #42 — **DDoS Botnet Feed Write** · Domain: Security & Edge · Access: `write`

## Purpose
IOCs, IP reputation, signatures, and update frequency for botnet feeds.

## Interface contract
```typescript
// protocol: DdosBotnetFeedWriteProtocol
interface DdosBotnetFeedWriteProtocol extends BaseOperation {
  id: string;
  name: 'DDoS Botnet Feed Write';
  accessLevel: 'write';
  category: 'Security & Edge';
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
| Trigger(s) | [`FeedUpdatedTrigger`](../triggers/DdosBotnetFeedWriteTrigger.md), [`ScheduleFeedSyncTrigger`](../triggers/DdosBotnetFeedWriteTrigger.md) |
| Task(s) | [`IngestBotnetFeedTask`](../tasks/DdosBotnetFeedWriteTask.md) |
| Workflow | [`DdosBotnetFeedWriteWorkflow`](../workflows/DdosBotnetFeedWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Fetch -> Validate -> Merge -> Deploy to edge -> Activate
