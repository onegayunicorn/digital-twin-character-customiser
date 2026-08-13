# Protocol: IdentityPqcSigningProtocol

> Capability #163 — **Identity & PQC Signing** · Domain: Access & Zero Trust · Access: `write`

## Purpose
DID registry, Knox Bio-Node attestation binding, PQC (Dilithium) signing interface — STUB (HMAC stand-in, not real PQC), Gaya Wallet MPC m-of-n signing, Quantum Lineage Bridge.

## Interface contract
```typescript
// protocol: IdentityPqcSigningProtocol
interface IdentityPqcSigningProtocol extends BaseOperation {
  id: string;
  name: 'Identity & PQC Signing';
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
| Trigger(s) | [`DidVerifiedTrigger`](../triggers/IdentityPqcSigningTrigger.md), [`KnoxAttestedTrigger`](../triggers/IdentityPqcSigningTrigger.md) |
| Task(s) | [`CreateDidTask`](../tasks/IdentityPqcSigningTask.md), [`SignPqcTask`](../tasks/IdentityPqcSigningTask.md), [`BindKnoxTask`](../tasks/IdentityPqcSigningTask.md) |
| Workflow | [`IdentityPqcSigningWorkflow`](../workflows/IdentityPqcSigningWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create DID -> Bind -> Attest -> Sign -> Verify -> Report
