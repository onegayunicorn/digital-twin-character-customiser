# Protocol: ArtifactsWriteProtocol

> Capability #62 — **Artifacts Write** · Domain: Security & Edge · Access: `write`

## Purpose
Binary assets, versions, signing, distribution, and retention for artifacts.

## Interface contract
```typescript
// protocol: ArtifactsWriteProtocol
interface ArtifactsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Artifacts Write';
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
| Trigger(s) | [`ArtifactUploadedTrigger`](../triggers/ArtifactsWriteTrigger.md) |
| Task(s) | [`UploadArtifactTask`](../tasks/ArtifactsWriteTask.md) |
| Workflow | [`ArtifactsWriteWorkflow`](../workflows/ArtifactsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Build -> Sign -> Upload -> Index -> Distribute
