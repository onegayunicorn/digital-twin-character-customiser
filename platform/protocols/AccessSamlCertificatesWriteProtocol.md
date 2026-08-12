# Protocol: AccessSamlCertificatesWriteProtocol

> Capability #113 — **Access: SAML Certificates Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Signing/encryption certs, metadata, and rollover for SAML.

## Interface contract
```typescript
// protocol: AccessSamlCertificatesWriteProtocol
interface AccessSamlCertificatesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: SAML Certificates Write';
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
| Trigger(s) | [`SAMLCertExpiryTrigger`](../triggers/AccessSamlCertificatesWriteTrigger.md) |
| Task(s) | [`ManageSAMLCertificateTask`](../tasks/AccessSamlCertificatesWriteTask.md) |
| Workflow | [`AccessSamlCertificatesWriteWorkflow`](../workflows/AccessSamlCertificatesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Generate -> Upload -> Update IdP -> Rollover -> Revoke old
