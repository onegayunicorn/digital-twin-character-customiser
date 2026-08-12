# Protocol: VectorizeWriteProtocol

> Capability #20 — **Vectorize Write** · Domain: Storage & Data · Access: `write`

## Purpose
Vector ingestion, dimensions, indexing, and distance metrics for Vectorize.

## Interface contract
```typescript
// protocol: VectorizeWriteProtocol
interface VectorizeWriteProtocol extends BaseOperation {
  id: string;
  name: 'Vectorize Write';
  accessLevel: 'write';
  category: 'Storage & Data';
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
| Trigger(s) | [`VectorBatchTrigger`](../triggers/VectorizeWriteTrigger.md), [`EmbeddingGeneratedTrigger`](../triggers/VectorizeWriteTrigger.md) |
| Task(s) | [`IngestVectorsTask`](../tasks/VectorizeWriteTask.md), [`BuildVectorIndexTask`](../tasks/VectorizeWriteTask.md) |
| Workflow | [`VectorizeWriteWorkflow`](../workflows/VectorizeWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Generate embeddings -> Insert -> Index -> Optimize
