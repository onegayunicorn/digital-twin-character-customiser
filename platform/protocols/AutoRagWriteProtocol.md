# Protocol: AutoRagWriteProtocol

> Capability #5 — **Auto Rag Write** · Domain: Agents & AI / Automation · Access: `write`

## Purpose
Source connectors, chunking, retrieval logic, and generation settings for RAG pipelines.

## Interface contract
```typescript
// protocol: AutoRagWriteProtocol
interface AutoRagWriteProtocol extends BaseOperation {
  id: string;
  name: 'Auto Rag Write';
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
| Trigger(s) | [`NewDataSourceDetectedTrigger`](../triggers/AutoRagWriteTrigger.md), [`ScheduleRAGUpdateTrigger`](../triggers/AutoRagWriteTrigger.md) |
| Task(s) | [`ConfigureAutoRAGTask`](../tasks/AutoRagWriteTask.md) |
| Workflow | [`AutoRagWriteWorkflow`](../workflows/AutoRagWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Connect source -> Chunk -> Embed -> Store -> Test query
