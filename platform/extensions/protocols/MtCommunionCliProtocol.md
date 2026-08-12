# Protocol: MtCommunionCliProtocol

> Capability #134 — **MT Communion CLI** · Domain: Access & Zero Trust · Access: `write`

## Purpose
IpAI MirrorTwin dialogue: intent -> sentiment valence -> 3-cell resonance routing -> reply -> engram persistence.

## Interface contract
```typescript
// protocol: MtCommunionCliProtocol
interface MtCommunionCliProtocol extends BaseOperation {
  id: string;
  name: 'MT Communion CLI';
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
| Trigger(s) | [`IntentReceivedTrigger`](../triggers/MtCommunionCliTrigger.md) |
| Task(s) | [`RouteIntentTask`](../tasks/MtCommunionCliTask.md), [`StoreEngramTask`](../tasks/MtCommunionCliTask.md) |
| Workflow | [`MtCommunionCliWorkflow`](../workflows/MtCommunionCliWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Intent -> Sentiment -> Route -> Reply -> Persist
