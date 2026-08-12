# Protocol: ChatAgentProtocol

> Capability #148 — **Chat Agent** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Operator dialogue router: intent -> governance agent or direct reply; refuses quarantined requests.

## Interface contract
```typescript
// protocol: ChatAgentProtocol
interface ChatAgentProtocol extends BaseOperation {
  id: string;
  name: 'Chat Agent';
  accessLevel: 'write';
  category: 'Access & Zero Trust';
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
| Trigger(s) | [`MessageReceivedTrigger`](../triggers/ChatAgentTrigger.md) |
| Task(s) | [`RouteIntentTask`](../tasks/ChatAgentTask.md), [`RefuseQuarantinedTask`](../tasks/ChatAgentTask.md) |
| Workflow | [`ChatAgentWorkflow`](../workflows/ChatAgentWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Parse -> Classify -> Route/Refuse -> Reply
