# Task: AgentOrchestrationTask

> Capability #133 — **Agent Orchestration**

Atomic executable unit(s) for this capability.

### Task: DispatchTaskTask

```typescript
// task: DispatchTaskTask
const DispatchTaskTaskSpec: TaskSpecification = {
  taskId: 'DispatchTaskTask',
  operationRef: 'AgentOrchestrationProtocol',
  inputSchema: { capability: 'Agent Orchestration' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute DispatchTaskTask

### Task: RegisterAgentTask

```typescript
// task: RegisterAgentTask
const RegisterAgentTaskSpec: TaskSpecification = {
  taskId: 'RegisterAgentTask',
  operationRef: 'AgentOrchestrationProtocol',
  inputSchema: { capability: 'Agent Orchestration' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RegisterAgentTask

## Related artifacts
- [Protocol](../protocols/AgentOrchestrationProtocol.md) · [Trigger(s)](../triggers/AgentOrchestrationTrigger.md) · [Workflow](../workflows/AgentOrchestrationWorkflow.md)
