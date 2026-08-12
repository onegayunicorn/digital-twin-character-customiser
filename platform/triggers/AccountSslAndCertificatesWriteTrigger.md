# Trigger: AccountSslAndCertificatesWriteTrigger

> Capability #73 — **Account: SSL and Certificates Write**

Event source(s) that initiate execution for this capability.

### Trigger: CertExpiryTrigger

```typescript
// trigger: CertExpiryTrigger
const CertExpiryTriggerContract: TriggerContract = {
  triggerId: 'CertExpiryTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for CertExpiryTrigger' },
  actionTarget: 'IssueDeployCertificateTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: CertRequestedTrigger

```typescript
// trigger: CertRequestedTrigger
const CertRequestedTriggerContract: TriggerContract = {
  triggerId: 'CertRequestedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for CertRequestedTrigger' },
  actionTarget: 'IssueDeployCertificateTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccountSslAndCertificatesWriteProtocol.md) · [Tasks](../tasks/AccountSslAndCertificatesWriteTask.md) · [Workflow](../workflows/AccountSslAndCertificatesWriteWorkflow.md)
