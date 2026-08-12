# Task: ApplicationSecurityReportsReadTask

> Capability #40 — **Application Security Reports Read**

Atomic executable unit(s) for this capability.

### Task: GenerateAppSecReportTask

```typescript
// task: GenerateAppSecReportTask
const GenerateAppSecReportTaskSpec: TaskSpecification = {
  taskId: 'GenerateAppSecReportTask',
  operationRef: 'ApplicationSecurityReportsReadProtocol',
  inputSchema: { capability: 'Application Security Reports Read' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute GenerateAppSecReportTask

## Related artifacts
- [Protocol](../protocols/ApplicationSecurityReportsReadProtocol.md) · [Trigger(s)](../triggers/ApplicationSecurityReportsReadTrigger.md) · [Workflow](../workflows/ApplicationSecurityReportsReadWorkflow.md)
