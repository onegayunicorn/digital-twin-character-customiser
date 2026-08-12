# Task: TurnstileSitesWriteTask

> Capability #53 — **Turnstile Sites Write**

Atomic executable unit(s) for this capability.

### Task: ConfigureTurnstileSiteTask

```typescript
// task: ConfigureTurnstileSiteTask
const ConfigureTurnstileSiteTaskSpec: TaskSpecification = {
  taskId: 'ConfigureTurnstileSiteTask',
  operationRef: 'TurnstileSitesWriteProtocol',
  inputSchema: { capability: 'Turnstile Sites Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ConfigureTurnstileSiteTask

## Related artifacts
- [Protocol](../protocols/TurnstileSitesWriteProtocol.md) · [Trigger(s)](../triggers/TurnstileSitesWriteTrigger.md) · [Workflow](../workflows/TurnstileSitesWriteWorkflow.md)
