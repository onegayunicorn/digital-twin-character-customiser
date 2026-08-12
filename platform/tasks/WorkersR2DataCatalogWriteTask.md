# Task: WorkersR2DataCatalogWriteTask

> Capability #19 — **Workers R2 Data Catalog Write**

Atomic executable unit(s) for this capability.

### Task: UpdateR2DataCatalogTask

```typescript
// task: UpdateR2DataCatalogTask
const UpdateR2DataCatalogTaskSpec: TaskSpecification = {
  taskId: 'UpdateR2DataCatalogTask',
  operationRef: 'WorkersR2DataCatalogWriteProtocol',
  inputSchema: { capability: 'Workers R2 Data Catalog Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UpdateR2DataCatalogTask

## Related artifacts
- [Protocol](../protocols/WorkersR2DataCatalogWriteProtocol.md) · [Trigger(s)](../triggers/WorkersR2DataCatalogWriteTrigger.md) · [Workflow](../workflows/WorkersR2DataCatalogWriteWorkflow.md)
