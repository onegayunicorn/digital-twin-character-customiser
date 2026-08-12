# Task: FieldExtractorsWriteTask

> Capability #44 — **Field Extractors Write**

Atomic executable unit(s) for this capability.

### Task: CreateFieldExtractorTask

```typescript
// task: CreateFieldExtractorTask
const CreateFieldExtractorTaskSpec: TaskSpecification = {
  taskId: 'CreateFieldExtractorTask',
  operationRef: 'FieldExtractorsWriteProtocol',
  inputSchema: { capability: 'Field Extractors Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute CreateFieldExtractorTask

## Related artifacts
- [Protocol](../protocols/FieldExtractorsWriteProtocol.md) · [Trigger(s)](../triggers/FieldExtractorsWriteTrigger.md) · [Workflow](../workflows/FieldExtractorsWriteWorkflow.md)
