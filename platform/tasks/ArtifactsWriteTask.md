# Task: ArtifactsWriteTask

> Capability #62 — **Artifacts Write**

Atomic executable unit(s) for this capability.

### Task: UploadArtifactTask

```typescript
// task: UploadArtifactTask
const UploadArtifactTaskSpec: TaskSpecification = {
  taskId: 'UploadArtifactTask',
  operationRef: 'ArtifactsWriteProtocol',
  inputSchema: { capability: 'Artifacts Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute UploadArtifactTask

## Related artifacts
- [Protocol](../protocols/ArtifactsWriteProtocol.md) · [Trigger(s)](../triggers/ArtifactsWriteTrigger.md) · [Workflow](../workflows/ArtifactsWriteWorkflow.md)
