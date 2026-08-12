# Task: AiGatewayWriteTask

> Capability #3 — **AI Gateway Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureAIGatewayTask

```typescript
// task: ConfigureAIGatewayTask
const ConfigureAIGatewayTaskSpec: TaskSpecification = {
  taskId: 'ConfigureAIGatewayTask',
  operationRef: 'AiGatewayWriteProtocol',
  inputSchema: { capability: 'AI Gateway Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureAIGatewayTask

## Related artifacts
- [Protocol](../protocols/AiGatewayWriteProtocol.md) · [Trigger(s)](../triggers/AiGatewayWriteTrigger.md) · [Workflow](../workflows/AiGatewayWriteWorkflow.md)
