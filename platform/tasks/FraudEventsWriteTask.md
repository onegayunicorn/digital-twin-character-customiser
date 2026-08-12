# Task: FraudEventsWriteTask

> Capability #45 — **Fraud Events Write**

Atomic executable unit(s) for this capability.

### Task: LogFraudEventTask

```typescript
// task: LogFraudEventTask
const LogFraudEventTaskSpec: TaskSpecification = {
  taskId: 'LogFraudEventTask',
  operationRef: 'FraudEventsWriteProtocol',
  inputSchema: { capability: 'Fraud Events Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute LogFraudEventTask

### Task: ScoreFraudRiskTask

```typescript
// task: ScoreFraudRiskTask
const ScoreFraudRiskTaskSpec: TaskSpecification = {
  taskId: 'ScoreFraudRiskTask',
  operationRef: 'FraudEventsWriteProtocol',
  inputSchema: { capability: 'Fraud Events Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ScoreFraudRiskTask

## Related artifacts
- [Protocol](../protocols/FraudEventsWriteProtocol.md) · [Trigger(s)](../triggers/FraudEventsWriteTrigger.md) · [Workflow](../workflows/FraudEventsWriteWorkflow.md)
