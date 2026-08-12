# Protocol: AiGatewayWriteProtocol

> Capability #3 — **AI Gateway Write** · Domain: Agents & AI / Automation · Access: `write`

## Purpose
Routing, rate limits, model access, authentication, and logging for AI inference.

## Interface contract
```typescript
// protocol: AiGatewayWriteProtocol
interface AiGatewayWriteProtocol extends BaseOperation {
  id: string;
  name: 'AI Gateway Write';
  accessLevel: 'write';
  category: 'Agents & AI / Automation';
  serviceDomain: string;
  enabled: boolean;
  auditLogging: boolean;
  rateLimit?: RateLimit;
  // capability-specific contract fields
}
```

## Related artifacts
| Type | File |
|---|---|
| Trigger(s) | [`AIRequestReceivedTrigger`](../triggers/AiGatewayWriteTrigger.md), [`AIMetricThresholdTrigger`](../triggers/AiGatewayWriteTrigger.md) |
| Task(s) | [`ConfigureAIGatewayTask`](../tasks/AiGatewayWriteTask.md) |
| Workflow | [`AiGatewayWriteWorkflow`](../workflows/AiGatewayWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define routes -> Attach models -> Set policies -> Deploy
