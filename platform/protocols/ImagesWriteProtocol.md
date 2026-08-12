# Protocol: ImagesWriteProtocol

> Capability #80 — **Images Write** · Domain: Media & Streaming · Access: `write`

## Purpose
Upload, resizing, format conversion, metadata, and variants for Images.

## Interface contract
```typescript
// protocol: ImagesWriteProtocol
interface ImagesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Images Write';
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
| Trigger(s) | [`ImageUploadedTrigger`](../triggers/ImagesWriteTrigger.md) |
| Task(s) | [`UploadTransformImageTask`](../tasks/ImagesWriteTask.md) |
| Workflow | [`ImagesWriteWorkflow`](../workflows/ImagesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Upload -> Validate -> Transform -> Store -> Deliver
