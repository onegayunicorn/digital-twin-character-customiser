# Task: TallymanTask

> Capability #147 — **Tallyman**

Atomic executable unit(s) for this capability.

### Task: AggregateMetricsTask

```typescript
// task: AggregateMetricsTask
const AggregateMetricsTaskSpec: TaskSpecification = {
  taskId: 'AggregateMetricsTask',
  operationRef: 'TallymanProtocol',
  inputSchema: { capability: 'Tallyman' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute AggregateMetricsTask

### Task: FlagAnomalyTask

```typescript
// task: FlagAnomalyTask
const FlagAnomalyTaskSpec: TaskSpecification = {
  taskId: 'FlagAnomalyTask',
  operationRef: 'TallymanProtocol',
  inputSchema: { capability: 'Tallyman' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute FlagAnomalyTask

## Related artifacts
- [Protocol](../protocols/TallymanProtocol.md) · [Trigger(s)](../triggers/TallymanTrigger.md) · [Workflow](../workflows/TallymanWorkflow.md)
