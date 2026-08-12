# Protocol: TrustAndSafetyWriteProtocol

> Capability #52 — **Trust and Safety Write** · Domain: Security & Edge · Access: `write`

## Purpose
Content policies, moderation rules, reporting, and takedown.

## Interface contract
```typescript
// protocol: TrustAndSafetyWriteProtocol
interface TrustAndSafetyWriteProtocol extends BaseOperation {
  id: string;
  name: 'Trust and Safety Write';
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
| Trigger(s) | [`ContentReportedTrigger`](../triggers/TrustAndSafetyWriteTrigger.md), [`PolicyUpdatedTrigger`](../triggers/TrustAndSafetyWriteTrigger.md) |
| Task(s) | [`UpdateTrustSafetyPolicyTask`](../tasks/TrustAndSafetyWriteTask.md) |
| Workflow | [`TrustAndSafetyWriteWorkflow`](../workflows/TrustAndSafetyWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Review -> Classify -> Action -> Notify -> Log
