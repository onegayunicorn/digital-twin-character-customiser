# Trigger: AccessSamlCertificatesWriteTrigger

> Capability #113 — **Access: SAML Certificates Write**

Event source(s) that initiate execution for this capability.

### Trigger: SAMLCertExpiryTrigger

```typescript
// trigger: SAMLCertExpiryTrigger
const SAMLCertExpiryTriggerContract: TriggerContract = {
  triggerId: 'SAMLCertExpiryTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for SAMLCertExpiryTrigger' },
  actionTarget: 'ManageSAMLCertificateTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessSamlCertificatesWriteProtocol.md) · [Tasks](../tasks/AccessSamlCertificatesWriteTask.md) · [Workflow](../workflows/AccessSamlCertificatesWriteWorkflow.md)
