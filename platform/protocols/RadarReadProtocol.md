# Protocol: RadarReadProtocol

> Capability #97 — **Radar Read** · Domain: Access & Zero Trust · Access: `read`

## Purpose
Internet traffic stats, outages, trends, and BGP changes from Radar.

## Interface contract
```typescript
// protocol: RadarReadProtocol
interface RadarReadProtocol extends BaseOperation {
  id: string;
  name: 'Radar Read';
  accessLevel: 'read';
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
| Trigger(s) | [`RadarDataUpdatedTrigger`](../triggers/RadarReadTrigger.md) |
| Task(s) | [`ReadRadarDataTask`](../tasks/RadarReadTask.md) |
| Workflow | [`RadarReadWorkflow`](../workflows/RadarReadWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Query -> Analyze -> Visualize -> Report
