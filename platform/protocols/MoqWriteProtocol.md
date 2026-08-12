# Protocol: MoqWriteProtocol

> Capability #81 — **MoQ Write** · Domain: Media & Streaming · Access: `write`

## Purpose
Media over QUIC ingest, distribution, and latency settings.

## Interface contract
```typescript
// protocol: MoqWriteProtocol
interface MoqWriteProtocol extends BaseOperation {
  id: string;
  name: 'MoQ Write';
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
| Trigger(s) | [`MoQStreamStartTrigger`](../triggers/MoqWriteTrigger.md) |
| Task(s) | [`ConfigureMoQEndpointTask`](../tasks/MoqWriteTask.md) |
| Workflow | [`MoqWriteWorkflow`](../workflows/MoqWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Ingest -> Transcode -> Distribute -> Playback -> Monitor
