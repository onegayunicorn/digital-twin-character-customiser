# Protocol: AgentMemoryWriteProtocol

> Capability #1 — **Agent Memory Write** · Domain: Agents & AI / Automation · Access: `write`

## Purpose
Defines memory CRUD, persistence, scope, TTL, and access controls for agent memory records.

## Interface contract
```typescript
// protocol: AgentMemoryWriteProtocol
interface AgentMemoryWriteProtocol extends BaseOperation {
  id: string;
  name: 'Agent Memory Write';
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
| Trigger(s) | [`AgentMemoryUpdatedTrigger (on memory entry created/updated/expired)`](../triggers/AgentMemoryWriteTrigger.md) |
| Task(s) | [`WriteAgentMemoryTask (persist/modify agent memory records)`](../tasks/AgentMemoryWriteTask.md) |
| Workflow | [`AgentMemoryWriteWorkflow`](../workflows/AgentMemoryWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Validate -> Write -> Replicate -> Notify
