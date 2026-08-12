# Trigger: AccessMutualTlsCertificatesWriteTrigger

> Capability #107 — **Access: Mutual TLS Certificates Write**

Event source(s) that initiate execution for this capability.

### Trigger: MTLSCertUploadedTrigger

```typescript
// trigger: MTLSCertUploadedTrigger
const MTLSCertUploadedTriggerContract: TriggerContract = {
  triggerId: 'MTLSCertUploadedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MTLSCertUploadedTrigger' },
  actionTarget: 'UploadMTLSCertificateTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/AccessMutualTlsCertificatesWriteProtocol.md) · [Tasks](../tasks/AccessMutualTlsCertificatesWriteTask.md) · [Workflow](../workflows/AccessMutualTlsCertificatesWriteWorkflow.md)
