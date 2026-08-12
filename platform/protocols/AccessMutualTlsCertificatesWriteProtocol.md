# Protocol: AccessMutualTlsCertificatesWriteProtocol

> Capability #107 — **Access: Mutual TLS Certificates Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Client certs, CA bundles, validation rules, and revocation for mTLS.

## Interface contract
```typescript
// protocol: AccessMutualTlsCertificatesWriteProtocol
interface AccessMutualTlsCertificatesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: Mutual TLS Certificates Write';
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
| Trigger(s) | [`MTLSCertUploadedTrigger`](../triggers/AccessMutualTlsCertificatesWriteTrigger.md) |
| Task(s) | [`UploadMTLSCertificateTask`](../tasks/AccessMutualTlsCertificatesWriteTask.md) |
| Workflow | [`AccessMutualTlsCertificatesWriteWorkflow`](../workflows/AccessMutualTlsCertificatesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Upload CA -> Require cert -> Validate -> Enforce
