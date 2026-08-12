# Protocol: FlagshipWriteProtocol

> Capability #28 — **Flagship Write** · Domain: Observability & Telemetry · Access: `write`

## Purpose
Feature flags, rollouts, targeting, and experiments.

## Interface contract
```typescript
// protocol: FlagshipWriteProtocol
interface FlagshipWriteProtocol extends BaseOperation {
  id: string;
  name: 'Flagship Write';
  accessLevel: 'write';
  category: 'Observability & Telemetry';
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
| Trigger(s) | [`FlagChangedTrigger`](../triggers/FlagshipWriteTrigger.md), [`ScheduleFlagTrigger`](../triggers/FlagshipWriteTrigger.md) |
| Task(s) | [`ManageFeatureFlagTask`](../tasks/FlagshipWriteTask.md) |
| Workflow | [`FlagshipWriteWorkflow`](../workflows/FlagshipWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define -> Target -> Rollout -> Monitor -> Adjust
