# Protocol: GatekeeperProtocol

> Capability #145 — **Gatekeeper** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Policy gate: blocks unverified claim markers and enforces ACLs. The enforcement point of the claims register.

## Interface contract
```typescript
// protocol: GatekeeperProtocol
interface GatekeeperProtocol extends BaseOperation {
  id: string;
  name: 'Gatekeeper';
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
| Trigger(s) | [`ContentSubmittedTrigger`](../triggers/GatekeeperTrigger.md), [`AccessRequestTrigger`](../triggers/GatekeeperTrigger.md) |
| Task(s) | [`CheckClaimsTask`](../tasks/GatekeeperTask.md), [`CheckAclTask`](../tasks/GatekeeperTask.md) |
| Workflow | [`GatekeeperWorkflow`](../workflows/GatekeeperWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Submit -> Check claims -> Check ACL -> Allow/Block -> Log
