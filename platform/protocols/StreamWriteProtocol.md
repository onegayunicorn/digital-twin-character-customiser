# Protocol: StreamWriteProtocol

> Capability #82 — **Stream Write** · Domain: Media & Streaming · Access: `write`

## Purpose
Live/VOD, transcoding, renditions, DRM, and manifests for Stream.

## Interface contract
```typescript
// protocol: StreamWriteProtocol
interface StreamWriteProtocol extends BaseOperation {
  id: string;
  name: 'Stream Write';
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
| Trigger(s) | [`StreamStartedTrigger`](../triggers/StreamWriteTrigger.md), [`StreamEndedTrigger`](../triggers/StreamWriteTrigger.md) |
| Task(s) | [`ManageStreamTask`](../tasks/StreamWriteTask.md) |
| Workflow | [`StreamWriteWorkflow`](../workflows/StreamWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create -> Ingest -> Transcode -> Publish -> View -> Archive
