# Protocol: AgentOrchestrationProtocol

> Capability #133 — **Agent Orchestration** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Sovereign orchestrator core: agent lifecycle state machine, priority task queue, scheduler tick loop, memory stores, tool ACL, audit chain.

## Interface contract
```typescript
// protocol: AgentOrchestrationProtocol
interface AgentOrchestrationProtocol extends BaseOperation {
  id: string;
  name: 'Agent Orchestration';
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
| Trigger(s) | [`TaskQueuedTrigger`](../triggers/AgentOrchestrationTrigger.md), [`AgentReadyTrigger`](../triggers/AgentOrchestrationTrigger.md) |
| Task(s) | [`DispatchTaskTask`](../tasks/AgentOrchestrationTask.md), [`RegisterAgentTask`](../tasks/AgentOrchestrationTask.md) |
| Workflow | [`AgentOrchestrationWorkflow`](../workflows/AgentOrchestrationWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Enqueue -> Schedule -> Execute -> Audit
