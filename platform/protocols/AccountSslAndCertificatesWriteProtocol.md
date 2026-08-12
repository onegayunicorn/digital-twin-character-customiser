# Protocol: AccountSslAndCertificatesWriteProtocol

> Capability #73 — **Account: SSL and Certificates Write** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
Certificate issuance, renewal, validation, deployment, and revocation.

## Interface contract
```typescript
// protocol: AccountSslAndCertificatesWriteProtocol
interface AccountSslAndCertificatesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Account: SSL and Certificates Write';
  accessLevel: 'write';
  category: 'Account, Auth, Email & Billing';
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
| Trigger(s) | [`CertExpiryTrigger`](../triggers/AccountSslAndCertificatesWriteTrigger.md), [`CertRequestedTrigger`](../triggers/AccountSslAndCertificatesWriteTrigger.md) |
| Task(s) | [`IssueDeployCertificateTask`](../tasks/AccountSslAndCertificatesWriteTask.md) |
| Workflow | [`AccountSslAndCertificatesWriteWorkflow`](../workflows/AccountSslAndCertificatesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Request -> Validate -> Issue -> Deploy -> Renew -> Revoke
