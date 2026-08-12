# Task: AccessSamlCertificatesWriteTask

> Capability #113 — **Access: SAML Certificates Write**

Atomic executable unit(s) for this capability.

### Task: ManageSAMLCertificateTask

```typescript
// task: ManageSAMLCertificateTask
const ManageSAMLCertificateTaskSpec: TaskSpecification = {
  taskId: 'ManageSAMLCertificateTask',
  operationRef: 'AccessSamlCertificatesWriteProtocol',
  inputSchema: { capability: 'Access: SAML Certificates Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ManageSAMLCertificateTask

## Related artifacts
- [Protocol](../protocols/AccessSamlCertificatesWriteProtocol.md) · [Trigger(s)](../triggers/AccessSamlCertificatesWriteTrigger.md) · [Workflow](../workflows/AccessSamlCertificatesWriteWorkflow.md)
