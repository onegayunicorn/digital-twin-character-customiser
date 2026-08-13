# Task: AgentTriggerBusTask

> Capability #168 — **Agent Trigger Bus**

Atomic executable unit(s) for this capability.

### Task: RouteTriggerTask

```typescript
// task: RouteTriggerTask
const RouteTriggerTaskSpec: TaskSpecification = {
  taskId: 'RouteTriggerTask',
  operationRef: 'AgentTriggerBusProtocol',
  inputSchema: { capability: 'Agent Trigger Bus' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute RouteTriggerTask

### Task: WakeAgentTask

```typescript
// task: WakeAgentTask
const WakeAgentTaskSpec: TaskSpecification = {
  taskId: 'WakeAgentTask',
  operationRef: 'AgentTriggerBusProtocol',
  inputSchema: { capability: 'Agent Trigger Bus' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute WakeAgentTask

## Related artifacts
- [Protocol](../protocols/AgentTriggerBusProtocol.md) · [Trigger(s)](../triggers/AgentTriggerBusTrigger.md) · [Workflow](../workflows/AgentTriggerBusWorkflow.md)
