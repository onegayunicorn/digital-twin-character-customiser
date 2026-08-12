# Task: UrlScannerWriteTask

> Capability #54 — **URL Scanner Write**

Atomic executable unit(s) for this capability.

### Task: ScanURLTask

```typescript
// task: ScanURLTask
const ScanURLTaskSpec: TaskSpecification = {
  taskId: 'ScanURLTask',
  operationRef: 'UrlScannerWriteProtocol',
  inputSchema: { capability: 'URL Scanner Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ScanURLTask

## Related artifacts
- [Protocol](../protocols/UrlScannerWriteProtocol.md) · [Trigger(s)](../triggers/UrlScannerWriteTrigger.md) · [Workflow](../workflows/UrlScannerWriteWorkflow.md)
