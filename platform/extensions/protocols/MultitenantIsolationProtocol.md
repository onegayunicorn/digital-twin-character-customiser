# Protocol: MultitenantIsolationProtocol

> Capability #164 — **Multi-Tenant Isolation** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Per-tenant encryption keys, DID bindings, webhook secrets, expiry schedules, and isolated state stores.

## Interface contract
```typescript
// protocol: MultitenantIsolationProtocol
interface MultitenantIsolationProtocol extends BaseOperation {
  id: string;
  name: 'Multi-Tenant Isolation';
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
| Trigger(s) | [`TenantCreatedTrigger`](../triggers/MultitenantIsolationTrigger.md) |
| Task(s) | [`CreateTenantTask`](../tasks/MultitenantIsolationTask.md), [`DeriveTenantKeyTask`](../tasks/MultitenantIsolationTask.md) |
| Workflow | [`MultitenantIsolationWorkflow`](../workflows/MultitenantIsolationWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Register -> Derive keys -> Bind DID -> Isolate state -> Verify
