# Task: MedicalDecisionSupportTask

> Capability #138 — **Medical Decision Support**

Atomic executable unit(s) for this capability.

### Task: RunTriageTask

```typescript
// task: RunTriageTask
const RunTriageTaskSpec: TaskSpecification = {
  taskId: 'RunTriageTask',
  operationRef: 'MedicalDecisionSupportProtocol',
  inputSchema: { capability: 'Medical Decision Support' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RunTriageTask

### Task: ReviewCaseTask

```typescript
// task: ReviewCaseTask
const ReviewCaseTaskSpec: TaskSpecification = {
  taskId: 'ReviewCaseTask',
  operationRef: 'MedicalDecisionSupportProtocol',
  inputSchema: { capability: 'Medical Decision Support' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ReviewCaseTask

### Task: MatchLiteratureTask

```typescript
// task: MatchLiteratureTask
const MatchLiteratureTaskSpec: TaskSpecification = {
  taskId: 'MatchLiteratureTask',
  operationRef: 'MedicalDecisionSupportProtocol',
  inputSchema: { capability: 'Medical Decision Support' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute MatchLiteratureTask

## Related artifacts
- [Protocol](../protocols/MedicalDecisionSupportProtocol.md) · [Trigger(s)](../triggers/MedicalDecisionSupportTrigger.md) · [Workflow](../workflows/MedicalDecisionSupportWorkflow.md)
