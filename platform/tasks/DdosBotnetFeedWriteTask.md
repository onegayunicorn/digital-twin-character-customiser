# Task: DdosBotnetFeedWriteTask

> Capability #42 — **DDoS Botnet Feed Write**

Atomic executable unit(s) for this capability.

### Task: IngestBotnetFeedTask

```typescript
// task: IngestBotnetFeedTask
const IngestBotnetFeedTaskSpec: TaskSpecification = {
  taskId: 'IngestBotnetFeedTask',
  operationRef: 'DdosBotnetFeedWriteProtocol',
  inputSchema: { capability: 'DDoS Botnet Feed Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute IngestBotnetFeedTask

## Related artifacts
- [Protocol](../protocols/DdosBotnetFeedWriteProtocol.md) · [Trigger(s)](../triggers/DdosBotnetFeedWriteTrigger.md) · [Workflow](../workflows/DdosBotnetFeedWriteWorkflow.md)
