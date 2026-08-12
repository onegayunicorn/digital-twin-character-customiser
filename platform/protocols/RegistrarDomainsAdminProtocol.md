# Protocol: RegistrarDomainsAdminProtocol

> Capability #33 — **Registrar Domains Admin** · Domain: Domain, DNS & Networking · Access: `admin`

## Purpose
Domain registration, transfer, renewal, auth codes, and lock.

## Interface contract
```typescript
// protocol: RegistrarDomainsAdminProtocol
interface RegistrarDomainsAdminProtocol extends BaseOperation {
  id: string;
  name: 'Registrar Domains Admin';
  accessLevel: 'admin';
  category: 'Domain, DNS & Networking';
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
| Trigger(s) | [`DomainEventTrigger`](../triggers/RegistrarDomainsAdminTrigger.md), [`ExpiryWarningTrigger`](../triggers/RegistrarDomainsAdminTrigger.md) |
| Task(s) | [`ManageDomainTask`](../tasks/RegistrarDomainsAdminTask.md) |
| Workflow | [`RegistrarDomainsAdminWorkflow`](../workflows/RegistrarDomainsAdminWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Check availability -> Register -> Configure DNS -> Activate
