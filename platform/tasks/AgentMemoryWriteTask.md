# Task: AgentMemoryWriteTask

> Capability #1 — **Agent Memory Write**

Atomic executable unit(s) for this capability.

### Task: WriteAgentMemoryTask

```typescript
// task: WriteAgentMemoryTask
const WriteAgentMemoryTaskSpec: TaskSpecification = {
  taskId: 'WriteAgentMemoryTask',
  operationRef: 'AgentMemoryWriteProtocol',
  inputSchema: { capability: 'Agent Memory Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** persist/modify agent memory records

## Related artifacts
- [Protocol](../protocols/AgentMemoryWriteProtocol.md) · [Trigger(s)](../triggers/AgentMemoryWriteTrigger.md) · [Workflow](../workflows/AgentMemoryWriteWorkflow.md)
