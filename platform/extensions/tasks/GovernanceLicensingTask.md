# Task: GovernanceLicensingTask

> Capability #165 — **Governance & Licensing**

Atomic executable unit(s) for this capability.

### Task: RunCouncilVoteTask

```typescript
// task: RunCouncilVoteTask
const RunCouncilVoteTaskSpec: TaskSpecification = {
  taskId: 'RunCouncilVoteTask',
  operationRef: 'GovernanceLicensingProtocol',
  inputSchema: { capability: 'Governance & Licensing' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RunCouncilVoteTask

### Task: SplitRevenueTask

```typescript
// task: SplitRevenueTask
const SplitRevenueTaskSpec: TaskSpecification = {
  taskId: 'SplitRevenueTask',
  operationRef: 'GovernanceLicensingProtocol',
  inputSchema: { capability: 'Governance & Licensing' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute SplitRevenueTask

### Task: PublishPolicyTask

```typescript
// task: PublishPolicyTask
const PublishPolicyTaskSpec: TaskSpecification = {
  taskId: 'PublishPolicyTask',
  operationRef: 'GovernanceLicensingProtocol',
  inputSchema: { capability: 'Governance & Licensing' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute PublishPolicyTask

## Related artifacts
- [Protocol](../protocols/GovernanceLicensingProtocol.md) · [Trigger(s)](../triggers/GovernanceLicensingTrigger.md) · [Workflow](../workflows/GovernanceLicensingWorkflow.md)
