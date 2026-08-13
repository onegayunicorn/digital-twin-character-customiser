# Protocol: ExpirySchedulerProtocol

> Capability #167 — **Expiry Scheduler** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Seven-day authorization expiry with hourly scheduler tick; expires stale authorizations.

## Interface contract
```typescript
// protocol: ExpirySchedulerProtocol
interface ExpirySchedulerProtocol extends BaseOperation {
  id: string;
  name: 'Expiry Scheduler';
  accessLevel: 'write';
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
| Trigger(s) | [`ExpiryTickTrigger`](../triggers/ExpirySchedulerTrigger.md), [`AuthorizationCreatedTrigger`](../triggers/ExpirySchedulerTrigger.md) |
| Task(s) | [`RegisterAuthorizationTask`](../tasks/ExpirySchedulerTask.md), [`RunExpiryTickTask`](../tasks/ExpirySchedulerTask.md) |
| Workflow | [`ExpirySchedulerWorkflow`](../workflows/ExpirySchedulerWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register -> Tick hourly -> Expire stale -> Notify
