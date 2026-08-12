# Task: HealthcareAgencyTask

> Capability #143 — **Healthcare Agency**

Atomic executable unit(s) for this capability.

### Task: DispatchAgencyAgentTask

```typescript
// task: DispatchAgencyAgentTask
const DispatchAgencyAgentTaskSpec: TaskSpecification = {
  taskId: 'DispatchAgencyAgentTask',
  operationRef: 'HealthcareAgencyProtocol',
  inputSchema: { capability: 'Healthcare Agency' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute DispatchAgencyAgentTask

### Task: AuditHealthcareActionTask

```typescript
// task: AuditHealthcareActionTask
const AuditHealthcareActionTaskSpec: TaskSpecification = {
  taskId: 'AuditHealthcareActionTask',
  operationRef: 'HealthcareAgencyProtocol',
  inputSchema: { capability: 'Healthcare Agency' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute AuditHealthcareActionTask

## Related artifacts
- [Protocol](../protocols/HealthcareAgencyProtocol.md) · [Trigger(s)](../triggers/HealthcareAgencyTrigger.md) · [Workflow](../workflows/HealthcareAgencyWorkflow.md)
