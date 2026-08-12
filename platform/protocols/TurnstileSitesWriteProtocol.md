# Protocol: TurnstileSitesWriteProtocol

> Capability #53 — **Turnstile Sites Write** · Domain: Security & Edge · Access: `write`

## Purpose
Site keys, challenge settings, widget configuration, and allowed origins for Turnstile.

## Interface contract
```typescript
// protocol: TurnstileSitesWriteProtocol
interface TurnstileSitesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Turnstile Sites Write';
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
| Trigger(s) | [`TurnstileConfigUpdatedTrigger`](../triggers/TurnstileSitesWriteTrigger.md) |
| Task(s) | [`ConfigureTurnstileSiteTask`](../tasks/TurnstileSitesWriteTask.md) |
| Workflow | [`TurnstileSitesWriteWorkflow`](../workflows/TurnstileSitesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register site -> Set challenge mode -> Install -> Verify
