# Protocol: AiSearchWriteProtocol

> Capability #4 — **AI Search Write** · Domain: Agents & AI / Automation · Access: `write`

## Purpose
Index management, ingestion, embeddings, and ranking configuration for AI search.

## Interface contract
```typescript
// protocol: AiSearchWriteProtocol
interface AiSearchWriteProtocol extends BaseOperation {
  id: string;
  name: 'AI Search Write';
  accessLevel: 'write';
  category: 'Agents & AI / Automation';
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
| Trigger(s) | [`DocumentIngestedTrigger`](../triggers/AiSearchWriteTrigger.md), [`IndexUpdatedTrigger`](../triggers/AiSearchWriteTrigger.md) |
| Task(s) | [`ManageAISearchIndexTask`](../tasks/AiSearchWriteTask.md) |
| Workflow | [`AiSearchWriteWorkflow`](../workflows/AiSearchWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Extract -> Embed -> Index -> Optimize
