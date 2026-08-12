# Task: AccessMutualTlsCertificatesWriteTask

> Capability #107 — **Access: Mutual TLS Certificates Write**

Atomic executable unit(s) for this capability.

### Task: UploadMTLSCertificateTask

```typescript
// task: UploadMTLSCertificateTask
const UploadMTLSCertificateTaskSpec: TaskSpecification = {
  taskId: 'UploadMTLSCertificateTask',
  operationRef: 'AccessMutualTlsCertificatesWriteProtocol',
  inputSchema: { capability: 'Access: Mutual TLS Certificates Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UploadMTLSCertificateTask

## Related artifacts
- [Protocol](../protocols/AccessMutualTlsCertificatesWriteProtocol.md) · [Trigger(s)](../triggers/AccessMutualTlsCertificatesWriteTrigger.md) · [Workflow](../workflows/AccessMutualTlsCertificatesWriteWorkflow.md)
