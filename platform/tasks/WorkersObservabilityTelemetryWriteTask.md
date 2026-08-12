# Task: WorkersObservabilityTelemetryWriteTask

> Capability #25 — **Workers Observability Telemetry Write**

Atomic executable unit(s) for this capability.

### Task: ExportTelemetryTask

```typescript
// task: ExportTelemetryTask
const ExportTelemetryTaskSpec: TaskSpecification = {
  taskId: 'ExportTelemetryTask',
  operationRef: 'WorkersObservabilityTelemetryWriteProtocol',
  inputSchema: { capability: 'Workers Observability Telemetry Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ExportTelemetryTask

### Task: ConfigureTelemetryTask

```typescript
// task: ConfigureTelemetryTask
const ConfigureTelemetryTaskSpec: TaskSpecification = {
  taskId: 'ConfigureTelemetryTask',
  operationRef: 'WorkersObservabilityTelemetryWriteProtocol',
  inputSchema: { capability: 'Workers Observability Telemetry Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureTelemetryTask

## Related artifacts
- [Protocol](../protocols/WorkersObservabilityTelemetryWriteProtocol.md) · [Trigger(s)](../triggers/WorkersObservabilityTelemetryWriteTrigger.md) · [Workflow](../workflows/WorkersObservabilityTelemetryWriteWorkflow.md)
