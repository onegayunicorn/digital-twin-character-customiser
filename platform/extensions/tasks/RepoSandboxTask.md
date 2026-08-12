# Task: RepoSandboxTask

> Capability #152 — **Repo Sandbox**

Atomic executable unit(s) for this capability.

### Task: GenerateSandboxTask

```typescript
// task: GenerateSandboxTask
const GenerateSandboxTaskSpec: TaskSpecification = {
  taskId: 'GenerateSandboxTask',
  operationRef: 'RepoSandboxProtocol',
  inputSchema: { capability: 'Repo Sandbox' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute GenerateSandboxTask

### Task: InstantiateRepoAgentTask

```typescript
// task: InstantiateRepoAgentTask
const InstantiateRepoAgentTaskSpec: TaskSpecification = {
  taskId: 'InstantiateRepoAgentTask',
  operationRef: 'RepoSandboxProtocol',
  inputSchema: { capability: 'Repo Sandbox' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute InstantiateRepoAgentTask

## Related artifacts
- [Protocol](../protocols/RepoSandboxProtocol.md) · [Trigger(s)](../triggers/RepoSandboxTrigger.md) · [Workflow](../workflows/RepoSandboxWorkflow.md)
