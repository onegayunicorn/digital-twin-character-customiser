# Protocol: RegistrarSandboxDomainsAdminProtocol

> Capability #34 — **Registrar Sandbox Domains Admin** · Domain: Domain, DNS & Networking · Access: `admin`

## Purpose
Test domain provisioning, isolation, expiry, and cleanup.

## Interface contract
```typescript
// protocol: RegistrarSandboxDomainsAdminProtocol
interface RegistrarSandboxDomainsAdminProtocol extends BaseOperation {
  id: string;
  name: 'Registrar Sandbox Domains Admin';
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
| Trigger(s) | [`SandboxDomainCreatedTrigger`](../triggers/RegistrarSandboxDomainsAdminTrigger.md) |
| Task(s) | [`ProvisionSandboxDomainTask`](../tasks/RegistrarSandboxDomainsAdminTask.md) |
| Workflow | [`RegistrarSandboxDomainsAdminWorkflow`](../workflows/RegistrarSandboxDomainsAdminWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create -> Assign -> Test -> Expire -> Cleanup
