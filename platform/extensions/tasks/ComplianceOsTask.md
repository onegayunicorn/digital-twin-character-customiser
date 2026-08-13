# Task: ComplianceOsTask

> Capability #156 — **Compliance OS**

Atomic executable unit(s) for this capability.

### Task: RunGateChainTask

```typescript
// task: RunGateChainTask
const RunGateChainTaskSpec: TaskSpecification = {
  taskId: 'RunGateChainTask',
  operationRef: 'ComplianceOsProtocol',
  inputSchema: { capability: 'Compliance OS' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RunGateChainTask

### Task: LogComplianceEvidenceTask

```typescript
// task: LogComplianceEvidenceTask
const LogComplianceEvidenceTaskSpec: TaskSpecification = {
  taskId: 'LogComplianceEvidenceTask',
  operationRef: 'ComplianceOsProtocol',
  inputSchema: { capability: 'Compliance OS' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute LogComplianceEvidenceTask

## Related artifacts
- [Protocol](../protocols/ComplianceOsProtocol.md) · [Trigger(s)](../triggers/ComplianceOsTrigger.md) · [Workflow](../workflows/ComplianceOsWorkflow.md)
