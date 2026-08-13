# Protocol: AgentTriggerBusProtocol

> Capability #168 — **Agent Trigger Bus** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Autonomous wake-up layer: declarative topic -> agent routing for the 13-agent roster (identity/payment/escrow/compliance/governance/twin/offgrid flows).

## Interface contract
```typescript
// protocol: AgentTriggerBusProtocol
interface AgentTriggerBusProtocol extends BaseOperation {
  id: string;
  name: 'Agent Trigger Bus';
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
| Trigger(s) | [`AnyPlatformEventTrigger`](../triggers/AgentTriggerBusTrigger.md) |
| Task(s) | [`RouteTriggerTask`](../tasks/AgentTriggerBusTask.md), [`WakeAgentTask`](../tasks/AgentTriggerBusTask.md) |
| Workflow | [`AgentTriggerBusWorkflow`](../workflows/AgentTriggerBusWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Event -> Route -> Wake agents -> Collect results -> Log
