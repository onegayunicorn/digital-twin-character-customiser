# Task: RadarReadTask

> Capability #97 — **Radar Read**

Atomic executable unit(s) for this capability.

### Task: ReadRadarDataTask

```typescript
// task: ReadRadarDataTask
const ReadRadarDataTaskSpec: TaskSpecification = {
  taskId: 'ReadRadarDataTask',
  operationRef: 'RadarReadProtocol',
  inputSchema: { capability: 'Radar Read' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ReadRadarDataTask

## Related artifacts
- [Protocol](../protocols/RadarReadProtocol.md) · [Trigger(s)](../triggers/RadarReadTrigger.md) · [Workflow](../workflows/RadarReadWorkflow.md)
